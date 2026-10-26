from pathlib import Path

import streamlit as st

from components import is_session_complete

_DIR = Path(__file__).parent


def _title(session_num: int, label: str) -> str:
    check = " :green[:material/check_circle:]" if is_session_complete(session_num) else ""
    return f"{session_num}. {label}{check}"


st.set_page_config(
    page_title="Create Agents using CoCo — Air Canada",
    page_icon=":material/flight:",
    layout="wide",
)

st.logo(
    str(_DIR / "static" / "snowflake_full_logo.png"),
    icon_image=str(_DIR / "static" / "snowflake_logo.png"),
)

page = st.navigation(
    {
        "": [
            st.Page("app_pages/home.py", title="Home", icon=":material/home:"),
            st.Page("app_pages/getting_started.py", title="Getting Started", icon=":material/rocket_launch:"),
            st.Page("app_pages/agenda.py", title="Agenda", icon=":material/calendar_today:"),
        ],
        "Block 1: Data & Semantics": [
            st.Page("app_pages/session_01.py", title=_title(1, "Review Data Model"), icon=":material/database:"),
            st.Page("app_pages/session_02.py", title=_title(2, "Semantic View"), icon=":material/description:"),
        ],
        "Block 2: Build & Govern Agents": [
            st.Page("app_pages/session_03.py", title=_title(3, "Create Agent"), icon=":material/smart_toy:"),
            st.Page("app_pages/session_04.py", title=_title(4, "Secure Agent"), icon=":material/lock:"),
            st.Page("app_pages/session_05.py", title=_title(5, "Evaluate Agent"), icon=":material/fact_check:"),
        ],
        "Block 3: Extend & Share": [
            st.Page("app_pages/session_06.py", title=_title(6, "Forecast Skill"), icon=":material/trending_up:"),
            st.Page("app_pages/session_07.py", title=_title(7, "CoWork Dashboard"), icon=":material/dashboard:"),
        ],
    },
    position="sidebar",
)

page.run()
