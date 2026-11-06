import streamlit as st
from components import render_session_header, render_prompt, render_explanation, render_technologies_used, render_key_concepts, render_what_you_built

render_session_header(7, 'CoWork Dashboard', '11:45 AM – 12:05 PM', '20 min', 'A CoWork dashboard built from queries on the semantic view')

render_technologies_used([{'name': 'CoWork dashboards', 'description': 'Dashboards in CoWork built from agent answers and semantic view queries, and shareable with business users.', 'icon': 'dashboard'}, {'name': 'Semantic SQL', 'description': 'SELECT ... FROM SEMANTIC_VIEW(...) queries metrics and dimensions consistently.', 'icon': 'code'}, {'name': 'Sharing', 'description': 'Publish to colleagues who have the right role.', 'icon': 'share'}])

st.warning(":material/science: CoWork dashboards are in limited access. The workshop account must have the feature enabled.")

render_prompt('Prompt 7.1', 'Build the dashboard in CoWork', "Create a dashboard called 'Network Performance 2026' with KPI tiles for revenue, bookings, OTP and load factor (YoY), a line chart of monthly revenue 2025 vs 2026, a bar chart of the top 10 routes, a heatmap of OTP by hub and month, and a table of revenue by cabin and Aeroplan tier. Then add a forecast panel for YYZ flights over the next 30 days.")

render_key_concepts([{'term': 'One definition, many surfaces', 'definition': 'The same metric definitions power Cortex Analyst, the agent and the dashboard, so the numbers match everywhere.'}])

render_what_you_built(['Network Performance 2026 CoWork dashboard', 'Dashboard shared with AIRLINE_ANALYST'])
