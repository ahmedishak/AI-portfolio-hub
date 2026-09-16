import streamlit as st

st.title("LuxStock AI")
st.write("Merchandising copilot: ingest CSV, score stockout risk, draft a supplier email, log approve.")
st.link_button("Open app", "http://localhost:3004")
st.markdown("""
**Demo:** Load sample week (`Shift+D`) → Overview KPIs → Alerts → draft → Approve.

Frontend is `:3004`. API is `:8000`.
""")
