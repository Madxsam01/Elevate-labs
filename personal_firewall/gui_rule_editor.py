import tkinter as tk
from tkinter import messagebox
import json

RULES_FILE = 'rules.json'

class RuleEditorApp:
    def __init__(self, root):
        self.root = root
        root.title("Firewall Rule Editor")

        self.rule_type = tk.StringVar(value="block")
        tk.Radiobutton(root, text="Block", variable=self.rule_type, value="block").pack()
        tk.Radiobutton(root, text="Allow", variable=self.rule_type, value="allow").pack()

        self.ip_entry = tk.Entry(root)
        self.ip_entry.insert(0, "IP Address")
        self.ip_entry.pack()

        self.port_entry = tk.Entry(root)
        self.port_entry.insert(0, "Port")
        self.port_entry.pack()

        self.protocol_entry = tk.Entry(root)
        self.protocol_entry.insert(0, "Protocol (tcp/udp)")
        self.protocol_entry.pack()

        tk.Button(root, text="Add Rule", command=self.add_rule).pack()

    def add_rule(self):
        try:
            ip = self.ip_entry.get()
            port = int(self.port_entry.get())
            proto = self.protocol_entry.get().lower()

            with open(RULES_FILE, 'r+') as f:
                data = json.load(f)
                data[self.rule_type.get()].append({
                    "ip": ip, "port": port, "protocol": proto
                })
                f.seek(0)
                json.dump(data, f, indent=2)
                f.truncate()
            messagebox.showinfo("Success", "Rule added successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = RuleEditorApp(root)
    root.mainloop()
