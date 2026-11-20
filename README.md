# Brief 4 : application Web Data avec Streamlit

Application web Data réalisée avec **Streamlit** pour l'entreprise fictive **DataInsight Solutions** (brief de la Wild Code School). Elle propose une page de connexion sécurisée (comptes lus dans un fichier CSV), un menu de navigation latéral et une galerie d'images sur 3 colonnes. Le projet contient aussi deux petits tableaux de bord réalisés pendant la formation (taxis et vols) : voir plus bas.


## Application en ligne
https://brief4-app-ltfpsutaslf4dzdwuwvtnj.streamlit.app/

L'application demande une connexion. Comptes de test :

| Nom d'utilisateur | Mot de passe |
|---|---|
| `utilisateur` | `mdp123` |
| `admin` | `admin123` |

## Contenu du dépôt
| Fichier ou dossier | Rôle |
|---|---|
| `app_securisee.py` | **Application principale** : connexion par fichier CSV, menu latéral, page d'accueil, galerie photos |
| `accounts.csv` | Comptes de test (nom, mot de passe, email, tentatives, connecté, rôle) |
| `images/` | Images de la galerie |
| `app.py` | Première application Streamlit (prise en main) |
| `app_taxis.py` | Tableau de bord des taxis : menu déroulant, filtre, tableau, métrique |
| `app_dataviz.py` | Tableau de bord des vols : slider d'années, choix du mois, métrique, courbe, heatmap |
| `CSV/` | Jeux de données de Seaborn Data (`taxis.csv`, `flights.csv`) |
| `requirements.txt` | Liste des bibliothèques à installer |
| `.gitignore` | Fichiers non envoyés sur GitHub (dont le dossier `venv/`) |

## Lancer l'application en local
Prérequis : **Python 3.10 à 3.12** (testé avec 3.12.4) et **Git**.

1. **Cloner** le dépôt :
   ```bash
   git clone https://github.com/flo-gllrd/brief4-streamlit.git
   ```
2. **Se placer** dans le dossier :
   ```bash
   cd brief4-streamlit
   ```
3. **Créer** l'environnement virtuel :
   ```bash
   python -m venv venv
   ```
4. **Activer** l'environnement virtuel (`(venv)` doit apparaître dans le terminal) :
   - Git Bash (Windows) : `source venv/Scripts/activate`
   - PowerShell (Windows) : `.\venv\Scripts\activate`
   - Mac / Linux : `source venv/bin/activate`
5. **Installer** les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
6. **Lancer** l'application :
   ```bash
   streamlit run app_securisee.py
   ```
   Elle s'ouvre dans le navigateur sur `http://localhost:8501`. Se connecter avec un compte de test, puis utiliser le menu latéral (Accueil, Galerie Photos). Pour arrêter l'application : `Ctrl+C` dans le terminal.

## Lancer les applications d'entraînement
Avec le même environnement activé :
```bash
streamlit run app_taxis.py
streamlit run app_dataviz.py
```

## Technologies
Python, Streamlit, streamlit-option-menu, Pandas, Seaborn, Matplotlib. Déploiement : Streamlit Community Cloud. Versionnement : Git et GitHub.

## Remarque de sécurité
Les mots de passe de `accounts.csv` sont écrits **en clair** : c'est une simplification pour l'exercice, avec des comptes de test uniquement. Dans un vrai projet, on stockerait des empreintes (*hash*) des mots de passe et on ne publierait jamais ce fichier.