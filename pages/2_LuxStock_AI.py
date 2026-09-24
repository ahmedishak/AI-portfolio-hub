import streamlit as st

st.title("LuxStock AI")
st.write(
    "A merchandising desk for one week of sales. Load a CSV and see which SKUs may stock out, and the revenue at stake."
)
st.write(
    "The figures come from the spreadsheet. The model only writes the supplier email. Approving the draft records the decision in the activity trail."
)
st.write("I built the scoring, the dashboard, and the draft step.")
st.link_button("Open LuxStock AI", "https://lux-stock-ai.vercel.app/")
st.markdown(
    """
**Try this:** Load sample week (`Shift+D`). Read the overview. Open Alerts, draft an email, then Approve.
"""
)
