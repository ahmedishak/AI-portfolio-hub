import streamlit as st

st.set_page_config(page_title="Ishak Ahmed", layout="wide")

hyphen = st.Page("pages/1_Hyphen_Matcher.py", title="Hyphen Matcher")
lux = st.Page("pages/2_LuxStock_AI.py", title="LuxStock AI")
comm = st.Page("pages/3_Comm_Pilot.py", title="Comm-Pilot")
bot = st.Page("pages/4_Bot.py", title="AI Booking Agent")


def home():
    st.title("Ishak Ahmed")
    st.write("I build AI tools that take a manual task from request to a finished result.")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.subheader("Hyphen Matcher")
        st.write("Paste a candidate background. Get an advisory UK route: INTO, iO-Sphere, Foundation, or HOLD.")
        st.link_button("Open Hyphen Matcher", "https://hyphen-matcher-app-v2.vercel.app/")
        if st.button("Details", key="hyphen_details"):
            st.switch_page(hyphen)

    with c2:
        st.subheader("LuxStock AI")
        st.write("Upload a week of sales. See which SKUs are at risk, then draft the supplier email.")
        st.link_button("Open LuxStock AI", "https://lux-stock-ai.vercel.app/")
        if st.button("Details", key="lux_details"):
            st.switch_page(lux)

    with c3:
        st.subheader("Comm-Pilot")
        st.write("A Gmail follow-up copilot. The live product is a Chrome side panel. This page is the walkthrough.")
        if st.button("Open Comm-Pilot", type="primary"):
            st.switch_page(comm)

    with c4:
        st.subheader("AI Booking Agent")
        st.write("Book an interpreter in chat. Copilot Studio saves the request and alerts the team.")
        if st.button("Open AI Booking Agent", key="bot_open"):
            st.switch_page(bot)


pg = st.navigation(
    [
        st.Page(home, title="Home", default=True),
        hyphen,
        lux,
        comm,
        bot,
    ]
)
pg.run()
