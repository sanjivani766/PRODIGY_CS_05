#  Network Packet Analyzer

This project is focused on cybersecurity and network analysis.  
It is a **Python-based packet sniffer** that captures and analyzes network packets on your system for **educational purposes**.  

The tool demonstrates the basics of **network traffic monitoring** and **protocol analysis** in a safe and controlled environment.

---

## **Features**

- **Real-time packet capture**: Monitors all network packets on your machine.  
- **Source & Destination IPs**: Displays the origin and destination of each packet.  
- **Protocol detection**: Identifies the protocol of each packet (TCP, UDP, ICMP, or others).  
- **Payload length**: Shows the size of the packet payload in bytes.  
- **Timestamp**: Each captured packet is displayed with the exact date and time.  
- **Clean stopping mechanism**: Sniffer can be stopped safely by pressing Enter.  
- **Ethical and educational**: Designed for learning and experimentation, not for malicious use.

## Technologies Used

Python 3.x: Programming language.

Scapy: For packet capture and analysis.

Colorama: Optional, for colored output in terminal.

## Learning Outcomes

By completing this task, I learned:

How to capture and inspect network packets in Python.

Understanding of TCP, UDP, and ICMP protocols.

How to safely display packet data with timestamp.

Implementing a clean stopping mechanism in a real-time application.

Ethical considerations in cybersecurity projects.

## Future Enhancements

Protocol-specific analysis: Decode application-layer protocols like HTTP, DNS, or FTP.

Logging to PCAP or database: Save captured packets for long-term analysis.

Live statistics dashboard: Visualize traffic patterns in real-time.

Suspicious activity alerts: Detect SYN floods, port scans, or brute-force attempts.

Filtering options: Capture only specific protocols, IP addresses, or ports.

GeoIP tracking: Show approximate location of source and destination IPs.

Integration with threat intelligence feeds: Flag packets from known malicious IPs.

Machine learning anomaly detection: Detect unusual traffic patterns automatically.

## Ethical Use

This tool is developed strictly for educational purposes.
It should only be used on networks where you have permission to capture traffic.
Unauthorized packet sniffing on public or private networks without consent is illegal.
This project is intended as a demonstration of network monitoring skills for educational purposes.
