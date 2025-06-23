# Elevate-labs
# Local Network Port Scanning Task

## Objective
To perform a TCP SYN scan using Nmap on the local network and identify open ports and potential security risks.

## Tools Used
- Nmap
- Wireshark (optional)

## Steps Performed
1. Found local IP range using `ipconfig`/`ifconfig`
2. Ran Nmap command: `nmap -sS 192.168.1.0/24`
3. Saved results in `scan_results.txt`
4. Documented findings in `observations.md`

## Outcome
- Gained basic understanding of open ports and network exposure.
- Identified devices and services running on my network.
