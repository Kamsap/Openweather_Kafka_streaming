import json
import gzip
import requests
from kafka import KafkaProducer
import time

# Étape 2 : Lire le fichier gzip et décompresser
def get_french_cities(fichier):
    """Extrait les villes françaises du fichier city.list.json.gz."""
    try:
        with gzip.open(fichier, 'rt', encoding='utf-8') as file:
            city_data = json.load(file)
            french_cities = [city for city in city_data if city['country'] == 'FR']
            return french_cities
    except FileNotFoundError:
        print("Le fichier n'a pas été trouvé. Vérifiez le chemin d'accès.")
        return []
    except json.JSONDecodeError:
        print("Erreur lors du décodage du fichier JSON.")
        return []
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return []

# Charger la liste des villes françaises
french_cities = get_french_cities('city.list.json.gz')
print(f"Nombre de villes françaises trouvées : {len(french_cities)}")
'''

'''
# Étape 3 : Développer le Producteur Python
# Initialisation du producteur Kafka
producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

# Clé d'API pour OpenWeatherMap
api_key = 'cb1b726d5f2ffe9c65d6da7787cbc2bc'

# Fonction pour interroger l'API OpenWeatherMap
def fetch_weather_data(city_id):
    url = f'http://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erreur lors de l'appel de l'API pour la ville ID {city_id}: {response.status_code}")
        return None

# Boucle pour envoyer les données à Kafka
while True:
    for city in french_cities:
        city_id = city['id']
        weather_data = fetch_weather_data(city_id)
        if weather_data:
            producer.send('weather', value=weather_data)
            print(f"Envoyé des données pour la ville {city['name']} - {weather_data}")
        time.sleep(5)  # Pause pour limiter le nombre de requêtes API
    time.sleep(60)  # Pause d'une minute entre chaque cycle complet