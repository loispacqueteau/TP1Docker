<<<<<<< Updated upstream
# TP1Docker
=======
# Compte-Rendu de TP : Manipulation de Docker & Serveur Web

Ce README documente les différentes étapes réalisées lors du TP de Docker (Université Toulouse Capitole), basées sur les manipulations de base des conteneurs et la création d'un serveur web Nginx.

---

## 1. Vérification de l'environnement Docker

Pour commencer, nous vérifions que Docker est correctement installé sur la machine et consultons les images locales disponibles.

```bash
docker --version
docker images
```

* **Résultat :** Version de Docker affichée (`29.9.2`) et liste initiale des images (vide au départ).

---

## 2. Manipulation de base des conteneurs (Hello-World)

### A. Téléchargement de l'image `hello-world`
```bash
docker pull hello-world
```

### B. Vérification des images locales
```bash
docker images
```
* **Résultat :** L'image `hello-world:latest` apparaît désormais dans la liste.

### C. Exécution du conteneur
```bash
docker run hello-world
```
* **Résultat :** Le conteneur s'exécute, affiche un message de bienvenue confirmant le bon fonctionnement de Docker, puis s'arrête.

### D. Gestion des conteneurs (actifs et arrêtés)
* Lister les conteneurs actifs :
  ```bash
  docker ps
  ```
* Lister tous les conteneurs (y compris ceux arrêtés) :
  ```bash
  docker ps -a
  ```
  *(On y retrouve notre conteneur `hello-world` avec son ID et son statut `Exited`)*.

---

## 3. Création d'un serveur web avec Nginx

### A. Téléchargement de l'image Nginx
```bash
docker pull nginx
```

### B. Lancement du conteneur Nginx en arrière-plan
On lance un conteneur nommé `mon_nginx` en mode détaché (`-d`) et en redirigeant le port 8080 de la machine hôte vers le port 80 du conteneur (`-p 8080:80`) :
```bash
docker run -d -p 8080:80 --name mon_nginx nginx
```

### C. Vérification de l'activité du conteneur
```bash
docker ps
```
* **Résultat :** Le conteneur `mon_nginx` est listé avec le statut `Up` et les ports associés. Il est accessible à l'adresse [http://localhost:8080](http://localhost:8080).

### D. Nettoyage : Arrêt et suppression du conteneur
Pour stopper proprement le serveur Nginx puis le supprimer :
```bash
docker stop mon_nginx
docker rm mon_nginx
```

Vérification finale pour s'assurer que le conteneur n'est plus actif :
```bash
docker ps
```
>>>>>>> Stashed changes
