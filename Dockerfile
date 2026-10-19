# Image de départ : Python 3.12 en version légère
FROM python:3.12-slim

# Dossier de travail dans le conteneur
WORKDIR /app

# On installe d'abord les librairies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Puis on copie les fichiers de l'application
COPY app.py model.pkl ./
COPY templates ./templates
COPY static ./static

# Port utilisé par Flask
EXPOSE 5000

# Commande lancée au démarrage du conteneur
CMD ["python", "app.py"]
