import streamlit as st
from kafka import KafkaConsumer
#import json
import pandas as pd
import time


# Attendre quelques secondes pour s'assurer que Kafka est prêt
time.sleep(10)

consumer = KafkaConsumer(
    'weather_topic',
    bootstrap_servers=['kafka:8501'],
    auto_offset_reset='earliest',
    group_id='dashboard-group'
)

# Création de l'interface Streamlit
st.title('Dashboard Météo en Temps Réel')

placeholder = st.empty()

for message in consumer:
    data = message.value
    df = pd.DataFrame([{
        'Ville': data['name'],
        'Température (°C)': data['main']['temp'],
        'Humidité (%)': data['main']['humidity'],
        'Description': data['weather'][0]['description']
    }])

    placeholder.dataframe(df)