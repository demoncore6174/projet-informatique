# projet-informatique

## Idées de projets:

Voici les pistes envisagées pour notre réalisation :

- [ ] **Jeu du Simon** — Reproduction du jeu avec un système de gestion des couleurs.
- [ ] **Banque interactive** — Simulation d'un système bancaire utilisant des capteurs NFC.

---

## Analyse Fonctionnelle : Le Jeu du Simon

### 1. Présentation Générale
* **Objectif du projet :** Concevoir une version interactive et connectée du jeu de mémoire "Simon" sur Raspberry Pi. Le système génère une séquence lumineuse et sonore que le joueur doit reproduire à l'aide de boutons physiques. Les scores sont enregistrés en base de données et consultables en temps réel sur une interface web.

### 2. fonctionnement entre le joueur et le projet
le joueur peut interagir avec le raspberry py. Il va observer une séquence de couleurs qu'il devra reproduire à l'aide de 4 boutons. Plus, il réussit, plus un score augmente et la difficulté de même. Hors des parties, le joueur pourra observer sur un site son classement par rapport aux autres.

### 3. Spécifications Fonctionnelles

#### A. Partie Matérielle (Raspberry Pi & Kit Grove)
* **Entrées (Capteurs) :** 4 boutons poussoirs (Grove - Button) pour saisir la séquence.
* **Sorties (Actionneurs) :** 
  * 4 LEDs de couleurs (ou un écran LCD RGB) pour afficher la séquence à mémoriser.
  * Un Buzzer (Grove - Buzzer) pour émettre un son distinct par couleur ( pour rendre unique chaque couleur)
* **Logique de jeu :** Le script Python gère la génération aléatoire des séquences, l'écoute des entrées, la vérification de la réponse et l'augmentation progressive de la difficulté.

#### B. Partie Base de Données
* **Enregistrement :** Stockage automatique après chaque partie de :
  * Le pseudo du joueur.
  * Le score (nombre d'étapes réussies).
  * La date et l'heure de la partie.

#### C. Partie Web & FastAPI
* **Tableau de bord (Dashboard) :** Hébergé via **FastAPI**, permettant d'afficher :
  * Le classement général des meilleurs scores.
  * Les statistiques globales des parties jouées.

 ---
## Analyse Fonctionnelle : La Station Météo Intelligente

### 1. Présentation Générale

* **Objectif du projet :** Concevoir une station météo connectée et autonome sur Raspberry Pi. Le système mesure en continu les grandeurs environnementales (température, humidité, pression atmosphérique, luminosité) à l'aide de capteurs Grove, analyse les tendances pour prédire les changements de temps, enregistre l'historique dans une base de données et permet de consulter les données et alertes en temps réel sur une interface web.

### 2. Fonctionnement entre l'utilisateur et le projet

Le utilisateur peut interagir avec le système de deux manières :
* **En local :** Il observe les conditions actuelles affichées directement sur un écran LCD RGB relié au Raspberry Pi, qui change de couleur selon le niveau de confort ou d'alerte (ex. bleu si froid, rouge si canicule/alerte).
* **À distance via le web :** Il se connecte au tableau de bord en ligne pour analyser l'historique des relevés sous forme de graphiques, suivre les tendances de pression (pour anticiper la pluie) et consulter des statistiques globales.

### 3. Spécifications Fonctionnelles

#### A. Partie Matérielle (Raspberry Pi & Kit Grove)

* **Entrées (Capteurs) :**
  * Un capteur de température et d'humidité (Grove - Temperature Sensor / DHT) pour la météo ambiante.
  * Un baromètre de haute précision (Grove - Barometer High-Accuracy) pour mesurer la pression atmosphérique et détecter les variations météo (loi des théodolites / tendance de Torricelli).
  * Un capteur de luminosité (Grove - Light Sensor) pour mesurer l'ensoleillement.
* **Sorties (Actionneurs) :**
  * Un écran LCD RGB (Grove - LCD RGB Backlight) pour afficher les messages, la température et l'état de l'air.
  * Un Buzzer (Grove - Buzzer) pour émettre un signal sonore en cas d'alerte météo critique (ex. chute brutale de pression ou température anormale).
* **Logique de script :** Un script Python s'exécute en arrière-plan pour interroger périodiquement les capteurs, stocker les données, piloter l'affichage LCD et évaluer des seuils d'alerte.

#### B. Partie Base de Données

* **Enregistrement :** Stockage périodique (toutes les X minutes) des données environnementales comprenant :
  * La température et l'humidité mesurées.
  * La pression atmosphérique.
  * Le niveau de luminosité.
  * La date et l'heure exactes de la mesure (horodatage).

#### C. Partie Web & FastAPI

* **Tableau de bord (Dashboard) :** Hébergé via **FastAPI**, permettant d'afficher :
  * Les graphiques d'évolution des grandeurs météo en temps réel.
  * Les prévisions simples basées sur la variation de la pression atmosphérique (ex. « Pluie probable », « Temps stable »).
  * Les statistiques globales (température min/max de la journée, pics de luminosité).

