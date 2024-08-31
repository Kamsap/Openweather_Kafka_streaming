from kafka import KafkaConsumer
from cassandra.cluster import Cluster
import json

# Connexion à Cassandra
cluster = Cluster(['127.0.0.1'])
session = cluster.connect('weather')

# Initialisation du consommateur Kafka
consumer = KafkaConsumer(
    'weather',
    bootstrap_servers=['127.0.0.1:9042'],
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Boucle pour consommer les messages Kafka et les insérer dans Cassandra
for message in consumer:
    data = message.value
    session.execute("""
        INSERT INTO weather_data (city_id, city_name, temperature, humidity, weather_description, timestamp)
        VALUES (%s, %s, %s, %s, %s, toTimestamp(now()))
    """, (data['id'], data['name'], float(data['main']['temp']), int(data['main']['humidity']), data['weather'][0]['description']))
    print(f"Insertion réussie pour la ville {data['name']}")