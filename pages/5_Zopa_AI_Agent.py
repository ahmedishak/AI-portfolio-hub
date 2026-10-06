from pathlib import Path

import streamlit as st

st.title("Zopa AI Money Assistant")
st.write(
    "A chat assistant for everyday banking. A customer asks in plain language, and the assistant reads their accounts and carries out the request."
)
st.write(
    "Money only moves after the customer says yes. The assistant repeats the amount and both accounts, waits for confirmation, then makes the transfer and returns a reference number."
)

st.write("I built it for Zopa Bank using Cursor and Claude Code.")

st.subheader("What the demo shows")
st.markdown(
    """
1. The customer asks for their current account balance. The assistant answers and notes there are no pending payments.
2. They ask to move £200 into Smart Saver. The assistant restates the transfer with both balances and asks before going ahead.
3. They confirm. The money moves, both balances update, and the assistant gives reference ZPA-9F4A2B.
4. It offers a next step: a monthly auto-transfer or a savings goal.
"""
)

st.video(str(Path(__file__).resolve().parent.parent / "assets" / "zopa_ai_agent_demo.mp4"))
st.caption("33 seconds, no sound. Balances and the reference number are sample data.")
