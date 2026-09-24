import streamlit as st
import streamlit.components.v1 as components

st.title("AI Booking Agent")
st.write(
    "An interpreter-booking agent. Someone types a request in plain language. Copilot Studio captures the language, date, and format, then saves an Interpreter Request in Dataverse."
)
st.write(
    "When that row is created, Power Automate turns the raw record into a readable alert: it labels the language, formats the date, emails the team, and logs the request."
)
st.write("I built the Copilot Studio topics, the Dataverse table, and the Power Automate flow.")

st.subheader("Try this")
st.markdown(
    """
Ask it to book an interpreter. For example: Polish, face to face, 26 September 2026.

You should see it confirm the language, the format, and the date. Behind the frame, that becomes a Dataverse row and a stakeholder email.
"""
)

components.html(
    """
    <iframe src="https://copilotstudio.microsoft.com/environments/7bd48057-e801-e228-8286-4504dd585749/bots/cr21c_linguistic_69MIK1/canvas?__version__=2&enableFileAttachment=false&cliAgent=true" frameborder="0" style="width: 100%; height: 640px;"></iframe>
    """,
    height=640,
)

st.subheader("How it is wired")
st.image("pages/architecture.png")

with st.expander("How the alert gets a readable date and language"):
    st.markdown(
        """
Dataverse stores internal ids and raw timestamps. The flow reads the formatted language label and formats the date before the email goes out:

`body/cr21c_languagerequired@OData.Community.Display.V1.FormattedValue`

`formatDateTime(..., 'dd MMM yyyy')`
"""
    )
