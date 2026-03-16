# Burp Suite: The Basics — Task 1

## Introduction

**TryHackMe Room Notes**

---

## 📌 What is Burp Suite?

Burp Suite is the industry-standard tool for **Web Application Penetration Testing**. It acts as a "Man-in-the-Middle" (MITM) proxy between your web browser and the target server. This allows you to pause, inspect, and modify web traffic in real-time before it reaches its destination.

### 🧱 Why Use It?

While browsers like Brave or Chrome have "Inspect Element," they only show you what has already happened. Burp Suite allows you to:

* **Intercept Requests:** Stop an outgoing request to change your "User ID" or "Price" before the server sees it.
* **Automate Attacks:** Send thousands of different passwords to a login form automatically.
* **Analyze Records:** Keep a full history of every request and response for deep forensic analysis.

---

## 🏗️ Core Module Overview

Burp Suite is a "suite" because it contains multiple tools under one roof:

| Tool | Purpose |
| --- | --- |
| **Proxy** | The heart of Burp. Intercepts and modifies traffic. |
| **Repeater** | Manually resends specific requests to test for vulnerabilities. |
| **Intruder** | Automates customized attacks (like brute-forcing). |
| **Decoder** | Encodes or decodes data (Base64, URL, Hex). |
| **Comparer** | Compares two responses to find subtle differences. |
| **Sequencer** | Analyzes the randomness of session tokens. |

---

## 🧠 Navigation & Mentality

As you start this room, remember that Burp Suite is highly configurable. The goal is to move from **theoretical understanding** (knowing what the buttons do) to **practical exploration** (seeing how the server reacts when you change a single bit of data).

### 🛡️ Getting Ready

1. **Installation:** You'll learn to set it up on your local machine (Mac, Linux, or Windows).
2. **Configuration:** You'll set up your browser to "talk" to Burp.
3. **The Proxy:** You'll learn the "Intercept is ON" workflow.

---

## 📝 Task 1 Answers

* **Let us start!**
* `No answer needed`



---

## 🛠️ Burp Suite Glossary

| Term | Meaning |
| --- | --- |
| **Intercept** | To pause a request in transit. |
| **Request** | The data your browser sends to the server (GET/POST). |
| **Response** | The data the server sends back to your browser (HTML/JSON). |
| **Scope** | Defining which websites Burp is allowed to monitor (to avoid clutter). |

---
# Burp Suite: The Basics — Task 2

## What is Burp Suite?

**TryHackMe Room Notes**

---

## 📌 Defining the Framework

Burp Suite, developed by **PortSwigger**, is a Java-based platform designed to be an all-in-one solution for web application security testing. It is essentially the "Swiss Army Knife" for hackers and security researchers.

### 🧱 Edition Comparison

There are three main versions of Burp Suite. As a student, you will most likely start with the Community edition.

| Edition | Target Audience | Key Features |
| --- | --- | --- |
| **Community** | Hobbyists & Students | Core manual tools (Proxy, Repeater), no automated scanner. |
| **Professional** | Professional Pentesters | Includes automated vulnerability scanner, faster Intruder, and project saving. |
| **Enterprise** | Large Organizations | Fully automated, scheduled scanning across entire networks. |

---

## ⚙️ How it Works: The Proxy "Catch"

The most fundamental concept to grasp is the **Interception Workflow**. Normally, your browser talks directly to a server. With Burp, you insert a middle layer.

1. **Request:** You click a button on a website.
2. **Intercept:** The request travels to Burp Suite and **stops**. It does not reach the server yet.
3. **Modification:** You can change the data (e.g., changing a price from `$100` to `$1`).
4. **Forward:** You tell Burp to "Forward" the modified request to the server.
5. **Response:** The server sends data back, which Burp also catches for you to inspect.

---

## 🧠 Why Java?

Because Burp Suite is written in **Java**, it is "Platform Independent." Whether you are on your **Mac** or using **Kali Linux**, the experience remains consistent. This also allows for the **BApp Store**, where the community can write and share extensions to add new features to Burp.

---

## 📝 Task 2 Answers

* **Which edition of Burp Suite will we be using in this module?**
* `Burp Suite Community Edition`


* **Which edition of Burp Suite is geared towards large-scale automated scanning?**
* `Burp Suite Enterprise Edition`


* **Burp Suite is written in which language?**
* `Java`



---

## 🛠️ Key Concepts

* **Point-and-Click:** While we use tools like `nmap` or `sqlmap` in the terminal, Burp is primarily a GUI-driven tool, making it easier to visualize complex web traffic.
* **Extensibility:** If Burp doesn't do something you need, there is likely an extension in the **BApp Store** that does.

---
# Burp Suite: The Basics — Task 3

## Features of Burp Community

