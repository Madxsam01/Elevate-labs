## ✅ `observations.md` (Manual Analysis & Risk Report)

# 🧾 Nmap Port Scan – Observations and Analysis

## 🔎 Scan Context
- Performed a **TCP SYN scan** on subnet `10.0.2.0/24` using `nmap -sS`.
- Environment: Kali Linux running Nmap 7.94SVN
- Network Interface: `eth0` (IP: 10.0.2.15)

---

## 🖥️ Devices Found

### 🔹 10.0.2.2
- **Open Ports**:
  - 135/tcp → msrpc
  - 445/tcp → microsoft-ds (SMB)
  - 3306/tcp → mysql
  - 8090/tcp → opsmessaging
- **MAC Address**: 52:55:0A:00:02:02
- **Analysis**:
  - Likely a Windows-based host running database and messaging services.
  - Presence of SMB suggests file sharing enabled.

---

### 🔹 10.0.2.3
- **Open Ports**:
  - 53/tcp → domain (DNS)
- **MAC Address**: 52:55:0A:00:02:03
- **Analysis**:
  - Appears to be a DNS server or caching resolver.

---

### 🔹 10.0.2.15 (Local Host)
- **Status**: All 1000 scanned TCP ports are closed.
- **Analysis**: No externally visible services running on this host.

---

## ⚠️ Potential Risks Identified

| Risk Source | Description |
|-------------|-------------|
| Port 445    | Exposes SMB services, vulnerable to attacks like EternalBlue. |
| Port 3306   | MySQL database may expose sensitive data or be targeted for injection attacks. |
| Port 8090   | Non-standard service; could be misconfigured and lack authentication. |
| Port 53     | DNS services can be abused for DNS amplification or poisoning if not secured. |

---

## 🛡️ Recommendations

- **Restrict access** to database and SMB ports to trusted IPs.
- **Use strong passwords and disable guest/anonymous access** on SMB.
- **Ensure firewalls block unused ports** at both host and network level.
- **Monitor non-standard ports** (like 8090) for unusual activity.
- **Patch and update** systems regularly to mitigate known exploits.
