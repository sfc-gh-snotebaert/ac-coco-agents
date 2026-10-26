# Create Agents using CoCo — Air Canada HOL

Hands-on lab guide (Streamlit) for November 12, 2026, Air Canada Office, using Snowsight Cortex Code. 3 hours.

| # | Session | Builds |
|---|---|---|
| 1 | Review data model | AIRLINE_OPS.OPS: FACT_BOOKING, DIM_FLIGHT, DIM_PASSENGER, DIM_AIRPORT |
| 2 | Semantic view | AIRLINE_OPS_SV |
| 3 | Create agent | AIRLINE_OPS_AGENT, used in CoWork |
| 4 | Secure agent | Least-privilege role, masking, Restricted Session Scope, agent identity |
| 5 | Agent evaluation | AGENT_EVAL_DATASET + evaluation runs |
| 6 | Forecast skill | FLIGHT_VOLUME_FORECAST + FORECAST_FLIGHT_VOLUME tool |
| 7 | CoWork dashboard | Dashboard on semantic-view queries |

Data: synthetic, Jan 2025 to Oct 2026 (`workshop_guide/data/`, regenerate with `generate_data.py`).

Run locally: `cd workshop_guide && pip install -r requirements.txt && streamlit run streamlit_app.py`
Deploy: share.streamlit.io, main file `workshop_guide/streamlit_app.py`.
