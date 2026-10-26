import streamlit as st
from components import render_session_header, render_prompt, render_explanation, render_technologies_used, render_key_concepts, render_what_you_built

render_session_header(1, 'Review the Data Model', '9:10 AM – 9:35 AM', '25 min', 'AIRLINE_OPS star schema: 1 fact table, 3 dimensions')

render_technologies_used([{'name': 'Cortex Code', 'description': "Snowflake's AI coding agent in Snowsight. You describe the outcome; it writes and runs the SQL.", 'icon': 'terminal'}, {'name': 'Star Schema', 'description': 'A central fact table (bookings) joined to dimension tables (flights, passengers, airports).', 'icon': 'schema'}, {'name': 'INFER_SCHEMA', 'description': 'Detects column names and types directly from staged CSV files.', 'icon': 'table_chart'}])

st.markdown("""
**Before Prompt 1.2:** download [airline_ops_data.zip](https://github.com/sfc-gh-snotebaert/ac-coco-agents/raw/main/workshop_guide/data/airline_ops_data.zip), unzip it, then in Snowsight browse to the `AIRLINE_OPS.OPS.DATA` stage (Catalog → Database Explorer) and upload the 4 CSV files.
""")

render_prompt('Prompt 1.1', 'Create database, schema, stage & warehouse', 'Create the Snowflake objects for our Air Canada airline operations workshop:\n0. First check whether a database called AIRLINE_OPS already exists. If it does, STOP and tell me who owns it. Do not modify, replace or write into an existing AIRLINE_OPS database.\n1. A database called AIRLINE_OPS\n2. A schema called OPS in that database\n3. An internal stage called DATA in AIRLINE_OPS.OPS with a directory table and server-side encryption\n4. A warehouse called AIRLINE_WH (size SMALL, auto-suspend 60 seconds, auto-resume)\n5. Set the session context to use these objects\nExecute all SQL and confirm each object was created.')

render_prompt('Prompt 1.2', 'Load the 4 tables from CSV', 'In AIRLINE_OPS.OPS, the CSV files DIM_AIRPORT.csv, DIM_FLIGHT.csv, DIM_PASSENGER.csv and FACT_BOOKING.csv are in the stage @DATA.\n1. Create a CSV file format with PARSE_HEADER=TRUE and FIELD_OPTIONALLY_ENCLOSED_BY=\'"\'\n2. Create the tables DIM_AIRPORT, DIM_FLIGHT, DIM_PASSENGER and FACT_BOOKING using INFER_SCHEMA, with uppercase column names\n3. Load them with COPY INTO (MATCH_BY_COLUMN_NAME=CASE_INSENSITIVE)\nExecute all SQL and show the row count of each table.')
render_explanation("What this prompt does", 'Expected row counts: **DIM_AIRPORT 20, DIM_FLIGHT 10,355, DIM_PASSENGER 3,000, FACT_BOOKING 56,329**. Flights run from Jan 1, 2025 to Oct 31, 2026, which gives you a full previous year plus the current year for year-over-year analysis.')

render_prompt('Prompt 1.3', 'Review and document the data model', 'Review the data model in AIRLINE_OPS.OPS:\n1. Describe each table, its grain and its likely primary key\n2. Identify the foreign key relationships (FACT_BOOKING.FLIGHT_ID -> DIM_FLIGHT, FACT_BOOKING.PASSENGER_ID -> DIM_PASSENGER, DIM_FLIGHT.ORIGIN_AIRPORT_CODE and DESTINATION_AIRPORT_CODE -> DIM_AIRPORT) and validate them with orphan-row checks\n3. Add PRIMARY KEY and FOREIGN KEY constraints (informational) plus table and column COMMENTs that describe each column in airline business terms\n4. Profile the data: date range of flights, flights per year, bookings per year, revenue per year\nSummarize the model as a Mermaid ER diagram.')
render_explanation("What this prompt does", 'Constraints and comments are not just documentation: the semantic view generator and Cortex Analyst read them, so good descriptions here directly improve answer quality later.')

render_key_concepts([{'term': 'Grain', 'definition': 'What one row represents. FACT_BOOKING = one booking; DIM_FLIGHT = one flight leg on one date.'}, {'term': 'Informational constraints', 'definition': "Snowflake doesn't enforce PK/FK (except NOT NULL), but tools use them to infer joins."}])

render_what_you_built(['AIRLINE_OPS.OPS schema, DATA stage and AIRLINE_WH warehouse', '4 tables, about 70K rows loaded', 'Documented keys, relationships and column comments'])
