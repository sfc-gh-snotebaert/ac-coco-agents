import streamlit as st
from components import render_session_header, render_prompt, render_explanation, render_technologies_used, render_key_concepts, render_what_you_built

render_session_header(3, 'Create the Agent', '10:00 AM – 10:25 AM', '25 min', 'AIRLINE_OPS_AGENT Cortex Agent available in CoWork')

render_technologies_used([{'name': 'Cortex Agents', 'description': 'Orchestrate LLM reasoning with tools such as Cortex Analyst over a semantic view.', 'icon': 'smart_toy'}, {'name': 'Snowflake CoWork', 'description': 'The business-user interface where agents are published and used.', 'icon': 'group'}, {'name': 'Agent instructions', 'description': 'Orchestration and response instructions that shape tone, scope and tool use.', 'icon': 'edit_note'}])

st.info(":material/group: After Prompt 3.1, open **CoWork** from Snowsight, pick **Air Canada Ops Assistant**, and ask one of the sample questions.")

render_prompt('Prompt 3.1', 'Create the agent', 'Create a Cortex Agent called AIRLINE_OPS_AGENT in AIRLINE_OPS.OPS:\n- Display name: "Air Canada Ops Assistant"\n- Tool: Cortex Analyst text-to-SQL using semantic view AIRLINE_OPS.OPS.AIRLINE_OPS_SV, warehouse AIRLINE_WH\n- Orchestration instructions: you help Air Canada network planning and revenue management analysts; always state the period and filters used; prefer charts for trends\n- Response instructions: concise, amounts in CAD, percentages with one decimal\n- 4 sample questions about revenue, on-time performance, load factor and Aeroplan tiers\nExecute and then describe the agent.')

render_prompt('Prompt 3.2', 'Test the agent from Cortex Code', 'Run AIRLINE_OPS.OPS.AIRLINE_OPS_AGENT with: "Compare load factor and on-time performance for YYZ departures this summer vs last summer, and explain the difference." Show the tool calls and the answer.')

render_key_concepts([{'term': 'Orchestration', 'definition': 'The agent plans which tool to call, calls it, reflects on results and may loop before answering.'}])

render_what_you_built(['AIRLINE_OPS_AGENT connected to AIRLINE_OPS_SV', 'Agent tested in Cortex Code and in CoWork'])
