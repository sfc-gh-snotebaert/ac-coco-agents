import streamlit as st
from components import render_session_header, render_prompt, render_explanation, render_technologies_used, render_key_concepts, render_what_you_built

render_session_header(6, 'Agent Skill: Forecast Flight Volume', '11:25 AM – 11:45 AM', '20 min', 'A forecasting model and a custom tool that lets the agent predict flight volume')

render_technologies_used([{'name': 'SNOWFLAKE.ML.FORECAST', 'description': 'Built-in time-series forecasting that handles seasonality automatically.', 'icon': 'trending_up'}, {'name': 'Custom tool', 'description': 'A stored procedure or UDF added to the agent as a tool.', 'icon': 'build'}, {'name': 'Skills', 'description': 'Reusable instructions/procedures that extend what an agent can do.', 'icon': 'school'}])

render_prompt('Prompt 6.1', 'Train the forecast model', 'In AIRLINE_OPS.OPS create a view DAILY_FLIGHT_VOLUME (FLIGHT_DATE, ORIGIN_AIRPORT_CODE, NUMBER_OF_FLIGHTS) from DIM_FLIGHT for dates up to today, then train a SNOWFLAKE.ML.FORECAST model FLIGHT_VOLUME_FORECAST with one series per origin airport. Show the forecast for YYZ for the next 30 days and the model evaluation metrics.')

render_prompt('Prompt 6.2', 'Wrap it as an agent skill/tool', 'Create a stored procedure FORECAST_FLIGHT_VOLUME(AIRPORT_CODE VARCHAR, DAYS INT) that returns the forecast (date, forecast, lower and upper bound) from FLIGHT_VOLUME_FORECAST. Add it as a custom tool on AIRLINE_OPS_AGENT with a clear description of when to use it, and add an orchestration instruction: use the forecast tool for future flight volume, and the semantic view for historical data.')

render_prompt('Prompt 6.3', 'Test in CoWork', 'Ask AIRLINE_OPS_AGENT: "How many flights do we expect to depart from YUL over the next 2 weeks, and how does that compare with the same period last year?" Confirm that it uses both the forecast tool and Cortex Analyst.')

render_key_concepts([{'term': 'Tool description', 'definition': 'The agent picks tools by their description, so write it like documentation: what it does, inputs and when to use it.'}])

render_what_you_built(['FLIGHT_VOLUME_FORECAST model', 'FORECAST_FLIGHT_VOLUME tool on the agent', 'Agent answering both historical and forward-looking questions'])
