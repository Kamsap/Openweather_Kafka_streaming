# Utiliser une image de base Python légère
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers requirements.txt dans le conteneur
COPY requirements-dashboard.txt .

# Installer les dépendances Python nécessaires
RUN pip install --no-cache-dir -r requirements-dashboard.txt

# Copier le script dashboard.py dans le conteneur
COPY dashboard.py .

# Exposer le port sur lequel Streamlit s'exécute
EXPOSE 8501

# Définir le point d'entrée pour exécuter Streamlit
CMD ["streamlit", "run", "dashboard.py"]