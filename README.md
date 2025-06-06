# 🎬 youtubeauto

**youtubeauto** est un pipeline complet pour transformer automatiquement des vidéos YouTube en contenus courts, optimisés pour TikTok. Il s'appuie sur des outils comme Whisper pour la transcription, MoviePy pour le montage, et OpenAI pour la génération de descriptions et hooks percutants.

---

## 🔧 Fonctionnalités principales

- 📥 Téléchargement automatique de vidéos YouTube (`yt_dlp`)
- 📝 Transcription via le modèle Whisper
- ✂️ Découpage intelligent en clips (durée aléatoire ou paramétrée)
- 💬 Génération de hooks et captions TikTok via l'API OpenAI
- 🎨 Composition vidéo verticale avec fond et overlay texte
- 🖥️ Interface utilisateur interactive via Streamlit

---

## 🗃️ Architecture du projet

```
.
├── main.py                       # Pipeline principal
├── generators/
│   └── youtube/
│       ├── downloader.py        # Télécharge les vidéos
│       ├── transcriber.py       # Transcrit l'audio
│       ├── slicer.py            # Découpe les vidéos en segments
│       ├── composer.py          # Assemble les clips avec overlay texte
│       └── description_generator.py # Gère les hooks & captions TikTok
│
├── interface/
│   ├── control_center.py        # Lancement Streamlit
│   └── ui/
│       ├── youtube_to_tiktok_tab.py # UI pour pipeline principal
│       └── prompt_editor_tab.py     # UI pour éditer les prompts IA
│
├── utils/                       # Fonctions utilitaires (logs, prompts, etc.)
├── fonts/                       # Polices personnalisées
├── cookies/                     # Fichier cookies pour YouTube
├── series/                      # Sorties par projet (vidéos, hooks, transcripts…)
└── videos/exports/              # Clips finaux exportés
```

---

## ⚙️ Installation

1. **Cloner le projet :**
   ```bash
   git clone https://github.com/tonprofil/youtubeauto.git
   cd youtubeauto
   ```

2. **Environnement virtuel (optionnel) :**
   ```bash
   python -m venv venv
   source venv/bin/activate  # (Windows : venv\Scripts\activate)
   ```

3. **Installer les dépendances :**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurer `.env` avec ta clé OpenAI (et autres paramètres optionnels) :**
   ```
   OPENAI_API_KEY=sk-...
   HOOK_GPT_MODEL=gpt-3.5-turbo
   WHISPER_MODEL=small
   ```

---

## 🚀 Utilisation en ligne de commande

```bash
python main.py "https://www.youtube.com/watch?v=RLbUjVb0DS4" yt_monprojet
```

---

## 🖥️ Interface Utilisateur (Streamlit)

```bash
streamlit run interface/control_center.py
```

---

## 🧠 Customisation IA

Édite `custom_prompts.json` pour personnaliser les hooks et captions.

---

## 📁 Sorties

- `series/<slug>/parts/` : clips découpés
- `series/<slug>/hooks/` : hooks générés
- `videos/exports/<slug>/` : clips finaux exportés

---

## 🧩 Dépendances principales

- yt_dlp
- openai
- moviepy
- whisper
- streamlit

---

## 📄 Licence

À définir selon ton choix (MIT, GPL, etc.)

---

## 📬 Contact

Auteur : [Ton nom ici]  
Twitter : [@tonhandle]  
Email : [ton@email.com]
