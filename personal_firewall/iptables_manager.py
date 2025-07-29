import json
import os

def apply_iptables_rules():
    with open("rules.json") as f:
        rules = json.load(f)

    # Flush existing custom rules
    os.system("sudo iptables -F")

    for rule in rules["block"]:
        ip = rule["ip"]
        port = rule["port"]
        proto = rule["protocol"]
        cmd = f"sudo iptables -A INPUT -p {proto} --dport {port} -s {ip} -j DROP"
        os.system(cmd)
        print(f"Applied iptables block rule: {cmd}")
