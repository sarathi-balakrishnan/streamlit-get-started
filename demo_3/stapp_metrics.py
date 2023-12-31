import streamlit as st 
#import snowflake.connector
from snowflake.snowpark import Session
#from snowflake.snowpark import QueryRecord
#from snowflake.snowpark.functions import col
#from snowflake.snowpark.functions import substr
#from snowflake.snowpark.types import IntegerType, StringType, StructField, StructType, DateType
import json

st.set_page_config(page_title="Snowpark with Streamlit Demo", page_icon=":smiley:", layout="wide")

# Initialize connection.
# Uses @st.cache_resource to only run once.
@st.cache_resource 
def init_connection():
    if "snowpark_session" not in st.session_state:
        # Get the current credentials
        #session = get_active_session()
        with open('credentials.json') as f:
            connection_parameters = json.load(f)
        session = Session.builder.configs(connection_parameters).create()
        st.session_state['snowpark_session'] =session
    else:
        session = st.session_state['snowpark_session']
    return session


conn_session = init_connection()


# Perform query.
# Use @st.cache_data to rerun only when the query changes or after 10 min.
def snowpark_df(query):
    df=conn_session.sql(query)
    return df




st.title("KPI Dashboard")

## Top row metrics 
st.markdown('## Key Metrics')

col1, col2, col3 = st.columns(3)

col1.metric(label = "Total Number of User", value = '200' , delta = "-2")
col2.metric("Total Credits Used", "3200", "0.46%")
col3.metric("Long Running Quries (>30m)", "406", "+4.87%")

st.markdown('## Detailed Charts')

col1, col2 = st.columns(2)

## Chart 1 - Warehouse Credits Over Time 
col1.markdown('## Warehouse Credits Over Time')

df_whCr=snowpark_df('select MNTH,uniform(100, 1000, random()) as SUM_CR from WarehouseCreditsOverTime order by 1') 
#used randon number for sample. remove "uniform(100, 1000, random()) as" to get real number for WH

col1.bar_chart(df_whCr,x="MNTH",y="SUM_CR")

## Chart 2 - Credits by Warehouse

df_CrbyWH=snowpark_df('select WAREHOUSE_NAME,uniform(100, 1000, random())  as CREDITS_USED from WarehouseCreditUsage')

col2.markdown('## Credits by Warehouse')

col2.bar_chart(df_CrbyWH, x="WAREHOUSE_NAME", y="CREDITS_USED")

##Chart 3 - Monthly Credits by Type'

col1.markdown('## Monthly Credits by Type')

df_MnCrUsage=snowpark_df('select MONTH,uniform(100, 1000, random()) as WAREHOUSE_CREDITS,uniform(100, 1000, random()) as PIPE_CREDITS,uniform(100, 1000, random()) as MVIEW_CREDITS,uniform(100, 1000, random()) as CLUSTERING_CREDITS,uniform(100, 1000, random()) as READER_CREDITS from MonthlyCreditsbyType')
col1.line_chart(df_MnCrUsage,x="MONTH",y=["WAREHOUSE_CREDITS","PIPE_CREDITS","MVIEW_CREDITS","CLUSTERING_CREDITS","READER_CREDITS"])

col2.write(df_MnCrUsage)

## Chart 4 - Credits by hour of the day

df_CrbyWH=snowpark_df('select HOUR,uniform(100, 1000, random()) as CR from HourlyCreditUsage')

col2.markdown('## Credits by hour of the day')

col2.area_chart(df_CrbyWH, x="HOUR", y="CR")

## Chart 5 - Data Storage Cost by Month

df_storage_cost=snowpark_df('select SORT_MONTH,uniform(100, 500, random()) as STORAGE,uniform(50, 200, random()) as  STAGE,uniform(100, 200, random()) as FAILSAFE from MonthlyStorageUsage')

col1.markdown('## Data Storage Cost by Month')

col1.bar_chart(df_storage_cost,x="SORT_MONTH",y=['STORAGE', 'STAGE', 'FAILSAFE'])
