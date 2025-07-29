🔥 Personal Firewall using Python
This project is a lightweight, customizable personal firewall developed in Python. It allows users to monitor, control, and block incoming or outgoing network traffic based on a set of predefined rules. It supports both command-line and graphical user interface (GUI) modes, making it user-friendly and flexible.

🛠️ Key Features
Real-time Packet Sniffing: Monitors live incoming and outgoing network packets using Scapy.

Rule-Based Filtering: Traffic can be allowed or blocked based on IP address, port number, and protocol (TCP/UDP), all defined in a JSON file.

GUI for Live Monitoring: A Tkinter-based interface shows real-time packet activity, including whether each packet is allowed or blocked, along with stats.

Rule Editor GUI: A simple GUI allows users to add or remove firewall rules without editing JSON manually.

Logging System: Suspicious or blocked packets are logged with timestamps for auditing and later analysis.

Email Alert System (Optional): Sends an email alert whenever a suspicious packet is blocked.

iptables Integration (Optional for Linux): Automatically applies blocking rules using the Linux firewall (iptables) for system-level security.

📁 Project Modules
firewall.py: Runs the main firewall logic via command-line interface.

gui_firewall.py: Provides a GUI that shows live packet data, traffic stats, and integrates logging and alerts.

gui_rule_editor.py: Allows users to create or update firewall rules through a simple form-based interface.

iptables_manager.py: Automatically applies block rules at the system level using iptables on Linux systems.

alert_emailer.py: Manages the sending of email alerts for flagged packets.

rules.json: A configuration file that stores user-defined rules in "allow" and "block" categories.

logs/suspicious.log: A log file that records details of blocked or suspicious packets with reasons and timestamps.

✅ How It Works
The firewall starts sniffing all network traffic using Scapy.

Each packet is checked against the rules defined in rules.json.

If a packet matches a block rule, it is logged and optionally triggers an email alert.

If a packet matches an allow rule, it is permitted through.

Packets that do not match any rule are blocked by default (configurable).

GUI users can see all this activity in real-time, including how many packets were allowed or blocked.

On Linux, users can apply the same block rules to the system firewall (iptables) for more robust protection.

📬 Email Alerts
The firewall can be configured to send an email every time a packet is blocked. This is useful for detecting unauthorized access attempts, port scans, or intrusion attempts in real-time.

📌 Use Cases
Personal computers for added network security

Lightweight intrusion detection on home or lab networks

Educational project for learning about firewalls, networking, and Python

