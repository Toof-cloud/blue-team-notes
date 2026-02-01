# Wireshark Notes – Use Cases & GUI Overview

## 📌 What is Wireshark?
Wireshark is one of the most powerful **network traffic analyzer** tools available. It allows analysts to capture, inspect, and analyze packets in depth.

> ⚠️ **Note:** Wireshark is **NOT** an Intrusion Detection System (IDS).  
It does **not** block, modify, or prevent traffic. It only **reads and analyzes packets**, so detection of issues relies heavily on the analyst’s knowledge and investigation skills.

---

## 🧠 Use Cases of Wireshark

### 1️⃣ Network Troubleshooting
- Detect network load issues
- Identify congestion and bottlenecks
- Locate failure points in network communication

### 2️⃣ Security Analysis
- Detect rogue or unknown hosts
- Identify abnormal port usage
- Spot suspicious or malicious traffic patterns

### 3️⃣ Protocol Analysis & Learning
- Inspect protocol behavior
- Analyze response codes
- Examine payload and packet structure

---

## 🖥️ Wireshark GUI Overview

When Wireshark opens, it displays a **single all-in-one interface** designed for efficient traffic investigation.

### Main GUI Sections

| Section | Description |
|------|------------|
| **Toolbar** | Contains menus and shortcuts for capturing, filtering, sorting, exporting, and merging packets |
| **Display Filter Bar** | Used to apply display filters and queries |
| **Recent Files** | Shows previously opened PCAP files |
| **Capture Filters & Interfaces** | Lists available network interfaces (e.g., `eth0`, `ens33`, `lo`) |
| **Status Bar** | Shows capture status, active profile, and packet statistics |

> 💡 A **network interface** is the connection point between the computer and the network.  
Examples include physical (Ethernet) and virtual/software interfaces.

---

## 📂 Loading PCAP Files

PCAP files can be loaded using:
- `File → Open`
- Drag and drop
- Double-clicking the PCAP file

Once loaded, Wireshark displays:
- File name
- Total packet count
- Packet timeline and details

---

## 📦 Packet Analysis Panes

Wireshark presents packet data using **three main panes**:

### 1️⃣ Packet List Pane
- Displays a summary of packets
- Includes source, destination, protocol, and info
- Clicking a packet loads details into other panes

### 2️⃣ Packet Details Pane
- Shows a layered protocol breakdown
- Allows deep inspection of headers and fields

### 3️⃣ Packet Bytes Pane
- Displays raw packet data in:
  - Hexadecimal
  - ASCII format
- Highlights fields based on selection in the details pane

---

## 🎨 Packet Coloring

Wireshark uses **coloring rules** to help quickly identify:
- Protocols
- Packet types
- Potential anomalies

### Types of Coloring Rules
- **Temporary rules** – active only during the current session
- **Permanent rules** – saved in the user profile and persist across sessions

### Managing Coloring Rules
- Create permanent rules via:
  - `View → Coloring Rules`
  - Right-click menu
- Enable/disable coloring via:
  - `View → Colorize Packet List`
- Temporary coloring can be applied using:
  - `View → Conversation Filter`

---

## 🦈 Traffic Sniffing (Live Capture)

### Control Buttons
- 🟦 **Blue Shark** – Start capturing traffic
- 🟥 **Red Button** – Stop capture
- 🟩 **Green Button** – Restart capture

The **Status Bar** displays:
- Active capture interface
- Number of captured packets

---

## 🔗 Merging PCAP Files

Wireshark allows merging multiple PCAP files into one.

### Steps:
1. Open an existing PCAP
2. Go to `File → Merge`
3. Select another PCAP file
4. Review total packet count
5. Click **Open** to merge
6. Save the merged PCAP before analysis

---

## 📊 Viewing Capture File Details

Viewing file metadata is useful when handling multiple PCAPs.

### Information Available:
- File hash
- Capture time
- Capture comments
- Interfaces used
- Packet statistics

### How to View:
- `Statistics → Capture File Properties`
- Click the **PCAP icon** at the bottom-left of the window

---

## ✅ Key Takeaways
- Wireshark is a **powerful analysis tool**, not a defense system
- Effective use depends on **analyst skill**
- GUI layout supports deep packet inspection
- Coloring, filtering, and merging enhance investigation efficiency
