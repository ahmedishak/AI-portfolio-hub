import streamlit as st

st.title("Hyphen Matcher")
st.write("Staff tool: paste a candidate background, get an advisory UK route plus policy and citations. Not an admissions decision.")
st.link_button("Open app", "http://localhost:3000")
st.markdown("""
**Routes:** INTO · iO-Sphere · Foundation · HOLD

**Demo:** open `/` → German Abitur (expect iO-Sphere) → Missing docs (expect HOLD) → Analytics.
""")
