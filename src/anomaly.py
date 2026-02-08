# anomaly.py
def detect_anomalies(stats):
    anomalies = []

    total = stats["total_packets"]
    udp_count = stats["protocols"].get("UDP", 0)

    if total > 0 and udp_count / total > 0.7:
        anomalies.append({
            "type": "High UDP Traffic",
            "reason": f"UDP ratio {udp_count/total:.2f}",
            "likely_cause": "Streaming, QUIC, or flooding"
        })

    return anomalies
