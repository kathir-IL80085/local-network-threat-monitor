# main.py
from capture import capture_packets
from analyzer import analyze_packets
from anomaly import detect_anomalies
from report import build_report
from exporter import export_report

def live_print(pkt):
    print(f"[LIVE] {pkt['src_ip']} → {pkt['dst_ip']} | {pkt['protocol']} | {pkt['size']}B")

def main():
    minutes = int(input("⏱ Enter monitoring duration (minutes): "))
    duration = minutes * 60

    print("\n[+] Live packet capture started...\n")
    packets = capture_packets(duration, live_callback=live_print)

    stats = analyze_packets(packets)
    anomalies = detect_anomalies(stats)
    report = build_report(stats, anomalies, minutes)

    print("\n🛡 NETWORK SECURITY REPORT")
    print("=" * 60)
    print(f"Total Packets: {report['summary']['total_packets']}")
    print(f"Risk Level  : {report['summary']['risk_level']}")
    print(f"Risk Score  : {report['summary']['risk_score']}/100")

    if anomalies:
        print("\nDetected Anomalies:")
        for a in anomalies:
            print(f" - {a['type']} ({a['reason']})")
    else:
        print("\nDetected Anomalies: None")

    file = export_report(report, packets)
    print(f"\n📁 Report exported to: {file}")

if __name__ == "__main__":
    main()
