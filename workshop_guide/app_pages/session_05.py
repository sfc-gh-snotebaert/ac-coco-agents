import streamlit as st
from components import render_session_header, render_prompt, render_explanation, render_technologies_used, render_key_concepts, render_what_you_built

render_session_header(5, 'Evaluate the Agent', '11:00 AM – 11:25 AM', '25 min', 'An evaluation dataset and scored evaluation run for AIRLINE_OPS_AGENT')

render_technologies_used([{'name': 'Agent evaluations', 'description': 'Run the agent against a set of questions with expected answers and score correctness, tool selection and groundedness.', 'icon': 'fact_check'}, {'name': 'Ground truth', 'description': 'Questions with reference answers computed by SQL you trust.', 'icon': 'table_rows'}, {'name': 'AI Observability', 'description': 'Traces and metrics for each agent run.', 'icon': 'monitoring'}])

render_prompt('Prompt 5.1', 'Build the evaluation dataset', 'In AIRLINE_OPS.OPS create a table AGENT_EVAL_DATASET with 10 questions about the airline data (revenue YoY, top routes, OTP by hub, cancellation rate, load factor, Aeroplan tier mix, plus 2 out-of-scope questions such as weather). For each, compute the ground-truth answer with SQL against the base tables and store it as the expected answer.')

render_prompt('Prompt 5.2', 'Run the evaluation', 'Create and run a Cortex Agent evaluation of AIRLINE_OPS.OPS.AIRLINE_OPS_AGENT using AGENT_EVAL_DATASET, measuring answer correctness and logical consistency. Show the scores per question and highlight the failures.')

render_prompt('Prompt 5.3', 'Improve and re-run', 'Based on the failed questions, improve the agent instructions or the semantic view (synonyms, metrics, verified queries), then re-run the evaluation and compare the scores with the first run.')
render_explanation("What this prompt does", 'This is the core loop for production agents: measure, fix, re-measure. Keep the dataset as a regression test.')

render_key_concepts([{'term': 'Regression evaluation', 'definition': "Re-running the same dataset after every change makes sure fixes don't break other answers."}])

render_what_you_built(['Ground-truth evaluation dataset', 'Baseline and improved evaluation runs'])
