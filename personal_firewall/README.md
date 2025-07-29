🔥 Personal Firewall using Python
A lightweight, customizable firewall application built using Python. This project empowers users to monitor and control their network traffic in real-time using user-defined rules. It is designed for personal use, educational purposes, and cybersecurity awareness.

📌 Table of Contents
Project Overview

Key Features

Technologies Used

Project Structure

Setup Instructions

Rule Configuration

Email Alerts

Future Improvements

Author

License

🎯 Project Overview
The Personal Firewall project is aimed at creating a simple but effective software-based firewall. It can capture and inspect network packets, block unwanted traffic, and alert users about suspicious activity. It also includes a graphical user interface (GUI) for better user interaction and control.

🚀 Key Features
Real-time packet sniffing and monitoring

Rule-based traffic control (allow/block specific IPs, ports, and protocols)

User-friendly GUI for live traffic display

Editable rule manager with easy updates

Detailed logging of blocked/suspicious packets

Optional email alert system for critical events

Optional system-level integration using iptables (Linux only)

🧰 Technologies Used
Python: Core programming language

Scapy: For network packet analysis

Tkinter: For the GUI interface

JSON: For managing rule configuration

SMTP (smtplib): For sending email alerts

iptables: Optional Linux-based traffic filtering

🧩 Project Structure
CLI Firewall: Main logic that monitors and filters packets

GUI Monitor: Graphical interface for real-time traffic display

Rule Editor: Allows users to add, edit, and remove rules

Email Notifier: Sends alerts when suspicious activity is detected

Log File: Stores blocked or suspicious packet details

iptables Manager: Integrates firewall rules with Linux system

⚙️ Setup Instructions
Install Python and dependencies

Clone or download the project repository

Launch the firewall (GUI or CLI based on preference)

Edit rules using the rule editor or manually in the rules file

Enable optional email alerts by configuring SMTP settings

(Linux only) Apply rules using iptables for deeper integration

📂 Rule Configuration
Rules are defined in a JSON file with two main categories:

Allow Rules: Define which packets are safe and should be permitted

Block Rules: Define packets that should be denied and logged

Each rule can include criteria such as IP address, port number, and protocol.

📬 Email Alerts
The firewall includes an optional feature to send email alerts whenever suspicious or blocked packets are detected. This helps users stay informed about potential threats even when away from their system.

To use this feature, users need to configure their email credentials and SMTP settings in the alert system module.

💡 Future Improvements
Integration with a web dashboard for remote access

Real-time analytics and graphical reports

AI-based smart rule suggestions

Geo-location of suspicious IP addresses

System tray application for quick controls

Multi-platform support and optimization

🙋‍♂️ Author
Sandeep Kumar
Developer and cybersecurity enthusiast.





