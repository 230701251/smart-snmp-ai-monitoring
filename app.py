from flask import Flask, render_template_string
from monitor import collect_metrics, detect_anomalies

app = Flask(__name__)

PAGE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Smart SNMP Monitoring with AI Alerts</title>
  <style>
    body{font-family:Arial,sans-serif;max-width:1000px;margin:32px auto;padding:0 16px;background:#f5f7fb;color:#172033}
    h1{color:#183b66}.note{background:#fff8df;padding:12px;border-left:4px solid #e0ad27}
    .grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:12px}
    .card{background:white;border-radius:10px;padding:16px;box-shadow:0 2px 8px #0001}
    .value{font-size:26px;font-weight:bold;margin-top:8px}.ok{color:#167647}.warn{color:#b42318}
    table{width:100%;border-collapse:collapse;background:white;margin-top:20px}
    th,td{text-align:left;padding:10px;border-bottom:1px solid #e6e8ee}
    th{background:#eaf0f8}
  </style>
</head>
<body>
  <h1>Smart SNMP Monitoring with AI Alerts</h1>
  <p>Starter dashboard for network-metric monitoring and anomaly detection.</p>
  <div class="note"><b>Demo mode:</b> the metrics below are simulated. This starter does not yet poll a real network device.</div>
  <div class="grid">
    <div class="card">CPU usage<div class="value">{{ metrics.cpu }}%</div></div>
    <div class="card">Memory usage<div class="value">{{ metrics.memory }}%</div></div>
    <div class="card">Network traffic<div class="value">{{ metrics.traffic }} Mbps</div></div>
    <div class="card">Packet loss<div class="value">{{ metrics.packet_loss }}%</div></div>
  </div>
  <h2>AI anomaly result</h2>
  <div class="card">
    {% if anomaly %}
      <div class="value warn">Potential anomaly detected</div>
      <p>{{ explanation }}</p>
    {% else %}
      <div class="value ok">No anomaly detected</div>
      <p>The current demo sample is within the model's expected range.</p>
    {% endif %}
  </div>
  <h2>Metric snapshot</h2>
  <table><tr><th>Metric</th><th>Value</th></tr>
    {% for key, value in metrics.items() %}<tr><td>{{ key.replace('_',' ').title() }}</td><td>{{ value }}</td></tr>{% endfor %}
  </table>
  <p><small>Refresh the page to generate a new demo sample. For real deployment, configure SNMP polling and secure alert delivery.</small></p>
</body></html>
"""

@app.route("/")
def dashboard():
    metrics = collect_metrics()
    anomaly, explanation = detect_anomalies(metrics)
    return render_template_string(PAGE, metrics=metrics, anomaly=anomaly, explanation=explanation)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
