# Guide Agent – Projet `youtubeauto`

## 📚 Présentation

`youtubeauto` est un outil automatisé de génération de contenu YouTube. Il combine :
- une interface Streamlit interactive
- des modules Python pour la génération, le téléchargement, la découpe et la transcription de vidéos
- l’API OpenAI pour produire titres, scripts et descriptions optimisés

---

## 📁 Structure du projet

- `main.py` – script principal (backend)
- `interface/` – interface utilisateur Streamlit
  - `control_center.py` – point d’entrée Streamlit
  - `ui/` – onglets : prompts, TikTok, etc.
- `generators/youtube/` – logique de traitement vidéo : download, slice, transcribe, etc.
- `configgpt/` – configuration des modèles GPT
- `tests/` – tests manuels pour les modules principaux
- `requirements.txt` – dépendances Python
- `setup.sh` – installation rapide
- `.env` – variables sensibles
- `custom_prompts.json` – prompts personnalisés
- `fonts/`, `cookies/` – ressources diverses

---

## ▶️ Lancer le projet

```bash
# 1. Installer les dépendances
bash setup.sh

# 2. Lancer l’interface (Streamlit)
streamlit run interface/control_center.py

# 3. Exécuter manuellement un script (optionnel)
python main.py
```

---

## 🧪 Tests

Les tests manuels se trouvent dans `tests/`. Ils couvrent :

- `compose_clip` (test_composer.py)
- `generate_caption` (test_description.py)
- `download` (test_downloader.py)
- `slice_video` (test_slicer.py)
- `transcribe` (test_transcriber.py)

💡 À noter :
- Ce sont des scripts d’intégration, non des tests unitaires classiques
- Utilisent `print()` pour valider le résultat
- Ne s’exécutent pas via `pytest` ou `unittest` (pour l’instant)

---

## 🧹 Linting & Formatage

```bash
black .
flake8 .
```

---

## 🧠 Directives pour Codex

- L’interface utilisateur se trouve dans `interface/`
- Les tâches principales de traitement sont dans `generators/youtube/`
- Toute fonctionnalité ajoutée doit être testable manuellement via les scripts de `tests/`
- Ne jamais exposer le contenu de `.env` ou `cookies/`
- Suivre les conventions de formatage (black) et de qualité (flake8)

---

## 💡 Exemples de tâches à déléguer à Codex

```text
Ajoute un bouton dans prompt_editor_tab.py pour réinitialiser les prompts personnalisés.
```

```text
Corrige les erreurs potentielles quand download échoue (par exemple, lien invalide).
```

```text
Crée un test `unittest` standard pour le module transcriber.
```

```text
Ajoute un champ pour choisir la langue de la vidéo dans control_center.py.
```

---

## 🛠️ Format de commit / PR

```
[youtubeauto] <Résumé clair de la modification>

- Ce qui a été modifié
- Comment tester
```
