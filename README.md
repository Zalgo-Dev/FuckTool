# FuckTool 🚀

**FuckTool** est un outil de **pentest Minecraft** avancé permettant :
- d'analyser des serveurs,
- de détecter des failles,
- de simuler des stress-tests réseau.

> 🛡️ **Projet à but éducatif et de sécurité uniquement.** Utilisez FuckTool **seulement sur vos propres serveurs** ou avec une autorisation explicite.

---

## ✨ Fonctionnalités principales

- 🔎 Récupération d'infos serveur Minecraft (version, forge, secure chat, etc.)
- 🛰️ DNS Lookup complet (A, AAAA, MX, TXT...)
- ⚡ Stress-tests avec support L4 / L7
- 📜 Historique des commandes sauvegardé
- 🧠 Autocomplétion dynamique (dropdown)
- 🎨 Interface console stylisée

---

## 🛠️ Installation

```bash
git clone https://github.com/votreprofil/FuckTool.git
cd FuckTool
```

```bash
pip install -r requirements.txt
```

---

## 🚀 Lancer FuckTool

```bash
python fucktool\main.py
```

---

## 📋 Commandes Disponibles (Aperçu du `help`)

```text
┌────────────────────────────────────────────────────────────────────────────────────────────────────┐
│  FuckTool - Command Help                                                                            │
├────────────────────────────────────────────────────────────────────────────────────────────────────┤
│  Server Information:                                                                                │
│  - info <ip:port>             ➜ Get server details (Title, Players, Version, etc.)                  │
│  - details <ip>               ➜ Get advanced server information                                    │
│                                (Geo, Secure Chat, Forge, etc.)                                      │
│                                                                                                    │
│  Network Tools:                                                                                     │
│  - dns <ip|domain>            ➜ Perform DNS lookup and show records                                │
│                                (A, AAAA, MX, TXT, etc.)                                             │
│  - stress <ip:port>           ➜ Advanced network stress tester (500 workers max)                   │
│    --persistent               ➜ Maintains long-lived connections (L4)                              │
│    --minecraft                ➜ MC protocol flood with keep-alives (L7)                            │
│    --http                     ➜ HTTP flood with realistic headers                                 │
│    --duration 60              ➜ Test duration (30-600s, default: 60)                               │
│    Note: Auto-HTTPS on port 443                                                                     │
│                                                                                                    │
│  Utilities:                                                                                         │
│  - clear                      ➜ Clear the screen                                                   │
│  - exit                       ➜ Quit FuckTool                                                      │
└────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 📂 Structure du projet

```bash
FuckTool/
├── fucktool/
│   ├── commands/
│   │   ├── details.py
│   │   ├── dns.py
│   │   ├── handler.py
│   │   ├── help.py
│   │   ├── info.py
│   │   └── stress.py
│   ├── core/
│   │   ├── colors.py
│   │   ├── header.py
│   │   ├── input_manager.py
│   ├── resources/
│   │   ├── fucktool.ico
│   │   └── install.bat
│   ├── __init__.py
│   ├── .fucktool_history
│   └── main.py
├── LICENSE.md
├── README.md
├── requirements.txt
└── main.py
```

---

## ⚙️ Dépendances

- Python 3.8+

---

## ❤️ Auteur

Développé par **ZalgoDev**.  
Spécialisé dans la cybersécurité et la recherche de failles.

---

## ⚠️ Avertissement

> FuckTool est destiné **exclusivement** à un usage **éthique** et **autorisé**.  
> Utiliser cet outil sans permission explicite est **illégal** et vous expose à des poursuites.

---
