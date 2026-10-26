import streamlit as st

st.title("Workshop agenda")
st.caption("November 12, 2026, Air Canada Office")

AGENDA = [
    ("9:00 AM", "Welcome & overview", None),
    ("9:10 AM", "Session 1: Review the data model", "25 min"),
    ("9:35 AM", "Session 2: Create the semantic view", "25 min"),
    ("10:00 AM", "Session 3: Create the agent", "25 min"),
    ("10:25 AM", ":orange-badge[BREAK]", None),
    ("10:35 AM", "Session 4: Secure the agent", "25 min"),
    ("11:00 AM", "Session 5: Evaluate the agent", "25 min"),
    ("11:25 AM", "Session 6: Forecast skill", "20 min"),
    ("11:45 AM", "Session 7: CoWork dashboard", "20 min"),
    ("12:05 PM", "Wrap-up & Q&A", None),
]
for time, title, dur in AGENDA:
    c1, c2 = st.columns([1, 4])
    c1.markdown(f"**{time}**")
    c2.markdown(f":material/play_circle: **{title}** :gray-badge[{dur}]" if dur else (title if "BREAK" in title else f":gray[{title}]"))

st.space("medium")
st.markdown("##### What you'll build")
st.markdown("""
| Object | Name |
|---|---|
| Database / schema / warehouse | AIRLINE_OPS.OPS / AIRLINE_WH |
| Tables | FACT_BOOKING, DIM_FLIGHT, DIM_PASSENGER, DIM_AIRPORT |
| Semantic view | AIRLINE_OPS_SV |
| Cortex Agent | AIRLINE_OPS_AGENT (Air Canada Ops Assistant) |
| Security | AIRLINE_ANALYST role, PII masking, RSS, AIRLINE_AGENT_SVC identity |
| Evaluation | AGENT_EVAL_DATASET + evaluation runs |
| ML | FLIGHT_VOLUME_FORECAST + FORECAST_FLIGHT_VOLUME tool |
| CoWork | Network Performance 2026 dashboard |
""")
