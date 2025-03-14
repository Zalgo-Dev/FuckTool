# 🔥 MCPFuckTool - Minecraft Pentesting Tool
[![Licence](https://img.shields.io/badge/Licence-Propri%C3%A9taire-red.svg)](LICENSE)  
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)  

## 🚀 **Overview**
MCPFuckTool is an **advanced pentesting tool** for Minecraft, allowing you to analyze, scan, and interact with servers.  
Ideal for administrators and security researchers who want to **test the robustness of their server protections**.  

⚠ **This project is intended for legal use only.**

---

## 🛠 **Features**
✅ **Server analysis** with `info <ip:port>` and `details <ip>`   
✅ **Clear and colorful display** for better readability  
✅ **Modular architecture** for flexible development  
✅ **Automatic update system (coming soon)**  

---

## 📂 **Project Structure**
```
MCPFuckTool/
│── main.py                   # 🎯 Main terminal
│── commands/                 # ⌨️ Folder containing all commands
│   ├── __init__.py           # 📌 Initializes commands
│   ├── commands_handler.py   # 🛠 Command handler
│   ├── infoCommand.py        # 🌍 `info` command
│   ├── detailsCommand.py     # 🔎 `details` command
│   ├── helpCommand.py        # ❓ `help` command
│── modules/                  # 📂 Folder containing general modules
│   ├── __init__.py           # 📌 Initializes modules
│   ├── colorsModule.py       # 🎨 ANSI color management
│   ├── headerModule.py       # 🏠 Header display
│   ├── utilsModule.py        # 🛠 Utility functions
│── requirements.txt          # 📦 Dependency list
│── README.md                 # 📖 Documentation
│── LICENSE                   # 📜 Proprietary License
```

---

## 🔧 **Installation**
### **1️⃣ Prerequisites**
- **Python 3.8+** must be installed. Check with:
  ```bash
  python --version
  ```

### **2️⃣ Install dependencies**
Clone the repo and install the dependencies:
```bash
git clone https://github.com/Zalgo-Dev/MCPFuckTool.git
cd MCPFuckTool
pip install -r requirements.txt
```

### **3️⃣ Run**
```bash
python main.py
```

---

## 📜 **Available Commands**
| 🏷 Command | 🎯 Description |
|------------|--------------|
| `help`     | Displays the list of commands |
| `info <ip:port>` | Shows server info |
| `details <ip>` | Provides advanced details about a server |
| `clear`    | Clears the screen |
| `exit`     | Exits MCPFuckTool |

💡 **Example:**  
```bash
info play.hypixel.net
```

---

## 📜 **License**
⚠️ **MCPFuckTool is under a STRICT PROPRIETARY LICENSE.**  
❌ **No modification, redistribution, or code reuse is allowed.**  
✅ **Contributions are accepted only with the author's validation.**  

🔹 See the full license details in [LICENSE](LICENSE.md).

---

## 👤 **Author**
- **ZalgoDev** - [GitHub](https://github.com/Zalgo-Dev) | [Twitter](https://x.com/ZalgoDev)

---

## 💡 **Disclaimer**
This project is intended for **educational and legal use only**.  
Misuse may **violate Minecraft server TOS** and **lead to penalties**.  

```
❌ Never test a server without the explicit authorization of its owner.
✔ Use this tool to improve server security.
```

---

## 🛠 **Upcoming Improvements**
- Add an **automatic update system**
- Add **exploits**
- Implement **advanced scanning tools**

---

### 🎯 **MCPFuckTool is ready to use!**  
🔥 **Clone, test, and secure your Minecraft servers now!**  
If you have suggestions, **open an issue on GitHub**. 🚀  
