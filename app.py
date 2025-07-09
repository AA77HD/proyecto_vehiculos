import pandas as pd
import plotly.express as px
import streamlit as st


car_data = pd.read_csv('vehicles_us.csv')

st.header('Análisis de anuncios de vehículos usados')

show_hist = st.checkbox('Mostrar histograma')

if show_hist:
    st.write('Histograma del kilometraje (odometer)')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)


scatter_button = st.checkbox('Mostrar gráfico de dispersión')

if scatter_button:
    st.write('Relación entre precio y año del vehículo')
    fig2 = px.scatter(car_data, x='model_year', y='price', color='type')
    st.plotly_chart(fig2, use_container_width=True)

