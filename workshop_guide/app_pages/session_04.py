import streamlit as st
from components import render_session_header, render_prompt, render_explanation, render_technologies_used, render_key_concepts, render_what_you_built

render_session_header(4, "Cortex Agents", "{{TIME_SESSION_4}}", "{{DUR_SESSION_4}}", "Cortex Agent with Analyst + Search + custom tools")

render_technologies_used([
    {"name": "Cortex Agent (CREATE AGENT)", "description": "An orchestrating AI that plans tasks, selects tools, executes them, reflects on results, and generates responses.", "icon": "smart_toy"},
    {"name": "Tool Orchestration", "description": "The Agent automatically routes questions to the right tool: Cortex Analyst for structured data, Cortex Search for documents, custom UDFs for logic.", "icon": "route"},
    {"name": "Custom Tools (UDFs)", "description": "User-defined functions that extend Agent capabilities with custom business logic.", "icon": "build"},
])


PROMPT_4_1 = """In {{DATABASE_NAME}}.{{SCHEMA_NAME}}, create a Cortex Agent called {{AGENT_NAME}}.

It should:
- Use auto as the orchestration model
- Have two tools: the {{SEMANTIC_VIEW_NAME}} semantic view (for structured data queries) and the {{SEARCH_SERVICE_NAME}} Cortex Search service (for unstructured document search)
- Include instructions defining it as the {{AGENT_ROLE_DESCRIPTION}}, guiding it to use structured data for {{STRUCTURED_QUESTION_TYPES}} and search for {{UNSTRUCTURED_QUESTION_TYPES}}
- Mention domain context: {{AGENT_DOMAIN_CONTEXT}}
- Include 3-4 sample questions spanning both tools

Execute and show confirmation."""

render_prompt("Prompt 4.1", "Create the Cortex Agent", PROMPT_4_1)

render_explanation("What this prompt does", """
Creates a **Cortex Agent** combining structured analytics with document search:

- **Structured questions** → routed to Cortex Analyst via the semantic view
- **Unstructured questions** → routed to Cortex Search
- **Mixed questions** → Agent uses both tools and synthesizes
""")


PROMPT_4_2 = """Test our {{AGENT_NAME}} with these queries:

{{AGENT_TEST_QUERIES}}

Show the responses and note which tools the agent selected."""

render_prompt("Prompt 4.2", "Test the Agent", PROMPT_4_2)

render_explanation("What this prompt does", """
Tests the agent with structured, unstructured, and mixed queries to validate tool routing.
""")


PROMPT_4_3 = """In {{DATABASE_NAME}}.{{SCHEMA_NAME}}, add a custom tool to the agent:

1. Create a UDF:

{{CUSTOM_UDF_SQL}}

2. Recreate {{AGENT_NAME}} with {{CUSTOM_UDF_NAME}} as an additional tool.

3. Test with: "{{CUSTOM_TOOL_TEST_QUESTION}}"

Execute all SQL."""

render_prompt("Prompt 4.3", "Agent with Custom Tool", PROMPT_4_3)

render_explanation("What this prompt does", """
Adds a **custom UDF tool** for domain-specific calculations. The Agent can now query data, search documents, AND run custom business logic.
""")


render_key_concepts([
    {"term": "Cortex Agent", "definition": "A Snowflake object that orchestrates LLMs, Analyst, Search, and custom tools to answer complex questions."},
    {"term": "Tool Routing", "definition": "The Agent selects the right tool for each question based on the question type and tool descriptions."},
    {"term": "Custom Tools", "definition": "SQL UDFs registered as Agent tools. Enable domain-specific calculations and business logic."},
])

render_what_you_built([
    "{{AGENT_NAME}} — Cortex Agent with Analyst + Search tools",
    "Tested structured, unstructured, and mixed queries",
    "{{CUSTOM_UDF_NAME}} as a custom tool",
    "Enhanced agent with three tool types",
])
