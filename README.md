🔐 Intrusion Detection System (IDS) — Project Summary
This project is a secure, modular, and extensible intrusion detection system designed to monitor incoming alerts from multiple clients over SSL-encrypted sockets. It provides both a desktop GUI (built using Tkinter) and a real-time web dashboard for visualization and interaction. The system uses a SQLite database to classify threat patterns and severities and offers tools to simulate, monitor, and react to network-based threats.

🧠 Main Components
secure_server.py

Acts as the central server that listens for incoming client alerts.

Uses SSL encryption to ensure secure communication.

Writes incoming logs to logs.txt.

secure_client.py

Sends alert messages to the server over an encrypted SSL connection.

Can be replaced or extended by any network client.

auto_logger.py

Simulates real-time alert generation.

Sends periodic random threat alerts to test the system.

dashboard.py (Tkinter GUI)

Monitors and visualizes alerts in real-time.

Displays:

Live logs.

Charts for threat frequency.

Pop-up alerts for high-severity threats.

Options to add new threats and severities on the fly.

web_dashboard (Flask + Socket.IO)

Displays threat logs and charts on a browser in real-time.

Allows remote access and monitoring.

Supports dynamic updates from the same server log file.

threat_db.py / init_db.py

Manages the threat classification database (threats.db).

Allows inserting and modifying known threats with severity levels.

log_parser.py

Parses logs.txt to identify and classify alerts based on stored patterns.

Used by both GUI and Web Dashboard.

cert.pem / key.pem

SSL certificate and private key used to encrypt client-server communication.

🚀 How It Works
Client connects to the SSL server and sends threat alerts.

The server logs each alert in logs.txt.

Both the Tkinter GUI and the web dashboard:

Read and parse logs in real time.

Match messages with patterns from the database.

Display them visually, with charts and popup alerts.

Admin can add/edit threat patterns through the GUI or web interface.

💡 Key Features
✅ Real-time threat detection.

✅ Secure (SSL) client-server communication.

✅ Unlimited client support.

✅ Parallel control and data channels.

✅ Auto logging & simulation tool.

✅ Editable threat classifications.

✅ Interactive GUI and web dashboard.

✅ Modular & extensible design.


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



