# 🚀 GlobalExam Endless - Mode Rapide

> **Langue :** [🇬🇧 English](README_EN.md) | [🇫🇷 Français](README_FR.md)

<div align="center">

![GlobalExam Endless](assets/5endless_logo.png)

**Automatisation ultra-rapide pour GlobalExam Activité 7 (Business > Bâtiment)**

[![Python](https://img.shields.io/badge/Python-3.13+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Windows](https://img.shields.io/badge/Windows-0078D4?style=for-the-badge&logo=windows&logoColor=white)](https://www.microsoft.com/)

**Mode Rapide • Sans Pause • Cycles Continus**

</div>

---

## 🎯 Qu'est-ce que GlobalExam Endless ?

**GlobalExam Endless** est un outil d'automatisation professionnel avec interface graphique pour l'Activité 7 de GlobalExam. Il fonctionne en continu sans pauses, idéal pour les complétions rapides.

### ✨ Fonctionnalités Principales

- ⚡ **Mode Ultra-Rapide** - Aucune pause entre les cycles
- 🎨 **Interface Moderne** - Thème sombre élégant avec accents violets
- 📊 **Statistiques en Temps Réel** - Suivi des cycles et de la progression
- 🔐 **Protection par Mot de Passe** - Authentification sécurisée au premier lancement
- 📐 **Adaptation Automatique** - Fonctionne sur toutes les résolutions d'écran
- 🔍 **Normalisation du Zoom** - Réglage automatique à 100%
- 📝 **Journal d'Activité en Direct** - Visualisation en temps réel

---

## 📦 Installation

### Démarrage Rapide

1. **Cloner ou télécharger** ce dépôt
2. **Installer les dépendances :**
   ```powershell
   pip install -r requirements.txt
   ```
3. **Lancer l'application :**
   ```powershell
   python 5endless_final_GUI.py
   ```

### Prérequis

- **OS :** Windows 10/11
- **Python :** 3.13+ (ou Python 3.x)
- **Navigateur :** Chrome/Firefox à 100% de zoom
- **Écran :** Toute résolution (adaptation automatique)

---

## 🚀 Utilisation

### Lancer l'Application

```powershell
python 5endless_final_GUI.py
```

### Premier Lancement

Au premier démarrage, un code d'accès vous sera demandé :
- Entrez le code lorsqu'il est demandé (saisie masquée)
- Un fichier `.first_run_ok` est créé après authentification
- Le code ne sera plus demandé sauf si vous supprimez ce fichier

### Utiliser l'Application

1. Ouvrez l'Activité 7 de GlobalExam dans votre navigateur
2. Cliquez sur **DÉMARRER** dans l'application
3. L'application va :
   - Détecter votre résolution d'écran
   - Normaliser le zoom du navigateur à 100%
   - Démarrer l'automatisation continue
4. Cliquez sur **ARRÊTER** pour stopper à tout moment

---

## 📊 Aperçu des Fonctionnalités

| Fonctionnalité | Description |
|----------------|-------------|
| **Mode Continu** | Fonctionne indéfiniment sans pauses |
| **Compteur de Cycles** | Suivi des cycles complétés |
| **Barre de Progression** | Progression visuelle à travers les questions |
| **Journal d'Activité** | Journalisation horodatée des événements |
| **Gestion d'Erreurs** | Récupération automatique en cas d'erreur |
| **Adaptation Résolution** | Fonctionne de 1366x768 jusqu'à 4K |

---

## 📂 Structure du Projet

```
GlobalExam_Endless/
├── 5endless_final_GUI.py    # Application principale
├── final_test.py             # Fonctions auxiliaires
├── PNJ/                      # Modèles d'images pour reconnaissance
├── assets/                   # Logos et icônes
│   ├── 5endless_logo.png
│   └── 5endless_logo.ico
├── requirements.txt          # Dépendances Python
├── .gitignore               # Règles d'exclusion Git
├── LICENSE                   # Fichier de licence
└── README.md                 # Ce fichier
```

---

## ⚙️ Configuration

### Adaptation Automatique de la Résolution

L'application adapte automatiquement les coordonnées basées sur une référence 1920x1080 :
- Détecte votre résolution actuelle
- Ajuste toutes les positions de clic proportionnellement
- Aucune configuration manuelle nécessaire

### Zoom du Navigateur

Au démarrage, l'application automatiquement :
- Appuie sur `Ctrl+0` trois fois
- S'assure que le navigateur est à 100% de zoom
- Prévient les désalignements de clics

---

## 🐛 Dépannage

| Problème | Solution |
|----------|----------|
| **Questions sautées** | Vérifiez que le zoom est à 100% |
| **Clics manquent la cible** | Vérifiez que l'adaptation résolution fonctionne |
| **L'appli ne démarre pas** | Vérifiez que Python 3.13+ est installé |
| **Images non trouvées** | Assurez-vous que le dossier PNJ existe avec tous les .png |

---

## ⚠️ Notes Importantes

- ✅ **Activité Ciblée :** Activité 7 de GlobalExam (Business > Bâtiment) uniquement
- ✅ **Zoom Navigateur :** Doit être à 100% (normalisé automatiquement au démarrage)
- ✅ **Résolution Écran :** Toute résolution supportée
- ⚠️ **Ne pas changer le zoom ou la résolution** pendant l'exécution

---

## 📝 Licence

Ce projet est fourni à des fins d'automatisation personnelle/éducative. Veuillez respecter les conditions d'utilisation de la plateforme.

---

<div align="center">

**Fait avec ❤️ pour l'automatisation GlobalExam**

🚀 **GlobalExam Endless** - Mode Rapide

</div>