**TryHackMe Room Notes**

---

## 📌 The Pentester's Toolkit

Even in the free Community Edition, Burp Suite provides the essential modules needed to conduct a thorough manual security assessment. Understanding when to switch between these tools is key to an efficient workflow.

### 🧱 Core Feature Breakdown

| Feature | Primary Function | Pentesting Use Case |
| --- | --- | --- |
| **Proxy** | Traffic Interception | Pausing a request to modify a hidden form field or cookie value. |
| **Repeater** | Manual Request Testing | Tweaking an SQL injection payload and resending it to see the server's error message. |
| **Intruder** | Automated Attacks | Testing a list of 1,000 common passwords against a single username. |
| **Decoder** | Data Transformation | Converting a suspicious Base64 string back into readable text. |
| **Comparer** | Visual Comparison | Comparing a successful login response vs. a failed one to find tiny timing or size differences. |
| **Sequencer** | Randomness Analysis | Checking if session cookies are truly random or if they follow a predictable pattern. |

---

## ⚙️ Extending the Suite: The BApp Store

One of Burp's greatest strengths is its extensibility. Because it runs on Java, it can integrate modules written in **Java, Python (Jython), or Ruby (JRuby)**.

* **Extender:** The module used to manage and load your extensions.
* **BApp Store:** An in-app marketplace where you can download community-made tools.
* **Popular Community Extension:** **Logger++**, which provides a much more detailed history of all traffic moving through every Burp module, not just the Proxy.

---

## 🧠 Workflow Tip: The Right Tool for the Job

* Use **Proxy** for general browsing and finding interesting endpoints.
* Use **Repeater** once you find a specific request you want to "poke" repeatedly.
* Use **Intruder** only when you have a large list of data (like a wordlist) to test.

---

## 📝 Task 3 Answers

* **Which Burp Suite feature allows us to intercept requests between ourselves and the target?**
* `Proxy`


* **Which Burp tool would we use to brute-force a login form?**
* `Intruder`



---

## 🛠️ Data Transformation Quick-Reference (Decoder)

When you see data that looks like this in the Proxy, use **Decoder**:

* `%20`, `%27`, `%22` $\rightarrow$ **URL Encoding** (Space, Single Quote, Double Quote)
* `YWRtaW4=` $\rightarrow$ **Base64 Encoding** ("admin")
* `&#60;` $\rightarrow$ **HTML Entities** ("<")

---
# Burp Suite: The Basics — Task 4

## Installation

**TryHackMe Room Notes**

---

## 📌 Getting Burp Suite on Your Machine

Burp Suite is versatile and can be installed on almost any operating system thanks to its Java foundation. Whether you are using the provided **AttackBox** or your own **Mac** or **Kali Linux** setup, the process is straightforward.

### 🧱 Platform-Specific Guides

| Platform | Installation Method |
| --- | --- |
| **AttackBox** | **Pre-installed.** No action required. Just search for "Burp" in the applications menu. |
| **Kali Linux** | **Pre-installed.** If missing, run: `sudo apt update && sudo apt install burpsuite`. |
| **macOS** | Download the `.dmg` installer from PortSwigger. Drag and drop to Applications. |
| **Windows** | Download the `.exe` installer. Follow the setup wizard (defaults are fine). |
| **Linux (Other)** | Download the `.sh` script. Run it with `chmod +x` and execute. |

---

## ⚙️ Installation Best Practices

* **Use the Installer:** While Burp is available as a standalone `.jar` file, using the dedicated installers for Windows, macOS, or Linux is better because they include a **private Java Runtime Environment (JRE)**. This ensures Burp has the exact version of Java it needs to run smoothly.
* **Permissions (Linux):** If you install without `sudo`, Burp lives in your home directory (`~/BurpSuiteCommunity/`). This is safer for your system but means you'll have to manually add it to your PATH if you want to launch it from the terminal by just typing `burpsuite`.

---

## 🧠 Security Perspective: Keep it Updated

PortSwigger releases updates for Burp Suite frequently. These updates often include:

* **New BApp Store extensions.**
* **Security patches** for the internal browser.
* **New vulnerability definitions** for the issue library.
Always check the **Dashboard** (which we will cover next) for the update notification bar.

---

## 📝 Task 4 Answers

* **If you have chosen not to use the AttackBox, ensure you have a copy of Burp Suite installed...**
* `No answer needed`



---

## 🛠️ Launching Burp for the First Time

When you first open Burp, you will see a splash screen. For the Community Edition:

1. **Project Type:** You will be forced to select **"Temporary Project"** (Saving projects is a Pro feature).
2. **Configuration:** Choose **"Use Burp defaults"**.
3. **Start Burp:** Click the button and wait for the Dashboard to load.

