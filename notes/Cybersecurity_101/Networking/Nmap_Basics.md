# TryHackMe: Nmap Notes

## Task 1: Introduction to Network Scanning

### The Core Challenges
When exploring a network, we generally aim to answer two primary questions:
1. **Host Discovery:** Which devices are currently "live" or active on the network?
2. **Service Discovery:** What services (e.g., SSH, HTTP, FTP) are these devices running?

### Manual Limitations
While basic tools exist, they often fall short in complex environments:

| Tool | Limitations |
| :--- | :--- |
| **Ping** | Easily blocked by firewalls (ICMP traffic). |
| **Arp-scan** | Only works within the local network segment (Layer 2). |
| **Telnet** | Extremely slow/inefficient for scanning thousands of ports. |

> [!IMPORTANT]
> Manually checking 254 IP addresses (in a `/24` subnet) or thousands of ports is a significant waste of time without automation and reliability.

### The Solution: Nmap
**Nmap** (Network Mapper) is the industry-standard tool for these tasks. 
* **History:** Open-source since 1997.
* **Versatility:** Capable of host discovery, port scanning, service version detection, and OS fingerprinting.
* **Flexibility:** Can bypass many common firewall restrictions and handle various network setups.



---
