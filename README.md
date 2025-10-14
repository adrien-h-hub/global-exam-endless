<p align="center">
  <img src="assets/5endless_logo.svg" alt="Endless - Mode rapide" height="72"/>
</p>

<p align="center">
  <strong>Automatisation GlobalExam – Activité 7 (Business > Bâtiment)</strong><br/>
  <em>Mode rapide, sans pause – optimisé avec délais anti-sauts et reconnaissance d’images</em>
</p>

<p align="center">
  <a href="#prerequis"><img src="https://img.shields.io/badge/OS-Windows-blue" alt="Windows"/></a>
  <a href="#installation"><img src="https://img.shields.io/badge/Python-3.13-3776AB" alt="Python 3.13"/></a>
  <a href="#perimetre"><img src="https://img.shields.io/badge/Portee-Activit%C3%A9%207%20Business%2FB%C3%A2timent-orange" alt="Scope"/></a>
  <a href="#licence"><img src="https://img.shields.io/badge/License-Private-lightgrey" alt="License"/></a>
</p>

---

## Sommaire

- [Périmètre](#perimetre)
- [Fonctionnalités](#fonctionnalites)
- [Prérequis](#prerequis)
- [Installation](#installation)
- [Première exécution (code masqué)](#premiere-execution-code-masque)
- [Utilisation](#utilisation)
- [Configuration & Assets](#configuration--assets)
- [Dépannage](#depannage)
- [FAQ](#faq)
- [Feuille de route](#feuille-de-route)
- [Contribuer](#contribuer)
- [Licence](#licence)
- [Avertissement](#avertissement)
- [Contact](#contact)

## Périmètre

- **Uniquement** pour l’**activité 7** de la partie **Business > Bâtiment** sur GlobalExam.
- Non garanti pour d’autres activités ou résolutions.

## Fonctionnalités

- **Mode rapide**: enchaîne les questions sans pause intermédiaire.
- **Délai post-clic**: réduit les sauts de question sur site lent.
- **Reconnaissance d’images** avec **coordonnées de secours**.
- **Relance en boucle** de l’activité (« Rejouer l’activité »).
- **Code d’accès masqué** au premier lancement (anti-mauvaise utilisation).

## Prérequis

- **Windows**
- **Python 3.13**
- **Affichage stable** (résolution/zoom constants)

## Installation

1. Cloner ou télécharger ce dépôt.
2. Installer les dépendances:
   ```powershell
   & "C:\Users\Dardq\AppData\Local\Programs\Python\Python313\python.exe" -m pip install -r requirements.txt
   ```

## Première exécution (code masqué)

Lors du premier lancement, un **code à usage unique** est demandé dans la console. La saisie est **masquée**. Ne publiez jamais ce code.

- Après une saisie correcte, un fichier `.first_run_ok` est créé afin de ne plus redemander le code aux exécutions suivantes.
- Pour réactiver le prompt, supprimez le fichier `.first_run_ok`.

## Utilisation

Exécuter depuis PowerShell (Windows):

```powershell
& "C:\Users\Dardq\AppData\Local\Programs\Python\Python313\python.exe" 5endless_final.py
```

Arrêt: `Ctrl + C` dans la console.

## Configuration & Assets

- **Dossier images**: `PNJ/` (inclus dans le dépôt, à remplir avec vos `.png`).
- **Logo**: `assets/5endless_logo.svg`.
- **Ajuster les délais**: ouvrez `5endless_final.py` et modifiez la valeur par défaut de `click_button(delay=0.8)`.
- **Chemin Python**: si besoin, remplacez par votre chemin local.

Arborescence minimale:

```
.
├─ 5endless_final.py
├─ final_test.py
├─ requirements.txt
├─ .gitignore
├─ assets/
│  └─ 5endless_logo.svg
└─ PNJ/
   └─ ... (vos images)
```

## Dépannage

- **Sauts de question**: augmentez légèrement `delay` dans `click_button()` (ex: 1.2s).
- **Image non trouvée**: vérifiez que le `.png` existe et que la **fenêtre navigateur est active**.
- **Mauvais zoom**: restaurez le zoom par défaut du navigateur.
- **Multiples écrans**: essayez en écran unique.

## FAQ

- **Q: Puis-je l’utiliser pour d’autres activités ?**
  - R: Non, uniquement pour l’**activité 7 (Business > Bâtiment)**.
- **Q: Comment réinitialiser le code masqué ?**
  - R: Supprimez `.first_run_ok`.
- **Q: Peut-on ajuster la sensibilité d’image ?**
  - R: Oui, modifiez la `confidence` dans les appels `click_image()` si nécessaire.

## Feuille de route


## Contribuer

- Ouvrez une **issue** pour tout bug ou suggestion.
- Proposez une **PR** avec une description claire et des captures si possible.

## Licence

Usage **privé**. Contactez le mainteneur pour une autre licence.

## Avertissement

Projet à visée personnelle/éducative. Respectez les conditions d’utilisation de la plateforme GlobalExam.

## Contact

- Mainteneur: propriétaire de ce dépôt.
