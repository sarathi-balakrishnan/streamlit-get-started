
import streamlit as st
import pandas as pd

#Generate SAS token and URL in Microsoft Azure
#Paste the blob_sas_url below
data = pd.read_csv('https://usfiles.blob.core.windows.net/trial/METADATA_EMAILNOTIFICATION2023_8_6_8_27_56.csv?sp=r&st=2023-09-11T13:03:14Z&se=2023-09-11T21:03:14Z&spr=https&sv=2022-11-02&sr=b&sig=OATUvWVrtp9SaAxRfaUKNEixLtRRIwL5JBRhTGVx%2Bhw%3D')
st.dataframe(data, hide_index=True)