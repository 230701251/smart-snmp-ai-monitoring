"""Demo network metric generator and AI anomaly detector.

Metrics are simulated for demonstration. This module does not contact real
network equipment. Replace collect_metrics() with an approved SNMP polling
implementation before using it on a real network.
"""
import random
from sklearn.ensemble import IsolationForest

def collect_metrics():
    """Return one simulated network metric sample."""
    # Rare spikes demonstrate how the anomaly detector behaves.
    if random.random() < 0.12:
        return {
            "cpu": random.randint(90, 100),
            "memory": random.randint(85, 100),
            "traffic": random.randint(850, 1200),
            "packet_loss": round(random.uniform(5, 15), 2),
        }
    return {
        "cpu": random.randint(10, 75),
        "memory": random.randint(25, 80),
        "traffic": random.randint(20, 650),
        "packet_loss": round(random.uniform(0, 2), 2),
    }

def detect_anomalies(current):
    """Train a small demo model on baseline samples and score current metrics."""
    baseline = []
    for _ in range(250):
        baseline.append([
            random.randint(10, 75),
            random.randint(25, 80),
            random.randint(20, 650),
            random.uniform(0, 2),
        ])

    model = IsolationForest(contamination=0.08, random_state=42)
    model.fit(baseline)
    row = [[current["cpu"], current["memory"], current["traffic"], current["packet_loss"]]]
    is_anomaly = model.predict(row)[0] == -1

    if is_anomaly:
        explanation = (
            f"CPU {current['cpu']}%, memory {current['memory']}%, "
            f"traffic {current['traffic']} Mbps, packet loss {current['packet_loss']}%."
        )
    else:
        explanation = "The current sample looks similar to the generated baseline."
    return is_anomaly, explanation
