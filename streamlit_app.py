
import streamlit as st

st.set_page_config(
    page_title="EXO-PRIOR",
    page_icon="🪐",
    layout="wide"
)

st.title("🪐 EXO-PRIOR")
st.subheader("Exoplanet Investigation Prioritization")

st.write(
    "Explore exoplanets and prioritize which worlds "
    "deserve further scientific investigation."
)

st.info(
    "Prototype starting point: our next step is to "
    "connect real exoplanet data."
)

st.metric("Project status", "Getting started")

st.caption(
    "Investigation priority does not prove habitability "
    "or the existence of life."
)
