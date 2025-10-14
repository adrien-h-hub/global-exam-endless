# 5Endless – Automatisation GlobalExam (Activité 7 / Business > Bâtiment)

![5Endless](assets/5endless_logo.svg)

Ce dépôt contient le script Python « mode rapide » (sans pause) qui automatise les questions de l’**activité 7** de la section **Business > Bâtiment** sur GlobalExam. Il ne fonctionne que pour cette activité.

## Prérequis

- Windows
- Python 3.13 (exemples ci-dessous utilisent ce chemin)
- Résolution et zoom stables (les coordonnées dépendent de l’affichage)

## Installation

1. Cloner ou télécharger ce dépôt.
2. Installer les dépendances:
   ```powershell
   & "C:\Users\Dardq\AppData\Local\Programs\Python\Python313\python.exe" -m pip install -r requirements.txt
   ```
3. Placer les images nécessaires (ex: `PNJ/…`, `Q7_answer.png`, etc.) dans les dossiers `PNJ/` et/ou `assets/`.

## Première exécution (code masqué)

Au premier lancement, un **code à usage unique** est demandé dans la console. La saisie est **masquée**.

- Code: `602172`
- Un fichier `.first_run_ok` est créé après succès pour ne plus redemander le code.
- Pour réactiver le prompt: supprimer `.first_run_ok`.

## Utilisation

### Mode rapide (sans pause)
```powershell
& "C:\Users\Dardq\AppData\Local\Programs\Python\Python313\python.exe" 5endless_final.py
```

## Notes

- Un léger délai est ajouté après chaque clic pour éviter les sauts de question si le site est lent.
- Mélange **reconnaissance d’images + coordonnées de secours**.
- Cible uniquement l’**activité 7** (Business > Bâtiment).

## Dépannage

- Si une question est sautée, augmentez le délai dans `click_button()`.
- Si une image n’est pas reconnue, vérifiez la présence du `.png` et que la fenêtre du navigateur est active.
