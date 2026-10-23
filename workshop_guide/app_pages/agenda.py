import streamlit as st

st.title("Workshop agenda")

AGENDA = [
    ("{{TIME_ARRIVAL}}", "Arrival & Coffee", None, None),
    ("{{TIME_WELCOME}}", "Welcome & Workshop Overview", None, None),
    ("{{TIME_SESSION_1}}", "Session 1: Data Prep", "{{DUR_SESSION_1}}", "1"),
    ("{{TIME_SESSION_2}}", "Session 2: Cortex Analyst & Semantic Views", "{{DUR_SESSION_2}}", "2"),
    ("{{TIME_SESSION_3}}", "Session 3: Cortex Search", "{{DUR_SESSION_3}}", "3"),
    ("{{TIME_BREAK}}", ":orange-badge[BREAK]", None, None),
    ("{{TIME_SESSION_4}}", "Session 4: Cortex Agents", "{{DUR_SESSION_4}}", "4"),
    ("{{TIME_SESSION_5}}", "Session 5: CoWork", "{{DUR_SESSION_5}}", "5"),
    ("{{TIME_SESSION_6}}", "Session 6: Streamlit", "{{DUR_SESSION_6}}", "6"),
]

for time, title, duration, session_num in AGENDA:
    if session_num:
        col1, col2 = st.columns([1, 4])
        col1.markdown(f"**{time}**")
        col2.markdown(f":material/play_circle: **{title}** :gray-badge[{duration}]")
    elif "BREAK" in title:
        col1, col2 = st.columns([1, 4])
        col1.markdown(f"**{time}**")
        col2.markdown(f"{title}")
    else:
        col1, col2 = st.columns([1, 4])
        col1.markdown(f"**{time}**")
        col2.markdown(f":gray[{title}]")

st.space("medium")

st.markdown("##### What you'll build by end of session")
st.markdown("""
| Object Type | Count | Examples |
|-------------|-------|---------|
| **Tables** | {{NUM_TABLES}} | {{TABLE_EXAMPLES}} |
| **Cortex Search Services** | 1 | {{SEARCH_SERVICE_NAME}} |
| **Semantic Views** | 1 | {{SEMANTIC_VIEW_NAME}} with relationships, metrics, and AI instructions |
| **Cortex Agents** | 1 | {{AGENT_NAME}} with Analyst + Search + custom tools |
| **Streamlit Apps** | 1 | Operations dashboard with AI chat |
""")

st.space("small")

st.markdown("##### Location")
with st.container(border=True):
    st.markdown("""
:material/location_on: **{{VENUE_NAME}}, {{VENUE_CITY}}**

{{EVENT_DATE}} — {{EVENT_TIME_RANGE}}
""")
