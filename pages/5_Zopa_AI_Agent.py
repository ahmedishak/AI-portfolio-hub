from pathlib import Path

import streamlit as st

st.title("Zopa AI Agent")
st.write("A 33-second recording of the agent running. The video has no sound.")

st.video(str(Path(__file__).resolve().parent.parent / "assets" / "zopa_ai_agent_demo.mp4"))
