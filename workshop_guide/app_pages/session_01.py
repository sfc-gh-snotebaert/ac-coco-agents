import streamlit as st
from components import render_session_header, render_prompt, render_explanation, render_technologies_used, render_key_concepts, render_what_you_built

render_session_header(1, "Data Prep", "{{TIME_SESSION_1}}", "{{DUR_SESSION_1}}", "Database, schema, warehouse, and {{NUM_TABLES}} operational tables loaded from CSV")

render_technologies_used([
    {"name": "Database & Schema", "description": "Snowflake's organizational hierarchy for objects. A database contains schemas, and schemas contain tables, views, and other objects.", "icon": "database"},
    {"name": "CSV File Format", "description": "Snowflake can infer schema and load data directly from CSV files using file formats and COPY INTO commands.", "icon": "table_chart"},
    {"name": "Virtual Warehouse", "description": "Snowflake's compute engine. A warehouse provides the CPU and memory to execute queries and load data.", "icon": "memory"},
])


PROMPT_1_1 = """Create the following Snowflake objects for our {{SCENARIO_SHORT_NAME}} AI workshop:

1. A database called {{DATABASE_NAME}}
2. A schema called {{SCHEMA_NAME}} inside that database
3. A stage called DATA in the schema {{SCHEMA_NAME}} with a directory table and server side encryption
3. A warehouse called {{WAREHOUSE_NAME}} (size MEDIUM, auto-suspend after 60 seconds, auto-resume enabled)
4. Set the session context to use these objects

Execute all SQL and confirm each object was created."""

render_prompt("Prompt 1.1", "Create Database, Schema & Warehouse", PROMPT_1_1)

render_explanation("What this prompt does", """
Creates the foundational Snowflake objects:

```sql
CREATE DATABASE {{DATABASE_NAME}};
CREATE SCHEMA {{DATABASE_NAME}}.{{SCHEMA_NAME}};
CREATE WAREHOUSE {{WAREHOUSE_NAME}}
  WAREHOUSE_SIZE = 'MEDIUM'
  AUTO_SUSPEND = 60
  AUTO_RESUME = TRUE;

USE DATABASE {{DATABASE_NAME}};
USE SCHEMA {{SCHEMA_NAME}};
USE WAREHOUSE {{WAREHOUSE_NAME}};
```
""")


PROMPT_1_2 = """In {{DATABASE_NAME}}.{{SCHEMA_NAME}}, the {{NUM_TABLES}} CSV files have been uploaded to an internal stage called DATA.

For all {{NUM_TABLES}} tables ({{TABLE_LIST_UPPERCASE}}):

1. Create a file format (CSV with PARSE_HEADER=TRUE, FIELD_OPTIONALLY_ENCLOSED_BY='"')
2. Create the tables with appropriate column types inferred from the data. Ensure to convert the column names to uppercase.
3. Load the data

Use CREATE TABLE with INFER_SCHEMA from a stage and then COPY INTO them. The key requirement is that all {{NUM_TABLES}} tables are created and populated.

Execute all SQL."""

st.markdown("""
**Before running the prompt below, download the CSV files and upload them to the `DATA` stage:**

1. Download the zip file containing all CSVs: [{{ZIP_FILENAME}}]({{ZIP_DOWNLOAD_URL}})
2. Unzip the file on your computer to get the individual CSV files.
3. Using Snowsight, use the Horizon Catalog to browse to the `{{DATABASE_NAME}}.{{SCHEMA_NAME}}.DATA` stage and upload all CSV files.
4. Then copy the prompt below into Cortex Code and execute.
""")

render_prompt("Prompt 1.2", "Load and Create Tables from CSV", PROMPT_1_2)

render_explanation("What this prompt does", """
Loads all operational data tables from CSV files uploaded to the internal stage `DATA`:

```sql
CREATE OR REPLACE FILE FORMAT csv_format
  TYPE = CSV
  PARSE_HEADER = TRUE
  FIELD_OPTIONALLY_ENCLOSED_BY = '"';

CREATE OR REPLACE TABLE {{EXAMPLE_TABLE}}
  USING TEMPLATE (
    SELECT ARRAY_AGG(OBJECT_CONSTRUCT(*))
    FROM TABLE(INFER_SCHEMA(
      LOCATION => '@{{DATABASE_NAME}}.{{SCHEMA_NAME}}.DATA/{{EXAMPLE_TABLE_FILE}}',
      FILE_FORMAT => 'csv_format'
    ))
  );

COPY INTO {{EXAMPLE_TABLE}}
  FROM @{{DATABASE_NAME}}.{{SCHEMA_NAME}}.DATA/{{EXAMPLE_TABLE_FILE}}
  FILE_FORMAT = csv_format;
```

**The tables**:
{{TABLE_DESCRIPTIONS_MARKDOWN}}
""")


PROMPT_1_3 = """Run a query in {{DATABASE_NAME}}.{{SCHEMA_NAME}} that shows every table name and its row count, ordered by row count descending. Format it nicely."""

render_prompt("Prompt 1.3", "Verify All Data Tables", PROMPT_1_3)

render_explanation("What this prompt does", """
A quick verification query. You should see approximately **{{TOTAL_ROWS}} total rows** across {{NUM_TABLES}} tables.
""")


render_key_concepts([
    {"term": "Internal Stage", "definition": "A named Snowflake stage that stores files within Snowflake's managed storage. Files are uploaded via Snowsight UI or PUT command."},
    {"term": "INFER_SCHEMA", "definition": "A Snowflake table function that automatically detects column names and types from files in a stage."},
    {"term": "File Format", "definition": "A named object specifying how to parse files (CSV delimiters, headers, quoting). Created once and reused across multiple COPY INTO operations."},
])

render_what_you_built([
    "{{DATABASE_NAME}} database and {{SCHEMA_NAME}} schema",
    "{{WAREHOUSE_NAME}} warehouse (Medium, auto-suspend 60s)",
    "{{NUM_TABLES}} operational data tables loaded from CSV (~{{TOTAL_ROWS}} total rows)",
])
