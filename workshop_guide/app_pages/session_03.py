import streamlit as st
from components import render_session_header, render_prompt, render_explanation, render_technologies_used, render_key_concepts, render_what_you_built

render_session_header(3, "Cortex Search", "{{TIME_SESSION_3}}", "{{DUR_SESSION_3}}", "Knowledge base, Cortex Search service, and RAG query pattern")

render_technologies_used([
    {"name": "Cortex Search Service", "description": "A managed hybrid search engine combining vector (semantic) and keyword search with automatic reranking. Created with a single SQL statement.", "icon": "search"},
    {"name": "RAG (Retrieval Augmented Generation)", "description": "A pattern that retrieves relevant documents first, then passes them as context to an LLM for grounded answer generation.", "icon": "hub"},
    {"name": "SEARCH_PREVIEW", "description": "SQL function to query a Cortex Search Service. Supports text queries, column selection, filtering, and result limits.", "icon": "preview"},
])


PROMPT_3_1 = """In {{DATABASE_NAME}}.{{SCHEMA_NAME}}:

1. First, create a unified text table for search called {{KNOWLEDGE_BASE_TABLE}} that combines:
{{KNOWLEDGE_BASE_UNION_INSTRUCTIONS}}

2. Then create a Cortex Search Service:
   CREATE OR REPLACE CORTEX SEARCH SERVICE {{SEARCH_SERVICE_NAME}}
     ON content
     ATTRIBUTES metadata_category, metadata_priority, doc_type
     WAREHOUSE = {{WAREHOUSE_NAME}}
     TARGET_LAG = '1 hour'
     EMBEDDING_MODEL = 'snowflake-arctic-embed-l-v2.0'
     AS (
       SELECT doc_id, doc_type, content, metadata_category, metadata_priority, doc_date
       FROM {{KNOWLEDGE_BASE_TABLE}}
     );

Execute all SQL. Then verify with SHOW CORTEX SEARCH SERVICES."""

render_prompt("Prompt 3.1", "Create Cortex Search Service", PROMPT_3_1)

render_explanation("What this prompt does", """
Builds a unified knowledge base from unstructured text sources and creates a hybrid search service.

The search service automatically embeds, indexes, and serves results with auto-refresh when source data changes.
""")


PROMPT_3_2 = """In {{DATABASE_NAME}}.{{SCHEMA_NAME}}, query our {{SEARCH_SERVICE_NAME}} service using SEARCH_PREVIEW:

{{SEARCH_TEST_QUERIES}}

Execute all searches and show results."""

render_prompt("Prompt 3.2", "Query the Search Service", PROMPT_3_2)

render_explanation("What this prompt does", """
Tests different search capabilities across the document corpus:

{{SEARCH_TEST_EXPLANATION}}
""")


PROMPT_3_3 = """In {{DATABASE_NAME}}.{{SCHEMA_NAME}}, implement a RAG pattern:

1. Question: "{{RAG_QUESTION}}"

2. Retrieve top 5 documents from {{SEARCH_SERVICE_NAME}}, then pass to SNOWFLAKE.CORTEX.COMPLETE() with instructions to answer ONLY from the provided documents, cite doc_ids, and structure the answer with: 1) Common incident types, 2) Root causes, 3) Effective measures, 4) Recommendations.

Use claude-sonnet-4-6 as the model. Execute and show the RAG response."""

render_prompt("Prompt 3.3", "RAG Pattern: Search + Generate", PROMPT_3_3)

render_explanation("What this prompt does", """
Implements the full **RAG** pattern: retrieve relevant documents, then generate a grounded answer with citations.
""")


render_key_concepts([
    {"term": "Cortex Search Service", "definition": "A managed hybrid search engine created with SQL. Handles embedding, indexing, reranking, and auto-refresh automatically."},
    {"term": "RAG", "definition": "Retrieval Augmented Generation: retrieve documents, include as context in LLM prompt, generate grounded answer."},
    {"term": "Hybrid Search", "definition": "Combining vector search (semantic similarity) with keyword search (exact matching). Better than either alone."},
])

render_what_you_built([
    "{{KNOWLEDGE_BASE_TABLE}} — unified document table",
    "{{SEARCH_SERVICE_NAME}} — Cortex Search service with hybrid search",
    "Search queries across multiple document types",
    "Full RAG pipeline for grounded Q&A",
])
