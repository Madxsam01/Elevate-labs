import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import json
import os
from scapy.all import sniff, IP, TCP, UDP
from datetime import datetime
from alert_emailer import send_email_alert  # Make sure this file exists

RULES_FILE = 'rules.json'
LOG_FILE = 'logs/suspicious.log'

class FirewallGUI:
    def __init__(self, root):
        self.root = root
        root.title("Personal Firewall GUI")
        root.geometry("900x600")

        self.allowed_count = 0
        self.blocked_count = 0
        self.enable_email = tk.BooleanVar()

        self.stats_label = tk.Label(root, text="Allowed: 0 | Blocked: 0", font=("Arial", 12, "bold"))
        self.stats_label.pack(pady=5)

        self.text_area = scrolledtext.ScrolledText(root, width=110, height=30, bg="black", fg="lime", font=("Courier", 9))
        self.text_area.pack(padx=10, pady=5)

        self.email_checkbox = tk.Checkbutton(root, text="Enable Email Alerts", variable=self.enable_email)
        self.email_checkbox.pack(pady=5)

        self.start_button = tk.Button(root, text="Start Firewall", command=self.start_sniffing, bg="green", fg="white")
        self.start_button.pack(pady=10)

    def start_sniffing(self):
        thread = threading.Thread(target=self.sniff_packets)
        thread.daemon = True
        thread.start()
        messagebox.showinfo("Firewall Started", "Packet sniffing has started.")

    def sniff_packets(self):
        sniff(prn=self.process_packet, store=0)

    def process_packet(self, pkt):
        result, reason = self.packet_filter(pkt)
        summary = pkt.summary()

        if result:
            self.allowed_count += 1
            status = "ALLOWED"
        else:
            self.blocked_count += 1
            status = "BLOCKED"
            self.log_packet(pkt, reason)
            if self.enable_email.get():
                send_email_alert(summary)

        self.update_gui(summary, status)

    def update_gui(self, summary, status):
        self.text_area.insert(tk.END, f"[{status}] {summary}\n")
        self.text_area.yview(tk.END)
        self.stats_label.config(text=f"Allowed: {self.allowed_count} | Blocked: {self.blocked_count}")

    def packet_filter(self, pkt):
        try:
            with open(RULES_FILE) as f:
                rules = json.load(f)
        except Exception as e:
            print("Error loading rules:", e)
            return True, "No rule check (error)"

        if IP in pkt:
            ip_layer = pkt[IP]
            proto = 'tcp' if TCP in pkt else 'udp' if UDP in pkt else 'other'
            port = pkt[TCP].dport if TCP in pkt else pkt[UDP].dport if UDP in pkt else None
            dst_ip = ip_layer.dst

            for rule in rules.get('block', []):
                if dst_ip == rule['ip'] and port == rule['port'] and proto == rule['protocol']:
                    return False, "Matched block rule"

            for rule in rules.get('allow', []):
                if dst_ip == rule['ip'] and port == rule['port'] and proto == rule['protocol']:
                    return True, "Matched allow rule"

            return False, "Default block (no match)"
        return True, "Non-IP packet"

    def log_packet(self, pkt, reason):
        os.makedirs("logs", exist_ok=True)
        with open(LOG_FILE, "a") as f:
            f.write(f"[{datetime.now()}] BLOCKED: {pkt.summary()} | Reason: {reason}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = FirewallGUI(root)
    root.mainloop()
