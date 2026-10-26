import streamlit as st
from components import render_session_header, render_prompt, render_explanation, render_technologies_used, render_key_concepts, render_what_you_built

render_session_header(4, 'Secure the Agent', '10:35 AM – 11:00 AM', '25 min', 'Least-privilege access with a dedicated role, Restricted Session Scope and agent identity')

render_technologies_used([{'name': 'RBAC', 'description': 'Grant USAGE on the agent and SELECT on the semantic view and tables only to the roles that need them.', 'icon': 'admin_panel_settings'}, {'name': 'Restricted Session Scope (RSS)', 'description': 'Limits which roles and privileges a Cortex Code / agent session may use, e.g. read-only SQL.', 'icon': 'lock'}, {'name': 'Agent identity', 'description': "Run the agent's tools under a dedicated service identity rather than the caller's full privileges.", 'icon': 'badge'}])

render_prompt('Prompt 4.1', 'Least-privilege role', 'Create a role AIRLINE_ANALYST with only: USAGE on AIRLINE_WH, database AIRLINE_OPS and schema OPS, SELECT on the 4 tables, SELECT/REFERENCES on semantic view AIRLINE_OPS_SV, and USAGE on agent AIRLINE_OPS_AGENT. Grant it to my user. Then add a masking policy on DIM_PASSENGER.EMAIL and DATE_OF_BIRTH that shows values only to ACCOUNTADMIN, and verify as AIRLINE_ANALYST that the agent returns masked values.')

render_prompt('Prompt 4.2', 'Restricted Session Scope', '/guardrails Create a Restricted Session Scope for this Cortex Code session that blocks ACCOUNTADMIN and SECURITYADMIN and allows read-only SQL on AIRLINE_OPS only. Apply it, then try to DROP TABLE AIRLINE_OPS.OPS.DIM_AIRPORT and show that it is blocked. Finally explain how to remove the scope.')
render_explanation("What this prompt does", "RSS limits what the AI may do on your behalf, even if your own role could do more. It's the guardrail for letting an agent act inside production accounts.")

render_prompt('Prompt 4.3', 'Agent identity', "Configure AIRLINE_OPS_AGENT so its tools run under a dedicated service identity: create a SERVICE user/role AIRLINE_AGENT_SVC with the AIRLINE_ANALYST grants, attach it as the agent's execution identity, and show the agent's configuration. Explain the difference between caller's-rights and agent-identity execution, and when to use each.")

render_key_concepts([{'term': 'Least privilege', 'definition': 'An agent can only do what its role allows: securing data is securing the agent.'}, {'term': 'Caller vs agent identity', 'definition': 'Caller identity = row-level security follows the user; agent identity = consistent, auditable service-level access.'}])

render_what_you_built(['AIRLINE_ANALYST role and PII masking', 'Restricted Session Scope applied and tested', 'Agent running under a service identity'])
