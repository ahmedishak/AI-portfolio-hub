import streamlit as st
import streamlit.components.v1 as components

st.title("AI Booking Agent")

# Replace the URL below with your copied Demo website link
components.html("""
    <iframe src="https://copilotstudio.microsoft.com/environments/7bd48057-e801-e228-8286-4504dd585749/bots/cr21c_linguistic_69MIK1/canvas?__version__=2&enableFileAttachment=false&cliAgent=true" frameborder="0" style="width: 100%; height: 500px;"></iframe>
""", height=500)
