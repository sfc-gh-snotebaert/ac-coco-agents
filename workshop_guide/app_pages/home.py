import streamlit as st

st.title("Create Agents using CoCo")
st.markdown("Air Canada hands-on lab: build, secure, evaluate and share Cortex Agents with Cortex Code in Snowsight")
st.space("small")
c1, c2, c3 = st.columns(3)
c1.metric("Sessions", "7")
c2.metric("Prompts", "19")
c3.metric("Duration", "3 hrs")
st.space("medium")
st.markdown("#### How this workshop works")
st.markdown("""
Each session has **numbered prompts**. Copy each prompt into **Cortex Code** in Snowsight (or into **CoWork** where noted) and run them in order, because every session builds on the one before.
""")
st.markdown("#### The scenario")
with st.container(border=True):
    st.markdown("""
Air Canada's network planning and revenue management teams want one assistant that answers questions about **bookings, revenue, on-time performance, load factor and Aeroplan members**, forecasts **flight volume**, and powers a shared **CoWork dashboard**, all governed with least privilege.

| Table | Grain | Rows |
|---|---|---|
| **FACT_BOOKING** | One booking (PNR) on one flight | 56,329 |
| **DIM_FLIGHT** | One flight leg on one date (Jan 2025 to Oct 2026) | 10,355 |
| **DIM_PASSENGER** | One passenger / Aeroplan member | 3,000 |
| **DIM_AIRPORT** | One airport (4 hubs + domestic, US, international) | 20 |

:material/info: The data is synthetic and generated for this workshop.
""")
st.markdown("#### What we're building")
with st.container(border=True):
    st.markdown("""
1. **Review the data model**: load and document the AIRLINE_OPS star schema
2. **Semantic view**: business metrics (revenue, OTP, load factor) for Cortex Analyst
3. **Cortex Agent**: Air Canada Ops Assistant, available in CoWork
4. **Secure the agent**: least-privilege role, PII masking, Restricted Session Scope, agent identity
5. **Evaluate the agent**: ground-truth dataset, scored runs, improvement loop
6. **Forecast skill**: an ML forecast of flight volume exposed as an agent tool
7. **CoWork dashboard**: network performance dashboard built on the semantic view
""")
st.markdown("#### Prerequisites")
with st.container(border=True):
    st.markdown("""
- A Snowflake account with **ACCOUNTADMIN** (see **Getting Started**)
- **Cortex Code** open in Snowsight
- Cross-region inference enabled
""")
st.space("medium")
st.caption("Built for the November 12, 2026 workshop  :material/location_on:  Air Canada Office")
