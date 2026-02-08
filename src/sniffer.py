from collections import defaultdict
from datetime import datetime
from scapy.all import IP, TCP, UDP
from capture import capture_packets

def run_sniffer(duration, show_live=True):
    stats = {
        "total": 0,
        "protocols": defaultdict(int),
        "src_ips": defaultdict(int),
        "dst_ports": defaultdict(int),
        "sizes": [],
        "samples": []
    }

    def handle_packet(pkt):
        if IP not in pkt:
            return

        ip = pkt[IP]
        proto = "OTHER"
        sport, dport = None, None

        if TCP in pkt:
            proto = "TCP"
            sport, dport = pkt[TCP].sport, pkt[TCP].dport
        elif UDP in pkt:
            proto = "UDP"
            sport, dport = pkt[UDP].sport, pkt[UDP].dport

        size = len(pkt)

        stats["total"] += 1
        stats["protocols"][proto] += 1
        stats["src_ips"][ip.src] += 1
        if dport:
            stats["dst_ports"][dport] += 1
        stats["sizes"].append(size)

        if len(stats["samples"]) < 10:
            stats["samples"].append(
                f"[{datetime.now().strftime('%H:%M:%S')}] "
                f"{ip.src}:{sport} → {ip.dst}:{dport} | {proto} | {size}B"
            )

        if show_live and stats["total"] % 10 == 0:
            print(f"[LIVE] {ip.src} → {ip.dst} | {proto} | {size}B")

    capture_packets(duration, handle_packet)
    return stats
