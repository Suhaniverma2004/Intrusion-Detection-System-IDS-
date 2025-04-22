🔐 Intrusion Detection System (IDS) — Project Summary
📌 Overview
This project is a multi-client, SSL-secured Intrusion Detection System with a real-time GUI dashboard. It detects suspicious patterns in network logs, classifies threats, visualizes data using charts, and supports alert popups and auto logging.

🧠 Key Features
✅ Multi-client architecture: Supports any number of clients sending alerts.

🔐 SSL Encryption: Uses TLS to secure communication between clients and server.

🖥 Interactive GUI: Real-time logs, threat charts, and alert popups.

📊 Threat Classification: Categorizes threats (e.g., attack, scan, malicious) with severity levels.

➕ Dynamic Threat Management: Threat patterns and severities stored in a SQLite DB and easily modifiable.

⚙️ Auto Logging Module: Simulates live threats for testing and demos.

💡 No Code Recompilation Required: Adding new clients or modifying threats does not require recompiling code.

🧱 Tech Stack
Python: Core implementation

Socket Programming: Secure client-server architecture

SSL/TLS: For encrypted transmission

SQLite3: Threat classification database

Tkinter: GUI dashboard

Matplotlib: Real-time threat charts

PyInstaller: Converts Python GUI to standalone .exe

🧩 Modules

Module	Description
secure_server.py	SSL-enabled server receiving alerts from clients
secure_client.py	Sends simulated alerts securely to the server
auto_logger.py	Randomly logs threat events for testing
dashboard.py	GUI interface showing logs, charts, and popups
threat_db.py	Manages threat patterns and severities via SQLite
init_db.py	Initializes the threat classification database
log_parser.py	Parses logs and counts threat frequency
🚀 How It Works
Clients send alerts to the SSL server.

Server logs them in logs.txt.

GUI Dashboard reads logs, classifies threats, and displays:

Realtime logs

Bar charts for frequency

Pop-up alerts for high-severity threats

Database stores threat patterns and severity dynamically.

📦 Deployment Options
✅ Run in VS Code (Python)

✅ Build as .exe desktop app (with PyInstaller)

✅ Modular & extensible: New clients and threats can be added easily

