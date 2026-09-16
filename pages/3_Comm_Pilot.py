from pathlib import Path

import streamlit as st

st.set_page_config(page_title="Comm-Pilot", layout="wide")
st.title("Comm-Pilot")
st.caption(
    "This page is the demo URL. The shipping product is a Chrome side panel on Gmail — it has no website."
)

st.info(
    "Real app: chrome://extensions → Developer mode → Load unpacked → ~/comm-pilot-extension. "
    "Nothing below sends mail."
)

draft_tab, search_tab, chase_tab, stats_tab = st.tabs(
    ["Draft", "Search", "Chase", "Stats"]
)

with draft_tab:
    st.write("Read the open thread, write what to say, generate a draft. Insert never sends.")
    thread = st.text_area(
        "Open thread (sample)",
        value=(
            "From: Priya at Millwork\n"
            "Re: SS27 jersey tech pack\n\n"
            "Can you send the revised pack this week? Need GSM and colourway lock."
        ),
        height=140,
    )
    notes = st.text_area(
        "What to say",
        value="Confirm we can send Thursday. GSM 180. Colourway: navy / ecru.",
        height=80,
    )
    if st.button("Draft & preview"):
        st.session_state["comm_draft"] = (
            f"Hi Priya,\n\nThanks for chasing the SS27 jersey pack.\n\n"
            f"{notes.strip()}\n\nI'll insert this into Gmail in the real extension — "
            f"this hub only previews.\n\nBest,\nIshak"
        )
    if st.session_state.get("comm_draft"):
        st.text_area("Preview (not sent)", st.session_state["comm_draft"], height=180)
        st.success("In Chrome, Insert puts this in the Gmail compose box.")

with search_tab:
    st.write("Find threads, then answer from a few selected ones — not the whole inbox.")
    st.text_input("Search Gmail", value="tech pack jersey")
    rows = [
        ("Millwork — revised jersey pack", "Priya", "2d"),
        ("Colourway lock SS27", "Priya", "5d"),
        ("GSM confirmation", "Ops", "1w"),
    ]
    picked = []
    for title, who, age in rows:
        if st.checkbox(f"{title} · {who} · {age}", value=title.startswith("Millwork"), key=title):
            picked.append(title)
    if st.button("Answer from selected"):
        if not picked:
            st.warning("Select at least one thread.")
        else:
            st.write(
                f"From {len(picked)} thread(s): Priya is waiting on the revised jersey pack, "
                "GSM, and colourway lock this week."
            )

with chase_tab:
    st.write("Open loops: unanswered asks and promises. Draft Follow-Up fills Draft notes only.")
    st.markdown(
        """
- **Millwork / Priya** — asked for revised tech pack — 2 days · unanswered
- **You → Millwork** — promised GSM Thursday — tracked promise
"""
    )
    if st.button("Draft follow-up into notes"):
        st.session_state["comm_draft"] = (
            "Hi Priya,\n\nQuick follow-up on the SS27 jersey revised pack, GSM, and colourway lock.\n\nBest,\nIshak"
        )
        st.success("Notes filled. Open the Draft tab to preview.")

with stats_tab:
    st.write("Last 90 days, metadata only. Average reply days per company.")
    st.dataframe(
        {
            "Company": ["Millwork", "Northweave", "Harbour Knit"],
            "Avg reply days": [1.4, 3.2, 0.8],
            "Threads (cap 100)": [12, 5, 8],
        },
        hide_index=True,
        use_container_width=True,
    )

assets = Path(__file__).resolve().parent.parent / "assets"
shots = [
    ("comm-draft.png", "Draft"),
    ("comm-search.png", "Search"),
    ("comm-chase.png", "Chase"),
    ("comm-stats.png", "Stats"),
]
existing = [(p, cap) for name, cap in shots if (p := assets / name).exists()]
if existing:
    st.subheader("Chrome side panel")
    cols = st.columns(len(existing))
    for col, (path, cap) in zip(cols, existing):
        col.image(str(path), caption=cap)
