# Utiliser une image de base Python légère
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers requirements.txt dans le conteneur
COPY requirements-producer.txt .

# Installer les dépendances Python nécessaires
RUN pip install --no-cache-dir -r requirements-producer.txt

# Copier le script producer.py dans le conteneur
COPY producer.py .

# Définir le point d'entrée pour exécuter le script du producteur
CMD ["python", "producer.py"]