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
