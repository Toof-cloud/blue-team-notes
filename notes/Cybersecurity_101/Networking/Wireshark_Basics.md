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

# Packet Dissection

## Overview
**Packet dissection**, also known as **protocol dissection**, is the process of investigating packet details by decoding the available protocols and their fields. Wireshark supports a wide range of protocols for dissection, and it also allows users to write custom dissection scripts.

More information about protocol dissection can be found in the official Wireshark documentation.

> **Note:**  
> This section focuses on how Wireshark uses the **OSI model** to break down packets and how these layers can be used for packet analysis. It is assumed that the reader already has background knowledge of the OSI model and its functions.

---

## Packet Details in Wireshark

By clicking on a packet in the **Packet List pane**, you can view its detailed structure in the **Packet Details pane**.  
- **Single click**: Expands packet details  
- **Double click**: Opens packet details in a new window  

Packets typically consist of **5 to 7 layers**, depending on the protocol stack used. These layers are mapped conceptually to the OSI model.

When a specific field is selected in the Packet Details pane, Wireshark automatically highlights the corresponding bytes in the **Packet Bytes pane**, allowing precise inspection of raw data.

---

## Packet Layers Breakdown

In a typical HTTP packet, Wireshark may display the following seven layers:

### 1. Frame (Layer 1 – Physical Layer)
This layer shows general information about the frame or packet, including:
- Frame number
- Frame length
- Capture time
- Interface details  

It represents information related to the **Physical layer** of the OSI model.

---

### 2. Source [MAC] (Layer 2 – Data Link Layer)
This layer displays:
- Source MAC address
- Destination MAC address  

It corresponds to the **Data Link layer**, which is responsible for node-to-node data transfer within the same network.

---

### 3. Source [IP] (Layer 3 – Network Layer)
This layer shows:
- Source IPv4 or IPv6 address
- Destination IPv4 or IPv6 address  

It represents the **Network layer**, which handles logical addressing and routing between networks.

---

### 4. Protocol (Layer 4 – Transport Layer)
This layer provides details about the transport protocol, such as:
- TCP or UDP
- Source port
- Destination port
- Sequence and acknowledgment numbers (for TCP)  

It maps to the **Transport layer**, responsible for end-to-end communication.

---

### 5. Protocol Errors
This section is a continuation of the **Transport layer**, particularly for TCP.  
It may include:
- TCP segment reassembly
- Retransmissions
- Out-of-order packets  

These details help identify communication issues or anomalies.

---

### 6. Application Protocol (Layer 7 – Application Layer)
This layer displays information specific to the application-level protocol, such as:
- HTTP
- FTP
- SMB
- DNS  

It represents the **Application layer**, where user-facing protocols operate.

---

### 7. Application Data
This layer is an extension of the Application Protocol layer and may show:
- Request or response payloads
- Headers and body data
- Encoded or plaintext content  

It contains the actual data being transmitted by the application.

---
# Packet Navigation (Wireshark)

## Packet Numbers
- Wireshark assigns a **unique packet number** to every captured packet.
- Helps navigate **large captures** and return to a **specific event** quickly.
- Packet numbers are sequential based on capture order.

**Use case:**
- Referencing packets during analysis
- Jumping back to a known suspicious packet

---

## Go to Packet
- Allows direct navigation to a specific packet number.
- Supports:
  - Jumping **up/down** between packets
  - **In-frame packet tracking**
  - Finding the **next packet in a conversation**

**Access methods:**
- `Go` menu
- Toolbar
- Keyboard shortcut

---

## Find Packets
- Enables searching packets by **content**, not just number.
- Useful for identifying:
  - Intrusion patterns
  - Errors
  - Specific protocol activity

### Input Types
- **Display Filter**
- **Hex**
- **String** (most common)
- **Regex** (most powerful)

> Searches are **case-insensitive by default**, but case sensitivity can be enabled.

### Search Locations
- **Packet List pane**
- **Packet Details pane**
- **Packet Bytes pane**

⚠️ Searching in the wrong pane will return no results even if the data exists.

---

## Mark Packets
- Marks packets for **quick identification** and later review.
- Useful for:
  - Highlighting suspicious activity
  - Exporting specific packets

**How to mark:**
- `Edit` menu
- Right-click → Mark/Unmark Packet

**Behavior:**
- Marked packets appear **black**
- Marks are **session-based** (lost when the file is closed)

---

## Packet Comments
- Allows adding **notes directly to packets**
- Useful for:
  - Documentation
  - Collaboration with other analysts
  - Remembering suspicious indicators

**Key difference from marking:**
- Comments **persist** in the capture file until removed

---

## Export Packets
- Used to extract **specific packets** from large capture files.
- Helps narrow the investigation scope.
- Ideal for sharing only **relevant evidence**.

**Access:**
- `File` → Export Specified Packets

---

## Export Objects (Files)
- Extracts files transferred over the network.
- Critical for malware and incident response analysis.

**Supported protocols:**
- DICOM
- HTTP
- IMF
- SMB
- TFTP

> Only available when the protocol supports object transfer.

---

## Time Display Format
- Default format: **Seconds Since Beginning of Capture**
- Often changed to **UTC** for clearer timelines.

**Change via:**
- `View` → Time Display Format

**Why important:**
- Improves event correlation
- Easier timeline reconstruction

---

## Expert Info
- Automatically flags **protocol anomalies** and issues.
- Should be treated as **guidance**, not absolute truth.
- False positives and negatives are possible.

### Severity Levels
| Severity | Color  | Description |
|--------|--------|------------|
| Chat   | Blue   | Normal workflow information |
| Note   | Cyan   | Notable events (e.g., app errors) |
| Warn   | Yellow | Unusual behavior or warnings |
| Error  | Red    | Malformed or problematic packets |

### Common Expert Info Groups
| Group      | Description |
|-----------|-------------|
| Checksum  | Checksum errors |
| Deprecated | Deprecated protocol usage |
| Comment   | Packet comment detection |
| Malformed | Malformed packet detection |

**Access Expert Info:**
- Status bar (lower-left)
- `Analyse` → Expert Information

Displays:
- Packet number
- Summary
- Protocol
- Group
- Total occurrences

