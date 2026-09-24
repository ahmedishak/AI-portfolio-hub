import streamlit as st

st.title("Hyphen Matcher")
st.write(
    "Staff paste a candidate's background and get an advisory UK route, the policy behind it, and citations."
)
st.write(
    "The route is INTO, iO-Sphere, Foundation, or HOLD. It is guidance for a person to review, and it is not an admissions decision."
)
st.write("I built the matcher, the policy checks, and the analytics view of past evaluations.")
st.link_button("Open Hyphen Matcher", "https://hyphen-matcher-app-v2.vercel.app/")
st.markdown(
    """
**Try this:** open the app and run German Abitur. Expect iO-Sphere. Then run Missing docs. Expect HOLD. Then open Analytics.
"""
)
