import streamlit as st
import pandas as pd

@st.cache
def load_data():
    return pd.read_csv('Reporte_Arreglado.csv')

data = load_data()

st.title('Reporte de Aparición de Dependencias en Leyes')

leyes = st.multiselect('Selecciona la Ley', data['doc_name'].unique())
dependencias = st.multiselect('Selecciona la Dependencia', data['entity_text'].unique())

filtered_data = data
if leyes:
    filtered_data = filtered_data[filtered_data['doc_name'].isin(leyes)]
if dependencias:
    filtered_data = filtered_data[filtered_data['entity_text'].isin(dependencias)]

st.dataframe(filtered_data)
