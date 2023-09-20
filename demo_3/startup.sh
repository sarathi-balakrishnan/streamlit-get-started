#!/bin/bash

# Install Streamlit if not already installed
if ! command -v streamlit &> /dev/null
then
    echo "Streamlit not found, installing..."
    pip install streamlit
fi
pip install numpy
pip install pandas
pip install seaborn
pip install plotly
pip install snowflake-connector-python
pip install snowflake-snowpark-python


# Run the Streamlit hello command
streamlit run stapp_metrics.py  --server.port 8000 --server.address 0.0.0.0

