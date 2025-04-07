# Intrusion Detection System (IDS) - Windows Version

This is a simple Intrusion Detection System using raw sockets and Python. It captures packets, detects SYN scans, applies firewall rules to block suspicious IPs, and uses a machine learning model for anomaly detection.

## ✅ Features

- Real-time packet sniffing (Raw Sockets)
- SYN scan detection
- ML-based anomaly detection using Isolation Forest
- IP blocking using Windows Firewall
- GUI log viewer
- Daily intrusion report generation
- Logs packet features for future ML training

## 🔧 Requirements

- Python 3.8+
- Run VS Code as Administrator
- Install dependencies:

```bash
pip install pandas scikit-learn
