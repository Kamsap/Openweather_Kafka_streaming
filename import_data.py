import json
import gzip

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
