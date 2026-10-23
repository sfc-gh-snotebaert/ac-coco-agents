import streamlit as st
from components import render_session_header, render_prompt, render_explanation, render_technologies_used, render_key_concepts, render_what_you_built

render_session_header(2, "Cortex Analyst & Semantic Views", "{{TIME_SESSION_2}}", "{{DUR_SESSION_2}}", "Semantic view with relationships, metrics, and natural language queries")

render_technologies_used([
    {"name": "Cortex Analyst", "description": "Snowflake's text-to-SQL engine that converts natural language questions into SQL queries using a semantic view to understand your data's business meaning.", "icon": "chat"},
    {"name": "Semantic View", "description": "A first-class Snowflake object (CREATE SEMANTIC VIEW) that describes your data in business terms: tables, relationships, facts, dimensions, metrics, and synonyms.", "icon": "description"},
    {"name": "AI_SQL_GENERATION", "description": "Custom instructions embedded in the semantic view that guide how Cortex Analyst generates SQL — providing domain context and disambiguation hints.", "icon": "auto_fix_high"},
])


PROMPT_2_1 = """/semantic_studio In {{DATABASE_NAME}}.{{SCHEMA_NAME}}, create a semantic view called {{SEMANTIC_VIEW_NAME}} for use with Cortex Analyst. It should cover these tables: {{SEMANTIC_VIEW_TABLES}}.

Include:
- Relationships between the tables following these rules:
  - Do NOT specify join_type — omit it entirely (the proto enum doesn't accept string values like many_to_one)
  - Convention: left_table = fact/many side, right_table = dimension/one side (put the table with many rows as left_table)
  - Define primary_key.columns on dimension tables ({{DIMENSION_TABLES}}) so the engine knows the "one" side
  - Use this template for each relationship:
    relationships:
      - name: <descriptive_name>
        left_table: <FACT_TABLE>
        right_table: <DIMENSION_TABLE>
        relationship_columns:
          - left_column: <FK_COLUMN>
            right_column: <PK_COLUMN>
  - Relationships needed: {{RELATIONSHIPS_LIST}}
- Facts for key numeric columns: {{FACTS_LIST}}
- Dimensions for categorical columns: {{DIMENSIONS_LIST}}
- Add useful SYNONYMS ({{SYNONYMS_EXAMPLES}})
- Metrics: {{METRICS_LIST}}
- An AI_SQL_GENERATION instruction with domain context: {{AI_INSTRUCTIONS_CONTEXT}}

Execute the SQL and confirm with DESCRIBE SEMANTIC VIEW."""

render_prompt("Prompt 2.1", "Create the Semantic View", PROMPT_2_1)

render_explanation("What this prompt does", """
Creates a **semantic view** — a first-class Snowflake object that enables natural language to SQL.

{{DOMAIN_CONCEPTS_EXPLANATION}}
""")


PROMPT_2_2 = """Ask Cortex Analyst these questions using {{DATABASE_NAME}}.{{SCHEMA_NAME}}.{{SEMANTIC_VIEW_NAME}}:

{{ANALYST_TEST_QUESTIONS}}

Show the generated SQL and results for each."""

render_prompt("Prompt 2.2", "Test with Natural Language Queries", PROMPT_2_2)

st.info("""
:material/lightbulb: **You can also test these in the Cortex Analyst UI!**

In Snowsight, navigate to **AI & ML → Cortex Analyst** in the left sidebar. Select your `{{SEMANTIC_VIEW_NAME}}` semantic view, and you'll see a playground where you can type natural language questions interactively.
""")

render_explanation("What this prompt does", """
Tests Cortex Analyst across different question types to validate the semantic view definitions.

{{ANALYST_TEST_EXPLANATION}}
""")


PROMPT_2_3 = """Now expand our {{SEMANTIC_VIEW_NAME}} in {{DATABASE_NAME}}.{{SCHEMA_NAME}}:

{{SEMANTIC_VIEW_EXPANSION_INSTRUCTIONS}}

Execute all SQL."""

render_prompt("Prompt 2.3", "Expand the Semantic View", PROMPT_2_3)

render_explanation("What this prompt does", """
Demonstrates iterative semantic view development — adding calculated metrics.

{{EXPANSION_EXPLANATION}}
""")


render_key_concepts([
    {"term": "Cortex Analyst", "definition": "Snowflake's text-to-SQL engine. Converts natural language to SQL using a semantic view for context."},
    {"term": "Semantic View", "definition": "A first-class Snowflake object mapping tables to business concepts. Contains relationships, facts, dimensions, metrics, synonyms, and AI instructions."},
    {"term": "AI_SQL_GENERATION", "definition": "Custom instructions guiding SQL generation. Essential for domain-specific terminology."},
])

render_what_you_built([
    "{{SEMANTIC_VIEW_NAME}} semantic view with domain-specific metrics",
    "Natural language queries validated against the view",
    "Expanded view with calculated metrics",
])
