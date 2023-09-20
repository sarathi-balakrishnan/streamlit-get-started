import streamlit as st
import  snowflake.connector
import pandas as pd

@st.cache_resource
def init_connection():
    return snowflake.connector.connect(
        **st.secrets["snowflake4"], client_session_keep_alive=True
    )

con = init_connection()

cur = con.cursor()

sql = "select SERVICE_TYPE, NAME, CREDITS_USED_COMPUTE, CREDITS_USED_CLOUD_SERVICES, CREDITS_USED from snowflake.account_usage.metering_history limit 10;"
cur.execute(sql)    
results = cur.fetchall()
df = pd.DataFrame(results, columns=[desc[0] for desc in cur.description])
st.dataframe(df, hide_index=True)