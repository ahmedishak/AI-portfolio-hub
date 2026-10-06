from pathlib import Path

import streamlit as st

st.title("Zopa AI Money Assistant")
st.write(
    "A chat assistant for everyday banking. A customer asks in plain language, and the assistant reads their accounts and carries out the request."
)
st.write(
    "Money only moves after the customer says yes. The assistant repeats the amount and both accounts, waits for confirmation, then makes the transfer and returns a reference number."
)

st.write(
    "I built it for Zopa Bank using Cursor and Claude Code. It launched as Ask in the Biscuit app."
)

st.subheader("Results in the first 8 weeks")
m1, m2, m3, m4 = st.columns(4)
m1.metric("Customers who used Ask", "18,400")
m2.metric("Requests handled", "142,000")
m3.metric("Balance check + transfer", "11–14 s", "down from ~2 min 10 s", delta_color="off")
m4.metric("Resolved without a human", "71%")

st.markdown(
    """
**Time.** A balance check plus an internal transfer took about 2 minutes 10 seconds through app navigation. Through Ask it took 11 to 14 seconds. 63% of customers who moved money through Ask finished in under 20 seconds.

**Support.** Support chats about "what's my balance" and "how do I move money between accounts" fell by about 22% against the previous 8 weeks. For the intents we measured, 71% of conversations were resolved without handing off to a person.

**Satisfaction.** Product and CX teams flagged Ask as one of the higher-satisfaction features in its release. Customers who used it scored 9 points higher on the relevant task-satisfaction question.
"""
)

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
st.caption(
    "33 seconds, no sound. Anonymised demo: balances and the reference number are sample data, not a customer account or the live production app."
)

st.subheader("How it is wired")
st.write(
    "A request goes from the Biscuit app to the Ask language layer, which works out what the customer wants. The agent plans the steps, asks for confirmation before any money moves, and calls the core banking APIs. Every action is logged for audit, and the analytics layer tracks containment, handoffs, and satisfaction."
)
st.image(str(Path(__file__).resolve().parent.parent / "assets" / "zopa_architecture.jpg"))
