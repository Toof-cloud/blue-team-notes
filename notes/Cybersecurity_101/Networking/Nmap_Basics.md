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
## Task 1: Introduction to Network Scanning (Continued)

### Remote Discovery vs. Local Discovery
When scanning a "remote" network (where a router sits between you and the target), Nmap's behavior changes because **ARP requests cannot cross routers.**

#### Remote Scanning Tactics
To find live hosts across a router, Nmap (as root) sends multiple types of packets to get a response:
* **ICMP Echo Requests:** Standard pings.
* **ICMP Timestamp Requests:** An alternative ping method.
* **TCP SYN (Port 443):** Checking for HTTPS.
* **TCP ACK (Port 80):** Checking for HTTP via a "fake" acknowledgement.



#### Analyzing Results
* **Live Host:** Responds to any of the above probes (e.g., an ICMP Echo Reply).
* **Dead Host:** No response. You may see "ICMP Destination Unreachable" messages sent back by the intermediate router.

---

### Special Scan Types
Beyond the standard `-sn` ping scan, Nmap offers specific options for targeting and noise control:

| Flag | Name | Purpose |
| :--- | :--- | :--- |
| `-sL` | **List Scan** | Lists every IP in the target range without sending a single packet to the targets. Used to verify your scope. |
| `-PS` | **TCP SYN Discovery** | Specifically uses SYN packets to discover hosts. |
| `-PA` | **TCP ACK Discovery** | Specifically uses ACK packets to discover hosts. |
| `-sn` | **No Port Scan** | Lightest "live host" check; does not scan for services/ports. |

> [!TIP]
> Use `-sL` (List Scan) before a big scan to ensure you haven't made a typo in your IP range (e.g., accidentally targeting the whole internet instead of your local lab).

---

## Task: Port Scanning & Service Detection

### TCP Scan Types
Once you know a host is alive, you need to find its open ports. There are two primary ways to scan TCP:

| Flag | Name | Description | Requirements |
| :--- | :--- | :--- | :--- |
| `-sS` | **SYN Scan** | "Stealth" scan. Sends SYN, waits for SYN/ACK, then sends RST. Never completes the connection. | **Root/Sudo** |
| `-sT` | **Connect Scan** | Completes the full 3-way handshake. Slower and more "noisy" in logs. | User privileges |



### Specifying Ports
Nmap scans the top 1000 ports by default. Use these flags to be specific:
* `-p 80,443`: Scan specific ports.
* `-p 1-1024`: Scan a range of ports.
* `-p-`: Scan all 65,535 ports (use with caution, it takes time!).
* `-F`: Fast scan (Top 100 ports).

---

### Service Version Detection (`-sV`)
Knowing a port is "open" isn't enough. The `-sV` flag forces Nmap to communicate with the port to determine exactly what software and version is running.

**Example Command:**
`sudo nmap -sV -p 8008 <target_ip>`

#### Why it matters:
* **Identification:** Tells you if port 8008 is running Apache, Nginx, or a custom web server.
* **Vulnerability Research:** Once you have a version number (e.g., `Apache 2.4.41`), you can search for specific exploits for that version.



---

### Summary of Flags Used
To find the hidden web server and its version in this room, we combined the techniques:
1. **Find Port:** `nmap -p- <target_ip>` (Found port 8008).
2. **Find Version:** `nmap -sV -p 8008 <target_ip>` (Identified the web server software).

---
*End of Nmap Basics Notes*
