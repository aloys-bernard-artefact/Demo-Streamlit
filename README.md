# 🎨 Demo Streamlit - Application Interactive

Une application de démonstration Streamlit présentant des visualisations de données interactives, des graphiques avec Plotly, et un jeu amusant de Pierre-Feuille-Ciseaux.

## 📋 Description

Cette application démontre les capacités de Streamlit pour créer des interfaces web interactives en Python. Elle inclut :

- 📊 **Visualisations de données** : Graphiques interactifs utilisant le célèbre dataset Iris
- 🎮 **Mini-jeu** : Pierre-Feuille-Ciseaux contre l'ordinateur
- 🐱 **Galerie d'images** : Collection d'images de chats adorables
- 📈 **Graphiques variés** : Multiples types de visualisations (scatter, bar, line, etc.)

## 🚀 Installation

### Prérequis

- Python 3.7 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. **Cloner le repository**
   ```bash
   git clone https://github.com/aloys-bernard-artefact/Demo-Streamlit.git
   cd Demo-Streamlit
   ```

2. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurer les secrets** (optionnel)
   
   Créer un fichier `.streamlit/secrets.toml` avec votre configuration :
   ```toml
   db_username = "votre_username"
   db_password = "votre_password"
   ```

## 🎯 Utilisation

### Lancer l'application

```bash
streamlit run app.py
```

L'application s'ouvrira automatiquement dans votre navigateur par défaut à l'adresse `http://localhost:8501`

### Fonctionnalités

#### 1. Visualisation de données Iris
- Sélectionnez les colonnes à afficher sur les axes X et Y
- Explorez les différentes caractéristiques des fleurs Iris
- Visualisez les données par espèce avec des couleurs différentes
- Interaction complète avec le graphique (zoom, pan, hover)

#### 2. Graphiques variés
- **Scatter plot** : Analyse de corrélation entre variables
- **Bar chart** : Comparaison des moyennes par espèce
- **Line chart** : Tendances et évolutions
- **Histogrammes** : Distribution des valeurs

#### 3. Jeu Pierre-Feuille-Ciseaux
- Choisissez votre coup : Pierre, Feuille ou Ciseaux
- Jouez contre l'ordinateur
- Découvrez le gagnant instantanément avec des animations

#### 4. Galerie d'images de chats 🐱
- Admirez une collection d'adorables photos de chats
- Images affichées de manière élégante dans l'interface

## 📦 Dépendances

- **streamlit** (1.51.0) : Framework pour créer des applications web interactives
- **plotly** (6.3.0) : Bibliothèque de visualisation de données interactive

## 🏗️ Structure du projet

```
Demo-Streamlit/
│
├── app.py                 # Application principale Streamlit
├── requirements.txt       # Dépendances Python
├── README.md             # Ce fichier
├── images/               # Dossier des images
│   └── cats/            # Images de chats
└── .streamlit/          # Configuration Streamlit
    └── secrets.toml     # Fichier de secrets (non versionné)
```

## 🎨 Captures d'écran

L'application présente une interface moderne et intuitive avec :
- Des contrôles interactifs pour la sélection des données
- Des graphiques réactifs et colorés
- Une expérience utilisateur fluide

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
1. Fork le projet
2. Créer une branche pour votre fonctionnalité (`git checkout -b feature/NouvelleFonctionnalite`)
3. Commit vos changements (`git commit -m 'Ajout de NouvelleFonctionnalite'`)
4. Push vers la branche (`git push origin feature/NouvelleFonctionnalite`)
5. Ouvrir une Pull Request

## 📝 Notes

- Cette application est à des fins de démonstration et d'apprentissage
- Le dataset Iris est chargé automatiquement depuis Plotly
- Les secrets sont utilisés pour démontrer la gestion sécurisée des configurations

## 🐛 Débogage

Si vous rencontrez des problèmes :
- Vérifiez que toutes les dépendances sont installées : `pip list`
- Assurez-vous d'utiliser Python 3.7+
- Consultez les logs dans le terminal

## 📧 Contact

Pour toute question ou suggestion, n'hésitez pas à ouvrir une issue sur GitHub.

## 🌟 Remerciements

- Merci à l'équipe Streamlit pour cet excellent framework
- Dataset Iris fourni par Plotly Express

---

*Développé avec ❤️ et Streamlit*
