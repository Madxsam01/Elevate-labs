# Nmap TCP SYN Scan – Observations

## Date:
June 23, 2025

## Command Used:
nmap -sS 10.0.2.0/24

markdown
Copy
Edit

## Summary:
Scanned local subnet (10.0.2.0/24) for live hosts and open TCP ports.

## Devices Found:

| IP Address   | Open Ports | Services     | Notes                  |
|--------------|------------|--------------|------------------------|
| 10.0.2.1     | 22, 80     | SSH, HTTP    | Likely a web server    |
| 10.0.2.3     | 445, 139   | SMB, NetBIOS | File sharing enabled   |

## Risks Identified:
- Port 445 is vulnerable to SMB exploits (e.g., EternalBlue).
- Web interface (port 80) may be exposed if not secured.
- Default SSH access might be brute-forced if passwords are weak.

## Recommendations:
- Disable unnecessary services.
- Use firewalls or iptables to restrict access.
- Update systems regularly and patch known vulnerabilities.
