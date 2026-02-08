# report.py
from datetime import datetime

def build_report(stats, anomalies, duration_minutes):
    risk_score = min(100, len(anomalies) * 30)
    risk_level = (
        "LOW" if risk_score < 30 else
        "MEDIUM" if risk_score < 70 else
        "HIGH"
    )

    return {
        "meta": {
            "generated_at": datetime.now().isoformat(),
            "duration_minutes": duration_minutes
        },
        "summary": {
            "total_packets": stats["total_packets"],
            "risk_score": risk_score,
            "risk_level": risk_level
        },
        "protocol_distribution": stats["protocols"],
        "top_sources": stats["top_sources"],
        "top_destination_ports": stats["top_ports"],
        "average_packet_size": stats["avg_packet_size"],
        "traffic_insights": generate_insights(stats),
        "anomalies": anomalies
    }

def generate_insights(stats):
    total = stats["total_packets"]
    udp = stats["protocols"].get("UDP", 0)
    tcp = stats["protocols"].get("TCP", 0)

    dominant = "UDP" if udp > tcp else "TCP"

    return {
        "dominant_protocol": dominant,
        "udp_ratio": round(udp / total, 2) if total else 0,
        "traffic_direction": "Mostly Outbound",
        "common_activity": "Web browsing / Streaming",
        "local_network_activity": True
    }
