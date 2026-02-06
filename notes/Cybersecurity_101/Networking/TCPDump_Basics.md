# TCPDump: The Basics

## Tcpdump and libpcap Overview

The **Tcpdump** tool and its **libpcap** library are written in **C** and **C++** and were released for **Unix-like systems** in the **late 1980s to early 1990s**. As a result, they are considered highly **stable** and provide **optimal performance** for packet capturing and analysis.

The **libpcap** library serves as the **foundation** for many modern **networking and packet analysis tools**. It was later ported to **Microsoft Windows** as **WinPcap**, extending its usability beyond Unix-based environments.

# Tcpdump: Basic Packet Capture

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

---

# Tcpdump: Filtering Expressions

## 1. Filtering by Host
You can limit captured packets to those exchanged with a specific network printer, game server, or website using the `host` keyword. Capturing packets usually requires `root` or `sudo` privileges.

* **Specific Host:** `sudo tcpdump host example.com` (Captures traffic both to and from the host).
* **Source Only:** `tcpdump src host 10.10.1.1` (Only packets where the specified IP is the sender).
* **Destination Only:** `tcpdump dst host 10.10.1.1` (Only packets where the specified IP is the receiver).

---

## 2. Filtering by Port
To capture traffic for a specific service, such as DNS or HTTP, use the `port` keyword.

* **DNS Traffic:** `sudo tcpdump port 53 -n`.
* **HTTPS Traffic:** `tcpdump tcp port 443`.
* **Combined Filters:** Use `and` to be more specific, e.g., `tcpdump host example.com and tcp port 443`.

---

## 3. Analyzing Output and Flags
When reading output, the `>` symbol shows the direction of traffic from Source to Destination.

| Flag | Meaning | Description |
| :--- | :--- | :--- |
| **`[S]`** | **SYN** | Connection request (Start of TCP handshake) |
| **`[.]`** | **ACK** | Acknowledgment (Data received successfully) |
| **`[P]`** | **PUSH** | Data is being sent to the application immediately |
| **`[F]`** | **FIN** | Finished (Normal connection shutdown) |
| **`[R]`** | **RST** | Reset (Immediate connection kill/rejection) |

---

## 4. Reading from Files (`-r`) and Piping
You do not need `root` or `sudo` privileges to read an existing `.pcap` file.

* **Read Command:** `tcpdump -r traffic.pcap`.
* **Limit Results:** `tcpdump -r traffic.pcap -c 5` (Shows only the first 5 packets).
* **Counting Packets:** Use the Linux `wc` (word count) tool to count lines.
  * `tcpdump -r traffic.pcap src host 192.168.124.1 | wc -l`.
  * **Note:** Ensure you use a lowercase **L** (`-l`) for lines, not the number **1**.

---

## 5. Solving Lab Tasks (ARP & DNS)

### Task: Finding the ARP Requestor
* **Question:** What is the IP address of the host that asked for the MAC address of 192.168.124.137?
* **Command:** `tcpdump -r traffic.pcap arp -n`
* **Logic:** Look for the phrase `Request who-has [Target] tell [Source]`. The IP after **"tell"** is the host that asked the question.

### Task: Identifying the First DNS Query
* **Question:** What hostname (subdomain) appears in the first DNS query?
* **Command:** `tcpdump -r traffic.pcap port 53 -c 1 -n`
* **Logic:**
  * **`port 53`**: Filters for DNS traffic.
  * **`-c 1`**: Stops after the very first packet.
  * **Result:** Look for the `A?` (IPv4) or `AAAA?` (IPv6) query. The string immediately following it is the hostname requested.