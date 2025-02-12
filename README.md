# 🔥 MCPFuckTool - Advanced Minecraft Pentesting Tool  
[![Licence](https://img.shields.io/badge/Licence-Propri%C3%A9taire-red.svg)](LICENSE)  
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)  

## 🚀 **Présentation**
MCPFuckTool est un **outil avancé de pentesting** pour Minecraft, permettant d’analyser, scanner et interagir avec des serveurs.  
Idéal pour les administrateurs et chercheurs en sécurité souhaitant **tester la robustesse des protections** de leur serveur Minecraft.  

⚠ **Ce projet est destiné à un usage légal uniquement.**

---

## 🛠 **Fonctionnalités**
✅ **Analyse des serveurs** avec `info <ip:port>` et `details <ip>`   
✅ **Affichage clair et coloré** pour une meilleure lisibilité  
✅ **Architecture modulaire** pour un développement flexible  
✅ **Système de mise à jour automatique (bientôt disponible)**  

---

## 📂 **Structure du projet**
```
MCPFuckTool/
│── main.py            # 🎯 Terminal principal
│── commands/          # ⌨️ Dossier contenant toutes les commandes
│   ├── __init__.py    # 📌 Initialise les commandes
│   ├── info.py        # 🌍 Commande `info` et `details`
│   ├── scan.py        # 🔎 Commande `scan`
│   ├── exploits.py    # 💥 Commande `exploit`
│── modules/           # 📂 Dossier contenant les modules généraux
│   ├── __init__.py    # 📌 Initialise les modules
│   ├── colors.py      # 🎨 Gestion des couleurs ANSI
│   ├── header.py      # 🏠 Affichage du header
│   ├── utils.py       # 🛠 Fonctions utilitaires
│── requirements.txt   # 📦 Liste des dépendances
│── README.md          # 📖 Documentation
│── LICENSE            # 📜 Licence Propriétaire
```

---

## 🔧 **Installation**
### **1️⃣ Pré-requis**
- **Python 3.8+** doit être installé. Vérifie avec :
  ```bash
  python --version
  ```

### **2️⃣ Installation des dépendances**
Clone le repo et installe les dépendances :
```bash
git clone https://github.com/Zalgo-Dev/MCPFuckTool.git
cd MCPFuckTool
pip install -r requirements.txt
```

### **3️⃣ Lancement**
```bash
python main.py
```

---

## 📜 **Commandes disponibles**
| 🏷 Commande | 🎯 Description |
|------------|--------------|
| `help`     | Affiche la liste des commandes |
| `info <ip:port>` | Affiche les infos d'un serveur |
| `details <ip>` | Donne des détails avancés sur un serveur |
| `clear`    | Efface l'écran |
| `exit`     | Quitte MCPFuckTool |

💡 **Exemple :**  
```bash
info play.hypixel.net
```

---

## 📜 **Licence**
⚠️ **MCPFuckTool est sous une licence PROPRIÉTAIRE STRICTE.**  
❌ **Aucune modification, redistribution ou réutilisation du code n'est autorisée.**  
✅ **Les contributions sont acceptées uniquement sur validation de l'auteur.**  

🔹 Voir les détails complets de la licence dans [LICENSE](LICENSE.md).

---

## 👤 **Auteur**
- **ZalgoDev** - [GitHub](https://github.com/Zalgo-Dev) | [Twitter](https://x.com/ZalgoDev)

---

## 💡 **Avertissement**
Ce projet est destiné à un **usage éducatif et légal** uniquement.  
L'utilisation abusive peut **violer les CGU des serveurs Minecraft** et **entraîner des sanctions**.  

```
❌ Ne jamais tester un serveur sans l'autorisation explicite de son propriétaire.
✔ Utilisez cet outil pour améliorer la sécurité des serveurs.
```

---

## 🛠 **Prochaines améliorations**
- Ajouter un **système de mise à jour automatique**
- Ajout des **exploits**
- Ajouter des **outils de scan avancés**

---

### 🎯 **MCPFuckTool est prêt à l'emploi !**  
🔥 **Clone, teste, et sécurise tes serveurs Minecraft dès maintenant !**  
Si tu as des suggestions, **ouvre une issue sur GitHub**. 🚀  
