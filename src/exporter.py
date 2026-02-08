# exporter.py
import json
from datetime import datetime
import os

def export_report(report, packets):
    os.makedirs("exports", exist_ok=True)

    filename = f"exports/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    with open(filename, "w") as f:
        json.dump({
            "report": report,
            "packets": packets
        }, f, indent=2)

    return filename
