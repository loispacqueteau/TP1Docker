import os
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

# Connexion au conteneur MongoDB via son nom réseau défini dans Docker Compose
mongo_uri = os.getenv("MONGO_URI", "mongodb://mongo:27017/testdb")
client = MongoClient(mongo_uri)
db = client.testdb


@app.route("/")
def hello():
  # Enregistre une nouvelle visite en insérant un document dans la collection
  db.visits.insert_one({"visite": True})
  # Compte le nombre total de documents dans la collection
  count = db.visits.count_documents({})
  return f"Hello! Visites enregistrées en BDD : {count}"


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)
