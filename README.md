# Smart SNMP-Based Network Monitoring with AI Alerts

A beginner-friendly Python starter project for a network-monitoring dashboard and
machine-learning anomaly detection. It is suitable as a learning/demo repository
for an AI automation portfolio.

## Features

- Flask web dashboard
- Network-style metrics: CPU, memory, traffic, and packet loss
- Scikit-learn Isolation Forest anomaly detection
- Potential anomaly message on the dashboard
- Simulated metric spikes for demonstration

## Important limitation

**This version uses simulated metrics; it does not yet poll real SNMP devices or send email/SMS alerts.**
Do not describe it as a production-ready SNMP monitoring system. Real SNMP polling
requires an authorized device, its IP address, SNMP version, and secure credentials,
plus implementation and testing of the appropriate OIDs.

## Requirements

- Python 3.10 or newer
- pip

## Run on Windows

1. Download or clone this repository.
2. Open PowerShell or Command Prompt in the project folder.
3. Create a virtual environment:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks activation, use Command Prompt and run:
   `.\.venv\Scripts\activate.bat`

4. Install dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

5. Start the dashboard:

   ```powershell
   python app.py
   ```

6. Open `http://127.0.0.1:5000` in your browser. Refresh to generate a new demo sample.

## Project structure

```text
smart-snmp-ai-monitoring/
├── app.py
├── monitor.py
├── requirements.txt
└── README.md
```

## Suggested next improvements

- Replace simulated metrics with SNMP polling against authorized lab equipment.
- Store timestamped metrics in SQLite or another database.
- Train and evaluate the anomaly model on collected baseline data.
- Add email/Slack alerts using environment variables for credentials.
- Add tests, logging, and a deployment guide.

## Portfolio description

Built a Python/Flask network-monitoring demo that visualizes simulated infrastructure
metrics and uses Scikit-learn Isolation Forest to flag unusual metric patterns.
The project demonstrates a starting point for AI-assisted monitoring and alert workflows.
