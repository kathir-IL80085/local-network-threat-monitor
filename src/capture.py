# capture.py
from scapy.all import sniff, IP, TCP, UDP
from datetime import datetime

def capture_packets(duration_seconds, live_callback=None):
    packets = []

    def handle_packet(pkt):
        if IP not in pkt:
            return

        proto = "OTHER"
        src_port = dst_port = None

        if TCP in pkt:
            proto = "TCP"
            src_port = pkt[TCP].sport
            dst_port = pkt[TCP].dport
        elif UDP in pkt:
            proto = "UDP"
            src_port = pkt[UDP].sport
            dst_port = pkt[UDP].dport

        packet_data = {
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "src_ip": pkt[IP].src,
            "dst_ip": pkt[IP].dst,
            "src_port": src_port,
            "dst_port": dst_port,
            "protocol": proto,
            "size": len(pkt)
        }

        packets.append(packet_data)

        if live_callback:
            live_callback(packet_data)

    sniff(prn=handle_packet, timeout=duration_seconds, store=False)
    return packets
