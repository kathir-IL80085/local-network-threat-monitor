# analyzer.py
from collections import Counter

def analyze_packets(packets):
    protocols = Counter()
    src_ips = Counter()
    dst_ports = Counter()
    total_size = 0

    for pkt in packets:
        protocols[pkt["protocol"]] += 1
        src_ips[pkt["src_ip"]] += 1
        if pkt["dst_port"]:
            dst_ports[pkt["dst_port"]] += 1
        total_size += pkt["size"]

    avg_size = total_size / len(packets) if packets else 0

    return {
        "total_packets": len(packets),
        "protocols": dict(protocols),
        "top_sources": src_ips.most_common(5),
        "top_ports": dst_ports.most_common(5),
        "avg_packet_size": avg_size
    }
