from scapy.all import sniff, IP, TCP, UDP, ICMP
from datetime import datetime
import threading

# Global stop flag
stop_flag = False

def process_packet(packet):
    if IP in packet:
        src = packet[IP].src
        dst = packet[IP].dst

        if TCP in packet:
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"
        elif ICMP in packet:
            protocol = "ICMP"
        else:
            protocol = "OTHER"

        payload_len = len(packet.payload)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {src} -> {dst} | Protocol: {protocol} | Payload Length: {payload_len}")

def stop_sniffer(packet):
    return stop_flag

def wait_for_stop():
    global stop_flag
    input("Press Enter to stop sniffing...\n")
    stop_flag = True

# Start thread to wait for Enter key
threading.Thread(target=wait_for_stop).start()

print("Starting Packet Sniffer...")
sniff(prn=process_packet, store=False, stop_filter=stop_sniffer)

print("Packet Sniffer Stopped.")