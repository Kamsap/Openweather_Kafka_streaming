# Utiliser une image de base Python légère
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers requirements.txt dans le conteneur
COPY requirements-consumer.txt .

# Installer les dépendances Python nécessaires
RUN pip install --no-cache-dir -r requirements-consumer.txt

# Copier le script consumer.py dans le conteneur
COPY consumer.py .

# Définir le point d'entrée pour exécuter le script du consommateur
CMD ["python", "consumer.py"]