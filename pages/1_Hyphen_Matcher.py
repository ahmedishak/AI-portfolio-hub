import streamlit as st

st.title("Hyphen Matcher")
st.write("Staff tool: paste a candidate background, get an advisory UK route plus policy and citations. Not an admissions decision.")
st.link_button("Open app", "https://hyphen-matcher-app-v2.vercel.app/sign-in?redirect_url=https%3A%2F%2Fhyphen-matcher-app-v2.vercel.app%2F")
st.markdown("""
**Routes:** INTO · iO-Sphere · Foundation · HOLD

**Demo:** open `/` → German Abitur (expect iO-Sphere) → Missing docs (expect HOLD) → Analytics.
""")
