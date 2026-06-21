from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
import tkinter as tk
from tkinter import scrolledtext
import threading

sniffing = False

def process_packet(packet):
    info = ""
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        if TCP in packet:
            protocol = "TCP"
            sport = packet[TCP].sport
            dport = packet[TCP].dport
        elif UDP in packet:
            protocol = "UDP"
            sport = packet[UDP].sport
            dport = packet[UDP].dport
            
        elif ICMP in packet:
            protocol = "ICMP"
            sport = "-"
            dport = "-"
        else:
            protocol = "OTHER"
            sport = "-"
            dport = "-"

        info += f"{'─'*50}\n"
        info += f"  Protocol : {protocol}\n"
        info += f"  Source   : {src_ip}:{sport}\n"
        info += f"  Dest     : {dst_ip}:{dport}\n"

        if Raw in packet:
            try:
                payload = packet[Raw].load.decode('utf-8', errors='replace')[:80]
                info += f"  Payload  : {payload}\n"
            except:
                info += f"  Payload  : [Binary Data]\n"

        text_area.after(0, append_text, info)

def append_text(info):
    text_area.config(state='normal')
    text_area.insert(tk.END, info + "\n")
    text_area.see(tk.END)
    text_area.config(state='disabled')

def start_sniffing():
    global sniffing
    sniffing = True
    start_btn.config(state='disabled')
    stop_btn.config(state='normal')
    status_label.config(text="Status: Sniffing... 🟢", fg="lime")
    def run():
        sniff(prn=process_packet, store=False,
              stop_filter=lambda p: not sniffing)
    threading.Thread(target=run, daemon=True).start()

def stop_sniffing():
    global sniffing
    sniffing = False
    start_btn.config(state='normal')
    stop_btn.config(state='disabled')
    status_label.config(text="Status: Stopped 🔴", fg="red")

def clear_output():
    text_area.config(state='normal')
    text_area.delete(1.0, tk.END)
    text_area.config(state='disabled')

root = tk.Tk()
root.title("Network Packet Analyzer - Prodigy CS Task 05")
root.geometry("750x550")
root.configure(bg="#0d1117")

tk.Label(root, text="Network Packet Analyzer",
         font=("Courier", 18, "bold"),
         bg="#0d1117", fg="#00ffcc").pack(pady=10)

tk.Label(root, text="⚠️ Educational & Ethical Use Only",
         font=("Arial", 9), bg="#0d1117", fg="#ff6b6b").pack()

status_label = tk.Label(root, text="Status: Idle ⚪",
                         font=("Arial", 10, "bold"),
                         bg="#0d1117", fg="gray")
status_label.pack(pady=5)

btn_frame = tk.Frame(root, bg="#0d1117")
btn_frame.pack(pady=8)

start_btn = tk.Button(btn_frame, text="▶ Start Capture",
                       command=start_sniffing,
                       bg="#00cc66", fg="white",
                       font=("Arial", 11, "bold"),
                       padx=15, pady=5, bd=0)
start_btn.grid(row=0, column=0, padx=10)

stop_btn = tk.Button(btn_frame, text="⏹ Stop Capture",
                      command=stop_sniffing,
                      bg="#cc3300", fg="white",
                      font=("Arial", 11, "bold"),
                      padx=15, pady=5, bd=0,
                      state='disabled')
stop_btn.grid(row=0, column=1, padx=10)

tk.Button(btn_frame, text="🗑 Clear",
          command=clear_output,
          bg="#334155", fg="white",
          font=("Arial", 11),
          padx=15, pady=5, bd=0).grid(row=0, column=2, padx=10)

text_area = scrolledtext.ScrolledText(root,
                                       width=90, height=22,
                                       bg="#0a0f1a", fg="#00ffcc",
                                       font=("Courier", 9),
                                       state='disabled')
text_area.pack(padx=10, pady=10)

tk.Label(root, text="Prodigy InfoTech | Cybersecurity Internship | Task 05",
         font=("Arial", 8), bg="#0d1117", fg="#555").pack(pady=3)

root.mainloop()