---
# Burp Suite: The Basics — Task 5

## The Dashboard

**TryHackMe Room Notes**

---

## 📌 The Command Center

When you first launch Burp Suite, the **Dashboard** serves as your home base. It provides a bird's-eye view of what the application is doing in the background and, in the Professional version, what vulnerabilities it has found.

### 🧱 The Four Quadrants

The dashboard is split into four distinct sections. Understanding these helps you monitor your session's health and progress.

| Quadrant | Name | Purpose |
| --- | --- | --- |
| **Top Left** | **Tasks** | Displays background activities. Community users will mostly see the **"Live passive crawl,"** which silently maps out the site as you browse. |
| **Bottom Left** | **Event Log** | The "system logs" of Burp. It tells you if the proxy started successfully or if there are connection errors. |
| **Top Right** | **Issue Activity** | **(Pro Only)** Real-time feed of vulnerabilities found by the automated scanner. |
| **Bottom Right** | **Advisory** | **(Pro Only)** Detailed "vulnerability encyclopedia" providing descriptions and fix advice for items in Issue Activity. |

---

## ⚙️ Key Dashboard Features

* **The Help Icon (?):** Burp Suite has excellent built-in documentation. Every tab has a small question mark in the top corner; clicking it gives you a detailed explanation of every button in that specific view.
* **Update Notifications:** At the very top or bottom of the dashboard, Burp will notify you if a new version is available.
* **Health Monitoring:** If you see many red entries in the **Event Log**, it usually means your proxy or browser configuration is incorrect.

---

## 🧠 Why "Live Passive Crawl"?

Even in the Community edition, Burp is always working. As you visit pages through the Burp Proxy, the **Live Passive Crawl** task identifies every script, image, and sub-page. This builds the **Site Map** (which we will cover in later tasks), allowing you to see the entire structure of the web app without having to click every single link manually.

---

## 📝 Task 5 Answers

* **What menu provides information about the actions performed by Burp Suite, such as starting the proxy...?**
* `Event log`



---

## 🛠️ Dashboard Troubleshooting

If you are testing a site and nothing is showing up in Burp, check the **Event Log** for these common errors:

* **"Proxy service failed to start on port 8080":** Another app (like another Burp instance) is already using that port.
* **"The client failed to negotiate a TLS connection":** Usually means you haven't installed the Burp CA Certificate in your browser yet (covered in Task 13).

---
# Burp Suite: The Basics — Task 6

## Navigation

**TryHackMe Room Notes**

---

## 📌 Master the Interface

Burp Suite's interface is designed for speed and organization. Because you will often be jumping between "capturing" a request and "modifying" it, understanding the tab hierarchy and shortcuts is essential for a smooth workflow.

### 🧱 The Tab Hierarchy

Burp uses a two-tier menu system to keep its many tools organized:

1. **Main Modules (Top Row):** These are the major tools like **Proxy**, **Target**, **Intruder**, and **Repeater**.
2. **Sub-Tabs (Second Row):** Once you select a module, the second row changes to show specific functions. For example, selecting **Proxy** will show sub-tabs like **Intercept**, **HTTP history**, and **WebSockets history**.

---

## ⚙️ Detaching for Productivity

If you are working on a large monitor (like your **Mac** setup), you might find it helpful to see two tools at once.

* **The Detach Feature:** Found under the **Window** menu, this allows you to pull a tab (like **Repeater**) into its own separate window. This is perfect for side-by-side comparison of different requests.

---

## ⌨️ Speed Run: Keyboard Shortcuts

In the middle of a pentest, clicking through menus wastes time. Professional researchers use shortcuts to jump between the most important modules.

| Shortcut | Destination Tab |
| --- | --- |
| `Ctrl + Shift + D` | **Dashboard** |
| `Ctrl + Shift + T` | **Target** |
| `Ctrl + Shift + P` | **Proxy** |
| `Ctrl + Shift + I` | **Intruder** |
| `Ctrl + Shift + R` | **Repeater** |

> **Pro Tip:** You can also send a request from the **Proxy** directly to **Repeater** by pressing `Ctrl + R` while the request is selected!

---

## 📝 Task 6 Answers

* **Which tab Ctrl + Shift + P will switch us to?**
* `Proxy tab`



---

## 🛠️ Interface Navigation Cheat Sheet

* **The "Home" Key:** Always look at the top left module; it's usually where the core action is happening.
* **Filter Bar:** Many sub-tabs (like HTTP History) have a filter bar just below the sub-tabs. Clicking this allows you to hide "noise" (like images or CSS) so you only see the actual web requests.
* **The Intercept Button:** In the **Proxy > Intercept** tab, this is the most clicked button in Burp. It toggles whether traffic is paused or allowed to flow through.

---
