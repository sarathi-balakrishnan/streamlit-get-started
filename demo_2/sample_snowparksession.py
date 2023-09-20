
import streamlit as st
from snowflake.snowpark import Session

st.set_page_config(page_title="Snowpark Connection Demo", page_icon=":smiley:", layout="wide")

credentials = st.secrets["snowflake4"]
session = Session.builder.configs(credentials).create()
df = session.sql("select * from SNOWFLAKE.ACCOUNT_USAGE.SESSIONS limit 10").collect()

st.dataframe(df, hide_index=True)
st.snow()

#st.bar_chart(df,x="CLIENT_APPLICATION_VERSION",y="AUTHENTICATION_METHOD")