# Utilisation de l'image officielle Python
FROM python:3.9-slim
# Définir le répertoire de travail
WORKDIR /app


COPY . /app


# COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


# Copier les fichiers nécessaires dans le conteneur
# COPY test.py ./


# Commande à exécuter au démarrage du conteneur
CMD ["python", "src/test.py"]
