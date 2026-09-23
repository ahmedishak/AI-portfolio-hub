Paste this over `Home.py`:

```python
import streamlit as st

st.set_page_config(page_title="Ishak — apps", layout="wide")

hyphen = st.Page("pages/1_Hyphen_Matcher.py", title="Hyphen Matcher")
lux = st.Page("pages/2_LuxStock_AI.py", title="LuxStock AI")
comm = st.Page("pages/3_Comm_Pilot.py", title="Comm-Pilot")
bot = st.Page("pages/4_Bot.py", title="AI Booking Agent")


def home():
    st.title("Apps")
    st.write(
        "Hyphen and LuxStock open in their own apps. "
        "Comm-Pilot opens a walkthrough here — the real product is a Chrome side panel."
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.subheader("Hyphen Matcher")
        st.write("UK route recommendation (advisory): INTO, iO-Sphere, Foundation, or HOLD.")
        st.link_button("Open Hyphen Matcher", "http://localhost:3000")
        if st.button("Details", key="hyphen_details"):
            st.switch_page(hyphen)

    with c2:
        st.subheader("LuxStock AI")
        st.write("CSV → stockout risk → supplier draft → approve trail.")
        st.link_button("Open LuxStock AI", "http://localhost:3004")
        if st.button("Details", key="lux_details"):
            st.switch_page(lux)

    with c3:
        st.subheader("Comm-Pilot")
        st.write("Gmail follow-up copilot. Chrome extension in real use; demo runs in this hub.")
        if st.button("Open Comm-Pilot", type="primary"):
            st.switch_page(comm)


pg = st.navigation(
    [
        st.Page(home, title="Apps", default=True),
        hyphen,
        lux,
        comm,
        bot,
    ]
)
pg.run()
```

Save it, then run `streamlit run Home.py` again.
