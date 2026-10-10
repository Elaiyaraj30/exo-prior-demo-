
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="EXO-PRIOR",
    page_icon="🪐",
    layout="wide"
)

st.title("🪐 EXO-PRIOR")
st.subheader("Exoplanet Investigation Prioritization")
st.write(
    "Explore confirmed exoplanets and identify worlds "
    "that deserve further scientific investigation."
)

@st.cache_data
def load_data():
    return pd.read_csv("nasa_planets300.csv")

try:
    df = load_data()
except Exception as e:
    st.error("Could not load nasa_planets.csv. Check that it exists in your GitHub repository.")
    st.stop()

df.columns = df.columns.str.strip()

# Find NASA column names
name_col = "pl_name" if "pl_name" in df.columns else df.columns[0]
host_col = "hostname" if "hostname" in df.columns else None

st.success(f"Loaded {len(df)} NASA planet records.")

search = st.text_input("🔎 Search for a planet")

filtered = df.copy()

if search:
    filtered = filtered[
        filtered[name_col].astype(str).str.contains(
            search, case=False, na=False
        )
    ]

if host_col:
    hosts = ["All stars"] + sorted(
        filtered[host_col].dropna().astype(str).unique().tolist()
    )
    selected_host = st.selectbox("Filter by host star", hosts)

    if selected_host != "All stars":
        filtered = filtered[
            filtered[host_col].astype(str) == selected_host
        ]

col1, col2 = st.columns(2)
col1.metric("Records displayed", len(filtered))
col2.metric(
    "Unique planets",
    filtered[name_col].nunique()
)

st.subheader("Planet catalogue")
st.dataframe(filtered, use_container_width=True, hide_index=True)

numeric_cols = filtered.select_dtypes(include="number").columns.tolist()

if numeric_cols:
    st.subheader("Explore a measurement")
    chosen_col = st.selectbox("Choose a numerical property", numeric_cols)

    chart_data = filtered[[name_col, chosen_col]].dropna().head(30)

    if not chart_data.empty:
        st.bar_chart(
            chart_data.set_index(name_col)[chosen_col]
        )

st.info(
    "Important: this dashboard displays catalogue data. "
    "It does not prove that any planet is habitable or contains life."
)

st.caption("EXO-PRIOR | NASA Exoplanet Archive data")
