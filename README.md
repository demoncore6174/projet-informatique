# projet-informatique

## Idées de projets:

Voici les pistes envisagées pour notre réalisation :

- [ ] **Jeu du Simon** — Reproduction du jeu avec un système de gestion des couleurs.
- [ ] **Banque interactive** — Simulation d'un système bancaire utilisant des capteurs NFC.

---

---
# Analyse Fonctionnelle : Projet Simon 
 
**Membres du groupe :**

BLERIOT Pierre 21608749

VENTURA Maël 21602758

MOVSISYAN Davit 21605413

**Projet :** Version interactive du jeu de mémoire "Simon" sur Raspberry Pi.

---

## 1. Introduction : Description générale du projet

### Contexte et Objectif:
Le projet a pour objectif de reproduire le jeu de mémoire **Simon**. dont le joueur doit mémoriser et reproduire des séquences de couleurs qui vont devenir de plus en plus difficiles au fil de la partie


---

## 2. Schéma général du projet

Le projet se construit autour d'un micro-ordinateur Raspberry Pi qui fait office de cœur central.

* **Composants matériels (Raspberry Pi & Kit Grove) :**
  * **Entrées :** 

    -4 boutons poussoirs (pour les 4 couleurs/séquences).
  * **Sorties (Actionneurs) :** 
  
    -4 LEDs de couleurs pour afficher la séquence.
    
    -un Buzzer pour associer un son unique à chaque couleur.

    -un écran RGB afin d'afficher des informations à l'utilisateur
* **Flux de données & Interaction :**
  * Le script Python (exécuté sur le Raspberry Pi) gère la logique du jeu, lit les boutons, pilote les actionneurs et assure le bon déroulement du jeu et de sa difficulté.
  * Les données de score de chaque partie jouée sont transmises et enregistrées dans une base de données.
  * Une page web communique avec la base de données pour afficher le classement en temps réel sur le web, accessible depuis n'importe quel appareil (ordinateur, smartphone).
---
```
  [ Joueur ] <---> [ 4 Boutons (Entrées) ]
      ^                  |
      |                  v          
[ LED, Buzzer et écran ] <-- [ Raspberry Pi ] ---> [ Base de Données ]
                                                           |
                                                           v 
                                            [ Site Web (Scores) ]
```


Le raspberry Pi interagit avec le joueur à travers les LED, le buzzer et l'éran. Le joueur, à travers les boutons peut aussi interagir avec le raspberry Pi qui avec son script pthon va déterminer si la partie  est terminée. Dans ce cas, il va transmettre de nouvelles données dans la base de données qui seront utilisées afin d'afficher un classement des scores.
---

## 3. Scénarios d'usages

* **Scénario 1 : Lancement et déroulement d'une partie par le joueur**
  Le joueur s'installe devant le projet et lance le script de jeu. Le Raspberry Pi génère une séquence aléatoire de couleurs avec des sons associés à chaque couleur. Le joueur observe, puis appuie sur les boutons correspondants. Si la séquence est correcte, un niveau supplémentaire s'ajoute et la difficulté augmente. En cas d'erreur, la partie s'arrête et le score final est affiché et sauvegardé.

* **Scénario 2 : Enregistrement automatique du score**
  À la fin de la partie (qu'elle soit gagnée ou perdue), le script Python récupère le pseudo ( ou une série d chiffres) du joueur ainsi que son score et les insère automatiquement dans la base de données avec la date exacte.

* **Scénario 3 : Consultation du classement en ligne**
  Un utilisateur (joueur ou visiteur) se rend sur le site web du projet. Depuis la page, il peut consulter en temps réel le classement général des meilleurs scores ainsi que les statistiques globales des parties jouées.

---

## 4. Fonctionnalités principales et secondaires


| $n^\circ$ | Nom | Description | Sur quoi la fonction agit | Importance |
| :--- | :--- | :--- | :--- | :--- |
| **1** | Générer la séquence | Le script Python génère ou allonge la séquence aléatoire de jeu | Raspberry Pi, LEDs, Buzzer | **1** |
| **2** | Lire les entrées joueur | Le Raspberry Pi détecte les appuis sur les 4 boutons poussoirs | Boutons, Raspberry Pi | **1** |
| **3** | Valider la séquence | Le programme compare la saisie du joueur avec la séquence attendue | Raspberry Pi, script python, écran | **1** |
| **4** | Enregistrer le score | Stockage automatique du score et du pseudo en fin de partie | Raspberry Pi, Base de données | **2** |
| **5** | Afficher le tableau des scores | Le site web récupère et affiche le classement des meilleurs joueurs | Base de données, Site web | **2** |
| **6** | Saisir son pseudo | Le joueur entre son nom ou un nombre avant ou après la partie pour enregistrer son score | écran, Raspberry Pi | **3** |

---

## 5. Planning prévisionnel

Répartition indicative des tâches sur les 6 semaines du projet :

| Membres du groupe | Semaine 1 | Semaine 2 | Semaine 3 | Semaine 4 | Semaine 5 | Semaine 6 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **VENTURA Maël** (Matériel & Logique Python) |Branchement et configuration des composants  |Développement du script Python principal  |----------|connexion avec python et la base de données|test du jeu dans son intégralité |finitions possibles et bugs |
| **BLERIOT Pierre** (site web)  | conception du site |--- | connexion à la base de données | --- | test | finitions possibles et bugs |
| **MOVSISYAN Davit** ( base de données)  |  conception de la base de données|--- |intégration des scores et connexion au site |  connexion avec le code python | test | finitions possibles et bugs|
