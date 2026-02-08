# Local Network Threat Monitor

A simple Python tool that sniffs live network traffic, analyzes it, detects unusual behavior, and generates a clear network security report.

Built as a learning + practical project for networking and cybersecurity.

---

## 🚀 What it does

- Captures live packets on your local network
- Displays packets in real time (source → destination, protocol, size)
- Analyzes traffic after capture
- Detects basic anomalies (example: high UDP traffic)
- Calculates a **risk score**
- Exports all packets + analysis report to a JSON file

---

## 📡 Live packet example
```
[LIVE] 192.168.1.3 → 46.232.210.48 | UDP | 146B

[LIVE] 172.64.148.235 → 192.168.1.3 | TCP | 54B
```


---

## 🛡 Sample security report
```
Total Packets: 182

Risk Level : LOW

Risk Score : 0/100

Detected Anomalies: None
```

---

## 📦 Requirements

- Python 3.8+
- Run as **Administrator** (Windows) or **sudo** (Linux/macOS)
- Python libraries:
  - `scapy`
  - `colorama`

---

## ⚙ Installation & Usage

```
git clone https://github.com/kathir-IL80085/local-network-threat-monitor.git
cd Local-Network-Threat-Monitor
pip install -r requirements.txt
python src/main.py
```
---

## What happens when you run it:

- Live packets are captured and shown in the terminal

- Traffic is analyzed automatically

- A network security report is printed

- Full data is exported to the exports/ folder

---

## 🗂 Project Structure

Local-Network-Threat-Monitor/

│

├── src/

│   ├── main.py        # Entry point

│   ├── capture.py     # Live packet sniffing

│   ├── analyzer.py    # Traffic analysis

│   ├── anomaly.py     # Anomaly detection logic

│   ├── report.py      # Report generation

│   └── exporter.py    # JSON export

│

├── exports/            # Generated reports

├── requirements.txt

└── README.md


---


## 🎯 Who this is for
- Cybersecurity students

- Networking learners

- Anyone curious about what actually runs on their local network
  

---  


## ⚠ Notes
High UDP traffic is often normal (video streaming, QUIC, calls)

This is a monitoring / defensive tool, not an attack tool


---


## 📜 Disclaimer
Use this tool only on networks you own or have permission to monitor.


---


## 👤 Author
Kathiresh

If you find this useful, feel free to ⭐ the repository.

