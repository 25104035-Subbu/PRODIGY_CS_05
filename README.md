# PRODIGY_CS_05 - Network Packet Analyzer

## Description
A Python-based Network Packet Analyzer that captures 
and displays real-time network traffic. Built using 
Scapy and Tkinter GUI.

## Features
- 🌐 Captures live network packets in real-time
- 📡 Displays Source & Destination IP addresses
- 🔍 Identifies Protocol (TCP / UDP / ICMP)
- 📦 Shows Payload data
- ▶️ Start / Stop Capture buttons
- 🖥️ Dark-themed GUI using Tkinter
- 🔄 Auto-scroll output display

## How It Works
- User clicks Start Capture button
- Tool starts sniffing network packets
- Each packet shows Protocol, Source IP, Dest IP
- Payload data displayed if available
- Stop Capture button stops sniffing

## Code Explanation
- `process_packet()` - captures and extracts packet info
- `start_sniffing()` - starts packet capture in background thread
- `stop_sniffing()` - stops packet capture
- `append_text()` - updates GUI with packet data

## Technologies Used
- Python 3.x
- Scapy (Packet Capture)
- Tkinter (GUI)
- Threading

## How to Run
- Open CMD as Administrator
- Navigate to file location
- Type: py packet_analyzer.py
- Click Start Capture
## Example Output

### ✅ Start Capture
- Status: Sniffing... 🟢
- Start Capture button disabled
- Stop Capture button enabled

### 📡 Packet Captured
- Protocol : TCP
- Source   : 57.144.55.32:5222
- Dest     : 10.82.205.1:7985
- Payload  : [Binary Data]

### ⏹ Stop Capture
- Status: Stopped 🔴
- Capture stops immediately

## ⚠️ Ethical Use
This tool is built strictly for 
educational purposes only.

