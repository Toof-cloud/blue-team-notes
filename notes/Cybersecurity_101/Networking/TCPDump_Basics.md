# TCP Dump

## Tcpdump and libpcap Overview

The **Tcpdump** tool and its **libpcap** library are written in **C** and **C++** and were released for **Unix-like systems** in the **late 1980s to early 1990s**. As a result, they are considered highly **stable** and provide **optimal performance** for packet capturing and analysis.

The **libpcap** library serves as the **foundation** for many modern **networking and packet analysis tools**. It was later ported to **Microsoft Windows** as **WinPcap**, extending its usability beyond Unix-based environments.

# Tcpdump Fundamentals

Running `tcpdump` without arguments is useful for testing installation, but real-world scenarios require specific arguments to define listening interfaces, output files, and display formats.

---

## 1. Specify the Network Interface
Use the `-i INTERFACE` flag to decide which network interface to listen to.
* **All interfaces:** `-i any`
* **Specific interface:** `-i eth0` or `-i ens5`

> **Note:** Use the command `ip address show` (or `ip a s`) to list available interfaces on your system.

---

## 2. Manage Packet Files
### Save Captured Packets
To save traffic for later analysis, use `-w FILE.pcap`. 
* Packets will not scroll on the screen when this option is used.
* Saved `.pcap` files can be opened in tools like **Wireshark**.

### Read Captured Packets
To analyze a previously saved file, use `-r FILE`. This is essential for studying protocol behavior or analyzing historical network attacks.

---

## 3. Capture Constraints & Formatting
### Limit Packet Count
Use `-c COUNT` to stop the capture after a specific number of packets. Otherwise, the process continues until interrupted via `CTRL-C`.

### Disable Name Resolution
By default, Tcpdump tries to resolve IPs to hostnames and ports to service names (e.g., 80 to http).
* `-n`: Do not resolve IP addresses.
* `-nn`: Do not resolve IP addresses **or** port/protocol numbers.

### Verbose Output
To see more detail (TTL, identification, length, etc.), use the verbose flags:
* `-v`: Verbose.
* `-vv`: More verbose.
* `-vvv`: Maximum verbosity.

---

## Summary Table

| Command | Explanation |
| :--- | :--- |
| `tcpdump -i INTERFACE` | Captures packets on a specific interface |
| `tcpdump -w FILE` | Writes captured packets to a file |
| `tcpdump -r FILE` | Reads captured packets from a file |
| `tcpdump -c COUNT` | Captures a specific number of packets |
| `tcpdump -n` | Don't resolve IP addresses |
| `tcpdump -nn` | Don't resolve IP addresses or protocol numbers |
| `tcpdump -v` | Verbose display (increase with `-vv` or `-vvv`) |

---

## Examples

* **Verbose Ethernet Capture:** `tcpdump -i eth0 -c 50 -v`  
    *Captures 50 packets on eth0 with verbose details.*

* **Save WiFi Traffic:** `tcpdump -i wlo1 -w data.pcap`  
    *Saves all WiFi traffic to a file until manually stopped.*

* **Fast Monitor All Interfaces:** `tcpdump -i any -nn`  
    *Monitors all traffic globally without waiting for DNS/Port lookups.*