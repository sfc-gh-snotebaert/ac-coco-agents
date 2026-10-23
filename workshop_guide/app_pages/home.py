import streamlit as st

st.title("{{WORKSHOP_TITLE}}")
st.markdown("{{WORKSHOP_SUBTITLE}}")

st.space("small")

col1, col2, col3 = st.columns(3)
col1.metric("Sections", "6", help="Hands-on lab sections")
col2.metric("Prompts", "16", help="Total prompts across all tools")
col3.metric("Duration", "{{DURATION}}", help="Total workshop time")

st.space("medium")

st.markdown("#### How this workshop works")

st.markdown("""
Each section has **numbered prompts** that you copy and paste into the appropriate tool:

- **Cortex Code** — for building infrastructure, creating objects, and writing SQL/Python
- **Cortex Analyst** — for testing natural language queries against your semantic view
- **Snowflake CoWork** — for collaborative data exploration and analysis

All prompts build on each other sequentially — run them in order throughout the morning.
""")

st.space("small")

st.markdown("#### The scenario")
with st.container(border=True):
    st.markdown("""
{{SCENARIO_DESCRIPTION}}

We'll build a complete AI platform covering:

| Data type | Examples |
|-----------|---------|
| **Structured** | {{STRUCTURED_DATA_EXAMPLES}} |
| **Unstructured** | {{UNSTRUCTURED_DATA_EXAMPLES}} |
| **Time series** | {{TIMESERIES_DATA_EXAMPLES}} |
""")

st.space("small")

st.markdown("#### What we're building")

with st.container(border=True):
    st.markdown("""
In {{DURATION}}, we build a complete AI-powered operations platform:

**1. Data Foundation** — Load structured and unstructured operations data into Snowflake from pre-generated CSV files.

**2. Natural Language Analytics** — Create a Semantic View over operational tables and query them with plain English via Cortex Analyst.

**3. Intelligent Search** — Build a Cortex Search service over safety documents and inspection reports for hybrid semantic + keyword search.

**4. AI Agents** — Create a Cortex Agent that orchestrates structured data queries AND document search through a single conversational interface.

**5. Collaborative AI** — Use CoWork to collaboratively analyze data with AI assistance.

**6. Operations Dashboard** — Deploy a Streamlit app with live KPIs, charts, and an AI chat interface.
""")

st.space("small")

st.markdown("#### Prerequisites")
with st.container(border=True):
    st.markdown("""
- Snowflake account with **ACCOUNTADMIN** role — see **Getting Started** in the sidebar to provision a free trial
- **Cortex Code** open in Snowsight and connected to your account
- Cross-region inference enabled (for Cortex LLM functions)
""")

st.space("medium")
st.caption("Built for the {{EVENT_DATE}} workshop  :material/location_on:  {{VENUE_NAME}}, {{VENUE_CITY}}")
