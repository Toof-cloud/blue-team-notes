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
# Burp Suite: The Basics — Task 7

## Options and Settings

**TryHackMe Room Notes**

---

## 📌 User vs. Project Settings

Configuring Burp Suite correctly is the difference between a cluttered workspace and an efficient one. Burp divides its settings into two distinct scopes to give you maximum control.

### 🧱 1. User Settings (Global)

These settings follow **you**, the user. They are saved to your local machine and applied every time you open Burp.

* **Examples:** Display themes (Dark Mode!), keyboard shortcuts, and update preferences.
* **Best For:** Personalizing your environment so it feels consistent across every engagement.

### 🧱 2. Project Settings

These settings follow the **target**. They are specific to the individual work you are doing right now.

* **Examples:** Scope definitions, specific proxy listeners, and handling session cookies.
* **⚠️ Community Note:** Since Community Edition doesn't allow saving projects, these settings are wiped every time you close the application.

---

## ⚙️ Navigating the Settings Window

The settings menu in modern Burp versions is centralized. You can access it via the **Settings** button in the top navigation bar.

* **The Search Bar:** This is the most efficient way to find a setting. Instead of clicking through categories, type "Hotkeys" or "Proxy" to jump straight there.
* **Categories:** Settings are grouped logically (e.g., Network, Tools, User Interface).
* **Contextual Shortcuts:** Many modules have a "Settings" button within their own tab that acts as a shortcut to the relevant section in the main Settings window.

---

## 🧠 Security Perspective: The Cookie Jar

Burp maintains a **"Cookie Jar"** in the background. As you browse, it stores the cookies set by the server.

* **Why it matters:** Other Burp tools (like Scanner or Intruder) can use the cookies in the jar to maintain a valid session while performing automated attacks. This prevents you from being logged out mid-test.

---

## 📝 Task 7 Answers

* **In which category can you find a reference to a "Cookie jar"?**
* `Sessions`


* **In which base category can you find the "Updates" sub-category...?**
* `Suite`


* **What is the name of the sub-category which allows you to change the keybindings...?**
* `Hotkeys`


* **If we have uploaded Client-Side TLS certificates, can we override these on a per-project basis (yea/nay)?**
* `yea`



---

## 🛠️ Settings Quick-Tips

| Feature | Tip |
| --- | --- |
| **Dark Mode** | Go to **User Interface > Display** and change the "Look and feel" to **Darcula**. |
| **Font Size** | If the text is too small on your high-res Mac screen, adjust it in **User Interface > Display**. |
| **Proxy Port** | If port 8080 is blocked, search for **Proxy Listener** to change it to 8081 or 8888. |

---
# Burp Suite: The Basics — Task 8

## Introduction to the Burp Proxy

**TryHackMe Room Notes**

---

## 📌 The Heart of the Suite

The Burp **Proxy** is the most vital component of your testing workflow. It sits between your browser and the web server, acting as a gateway that allows you to see, stop, and change data as it travels across the wire.

### 🧱 The Interception Cycle

When the **Intercept** feature is enabled, Burp Suite "freezes" the request. This gives you time to look at the raw data before the server ever receives it.

* **Forward:** Sends the request (and any changes you made) to the server.
* **Drop:** Deletes the request. The server will never know you tried to send it, and the browser will show a loading error.
* **Intercept is on/off:** Toggles whether you want to stop every single request or just let them flow through while logging them in the background.

---

## ⚙️ History vs. Intercept

Even when "Intercept is off," Burp is still working as a proxy.

1. **Intercept Tab:** For real-time "live" modification of a single request.
2. **HTTP History Tab:** A chronological log of every request and response that has passed through the proxy.
* **Pro Tip:** This is incredibly useful for finding "background" requests like API calls or JavaScript files that you might have missed while browsing.



---

## 🔍 Advanced Proxy Features

The Proxy isn't just a simple "pause" button; it has powerful automation settings:

* **Response Interception:** By default, Burp only stops outgoing requests. You can change the settings to also stop **responses** from the server, allowing you to modify the HTML or JavaScript before your browser renders it.
* **Match and Replace:** You can set rules to automatically change data.
* *Example:* Automatically change your `User-Agent` to look like an iPhone, even if you are on your **Mac**.
* *Example:* Automatically replace "Admin: False" with "Admin: True" in every cookie that passes through.



---

## 🧠 Security Perspective: WebSocket Interception

Modern "live" web apps often use **WebSockets** for real-time communication (like chat apps or stock tickers). Unlike standard HTTP, WebSockets keep a persistent connection open. Burp Proxy captures these too in the **WebSockets history** tab, allowing you to intercept binary or text data that usually bypasses standard logging.

---

## 📝 Task 8 Answers

* **Click me to proceed to the next task.**
* `No answer needed`



---

## 🛠️ Proxy Quick-Reference

| Action | Shortcut (while in Intercept) |
| --- | --- |
| **Forward Request** | `Ctrl + F` |
| **Send to Repeater** | `Ctrl + R` |
| **Send to Intruder** | `Ctrl + I` |
| **Toggle Intercept** | Click the "Intercept is on/off" button |

---
# Burp Suite: The Basics — Task 9

## Connecting through the Proxy (FoxyProxy)

**TryHackMe Room Notes**

---

## 📌 Why Use FoxyProxy?

By default, your browser sends traffic directly to the internet. To use Burp, we must tell the browser: *"Stop! Send everything to `127.0.0.1:8080` (Burp) first."* While you can change this in your browser's deep settings, **FoxyProxy** is the industry-standard browser extension that allows you to toggle this connection on and off with a single click.

### 🧱 Configuration Details

To link your browser to Burp Suite, use the following standard parameters:

* **Proxy IP:** `127.0.0.1` (This refers to "localhost" or your own machine).
* **Port:** `8080` (The default port where Burp's Proxy listener "sits" and waits for data).
* **Type:** HTTP

---

## ⚙️ The Interception Workflow

Once FoxyProxy is active and pointing to Burp, your browsing experience changes:

1. **Activate FoxyProxy:** Select your "Burp" profile in the browser.
2. **Enable Intercept:** In Burp Suite, go to **Proxy > Intercept** and ensure the button says **"Intercept is on"**.
3. **The "Hang":** When you navigate to a site (like `http://MACHINE_IP`), the browser will look like it's loading forever. **This is normal.** It means Burp has successfully caught the request and is waiting for your command.
4. **Forward/Drop:** You now decide the fate of that request in the Burp window.

---

## 🔍 Troubleshooting the Connection

If you enable FoxyProxy and see an "Unable to connect" error in your browser, check these three things:

* **Is Burp running?** The proxy won't work if the "receiver" (Burp) isn't open.
* **Is the Port correct?** Check **Settings > Network > Proxy** in Burp to ensure the listener is actually on `8080`.
* **Is Intercept off?** If the browser is hanging but you don't see anything in the Intercept tab, you might have another request already waiting for a "Forward" or "Drop" click.

---

## 🧠 Security Perspective: Noise Reduction

Browsers are noisy! Even if you only want to look at one website, your browser is constantly sending requests to:

* Google (for search suggestions).
* Browser developers (for telemetry/updates).
* Various extensions.

**Pro Tip:** Before you turn on "Intercept," close all other browser tabs. This prevents Burp from being flooded with "junk" requests that have nothing to do with your target.

---

## 📝 Task 9 Answers

* **Click me to proceed to the next task.**
* `No answer needed`



---

## 🛠️ Right-Click Power Actions

Once a request is caught in the Proxy, right-clicking it opens a world of possibilities:

* **Send to Repeater (`Ctrl + R`):** Perfect for when you want to try different inputs on that specific page.
* **Send to Intruder (`Ctrl + I`):** For when you want to automate a brute-force attack.
* **Change Request Method:** Instantly swap a `GET` request to a `POST` request.

---
# Burp Suite: The Basics — Task 10

## Site Map and Issue Definitions

**TryHackMe Room Notes**

---

## 📌 Mapping the Attack Surface

The **Target** tab is where Burp Suite organizes everything it knows about the web applications you are testing. While the Proxy shows you a "live stream" of traffic, the Target tab acts as the "librarian," filing every request into a logical structure.

### 🧱 The Three Sub-Tabs

| Sub-Tab | Purpose | Key Benefit |
| --- | --- | --- |
| **Site Map** | A hierarchical tree view of the target. | Automatically organizes folders and files (e.g., `/assets`, `/api`, `/admin`) as you browse. |
| **Issue Definitions** | A built-in vulnerability encyclopedia. | Provides a massive list of web flaws (like XSS, SQLi) with descriptions and remediation advice. |
| **Scope Settings** | Defines the "In-Scope" targets. | Tells Burp to ignore traffic from unrelated sites (like your background Spotify or Google tabs). |

---

## ⚙️ Enumeration via Browsing

Even without the Professional automated scanner, you can perform **Passive Crawling**.

* As you click through the target website on your **Mac** or **Kali** browser, Burp watches every request.
* It populates the Site Map with scripts (`.js`), stylesheets (`.css`), and hidden endpoints that you might not see on the page but are loaded in the background.
* **Pro Tip:** Look for grayed-out items in the Site Map. These are URLs that Burp has *inferred* exist (from links found in other pages) but you haven't actually visited yet.

---

## 🔍 Issue Definitions: The Pentester’s Cheat Sheet

While the Community Edition doesn't automatically find bugs, the **Issue Definitions** tab is an invaluable learning resource.

* If you suspect a site is vulnerable to **"Cross-Origin Resource Sharing (CORS) Misconfiguration,"** you can search for it here.
* Burp will provide a detailed breakdown of the risk and how a developer should fix it. This is excellent for writing professional reports.

---

## 🧠 Security Perspective: Finding the "Hidden"

Attackers love the Site Map because it often reveals **API endpoints** and **development artifacts**. For example, a website might fetch data from `/api/v1/user/details`. Even if that URL isn't in your browser's address bar, Burp will catch it, allowing you to right-click it and send it to **Repeater** for further testing.

---

## 📝 Task 10 Answers

* **What is the flag you receive after visiting the unusual endpoint?**
* `THM{NmNlZDI4NjdiZGMzZGUzOTI2YmIyN2Vj}`
* *(Method: Browse the site thoroughly. Look at your Site Map for an endpoint that doesn't look like a standard page, such as `/secret-flag-path` or a similar hidden directory.)*



---

## 🛠️ Site Map Navigation Tips

* **Right-Click > Show only in-scope items:** Cleans up the "noise" so you only see your target.
* **Right-Click > Engagement Tools (Pro Only):** Allows for automated discovery, but in Community, you'll be doing this manually by clicking every link you find.

---
# Burp Suite: The Basics — Task 11

## The Burp Suite Browser

**TryHackMe Room Notes**

---

## 📌 The "Easy Button" for Interception

If configuring FoxyProxy or messing with system certificates feels tedious, Burp Suite provides a built-in solution: the **Burp Browser**. This is a modified version of **Chromium** that comes bundled with Burp Suite and is hard-wired to send all traffic through the Proxy automatically.

### 🧱 Why Use the Built-in Browser?

* **Zero Configuration:** You don't need to change any settings in your OS or primary browser (like Brave or Safari).
* **Pre-installed Certificates:** It already trusts Burp’s Certificate Authority (CA), meaning it can handle HTTPS traffic out of the box.
* **Isolation:** It keeps your pentesting traffic separate from your personal browsing, preventing "noise" from other tabs or extensions from cluttering your Burp history.

---

## ⚙️ The "Sandbox" Issue on Linux

If you are using **Kali Linux** (likely in your VM) or the **AttackBox** and running as the `root` user, the browser might fail to launch. This is a security feature of Chromium—it refuses to run a "Sandbox" (an isolated environment) when the user has full system administrative privileges.

### 🛠️ How to Fix It:

1. **The Recommended Way:** Run Burp as a standard, non-root user.
2. **The Quick Way (for Labs):** * Go to **Settings > Tools > Burp's browser**.
* Check the box: **"Allow Burp's browser to run without a sandbox"**.
* *Warning:* Only do this in a lab environment. Running a browser without a sandbox means if you visit a malicious site that exploits the browser, it has direct access to your system.



---

## 🧠 Navigation Tip: Finding the Browser

You can launch it by going to the **Proxy** tab and selecting the **Intercept** sub-tab. The big **Open Browser** button will be right there next to the Intercept toggle.

---

## 📝 Task 11 Answers

* **Click me to proceed to the next task.**
* `No answer needed`



---

## 🛠️ Burp Browser vs. External Browser

| Feature | Burp Browser | External (Firefox/Brave) |
| --- | --- | --- |
| **Setup Time** | Instant | Requires FoxyProxy + CA Cert |
| **HTTPS Support** | Automatic | Manual Setup Required |
| **Extensions** | Limited | Use your favorite tools |
| **Stability** | Very High | High |

---
# Burp Suite: The Basics — Task 12

## Scoping and Targeting

**TryHackMe Room Notes**

---

## 📌 The "Noise" Problem

When you start a pentest, your browser is likely sending requests to dozens of domains—Google Analytics, browser telemetry, background extensions, and CDNs. If Burp intercepts everything, your **HTTP History** and **Intercept** tab will be flooded with "noise," making it impossible to find the actual vulnerabilities in your target.

### 🧱 What is Scoping?

**Scoping** is the process of telling Burp Suite exactly which domains or IP addresses you are legally allowed (or personally interested) to test.

* **In-Scope:** Your target (e.g., `http://10.10.x.x/`).
* **Out-of-Scope:** Everything else (e.g., `google.com`, `mozilla.net`).

---

## ⚙️ How to Set Your Scope

There are two ways to define your target scope:

1. **The Easy Way:** Go to the **Target > Site map** tab. Right-click the folder representing your target machine and select **Add to scope**.
2. **The Manual Way:** Go to **Target > Scope settings**. Here you can use prefixes or even **Regex** (Regular Expressions) to include or exclude specific subdomains or folders.

---

## 🔍 The "Double Lock" Configuration

Adding a target to your scope is only the first step. To truly clean up your workspace, you must tell Burp's modules to respect that scope.

### 1. Cleaning the History

When you add a target to the scope, Burp will ask: *"Do you want to stop logging out-of-scope items?"* * Selecting **Yes** prevents your **HTTP History** from filling up with junk.

### 2. Silencing the Proxy (Crucial)

By default, the **Proxy Intercept** will still stop *every* request, even if it's out of scope. To fix this:

1. Go to **Settings > Tools > Proxy**.
2. Find the **Intercept Client Requests** section.
3. Add or enable the rule: `And | URL | Is in target scope`.

---

## 🧠 Security Perspective: Legal Safety

In a professional environment, scoping isn't just for convenience—it's for **legal protection**. Attacking a server that is not listed in your "Rules of Engagement" (RoE) can have serious legal consequences. By strictly enforcing your scope within Burp, you ensure that you don't accidentally send a malicious payload to a third-party service integrated into the web app.

---

## 📝 Task 12 Answers

* **Add http://MACHINE_IP/ to your scope... See the difference...**
* `No answer needed`



---

## 🛠️ Scoping Cheat Sheet

| Goal | Action |
| --- | --- |
| **Hide background noise** | `Target > Site map > Filter bar > "Show only in-scope items"` |
| **Ignore subdomains** | Use `Exclude from scope` for specific folders in the Site Map. |
| **Reset Intercept** | If you accidentally "Forward" a request you didn't mean to, check the **HTTP History** to see what was sent. |

---
# Burp Suite: The Basics — Task 13

## Proxying HTTPS

**TryHackMe Room Notes**

---

## 📌 The Encryption Hurdle

When you use a proxy to intercept **HTTPS** traffic, you are essentially performing a **Man-in-the-Middle (MITM)**. Under normal circumstances, your browser expects a certificate signed by a known "Certificate Authority" (CA) like DigiCert or Let's Encrypt.

Because Burp Suite needs to read your encrypted data, it creates its own certificate to "pretend" to be the website you are visiting. Browsers (like the one on your **Mac** or **Kali** VM) will see this unrecognized certificate and block the connection for your safety.

---

## ⚙️ How to Trust the Burp CA

To fix this, you must tell your browser that PortSwigger (Burp's creator) is a trusted authority. Once trusted, your browser will allow Burp to decrypt and re-encrypt traffic seamlessly.

### 🧱 The 3-Step Setup

1. **Download the Certificate:** * Ensure FoxyProxy is **ON** and pointing to Burp.
* In your browser, go to `http://burp/cert`.
* A file named `cacert.der` will download.


2. **Import to Browser:** * In Firefox, go to `about:preferences` and search for **Certificates**.
* Click **View Certificates** -> **Authorities** -> **Import**.
* Select the `cacert.der` file.


3. **Establish Trust:** * **CRITICAL:** When the pop-up appears, you must check the box: **"Trust this CA to identify websites"**.
* Click OK and restart your browser.



---

## 🔍 Why `http://burp`?

Burp Suite hosts a tiny local web server on its listener port (usually `8080`). When you type `http://burp` while the proxy is active, Burp intercepts that request itself and serves a special internal page where you can download the certificate or check your connection status.

---

## 🧠 Security Perspective: The "Privacy" Trade-off

By installing this certificate, you are giving Burp Suite the power to see **everything** you do in that browser, including passwords and banking details if you visit those sites.

* **Pentesting Best Practice:** Never install the Burp CA in your "daily driver" browser where you check personal email or social media. Keep a dedicated browser (like Firefox Developer Edition or the built-in Burp Browser) specifically for security work.

---

## 📝 Task 13 Answers

* **If you are not using the AttackBox, configure Firefox... to accept the PortSwigger CA certificate.**
* `No answer needed`



---

## 🛠️ HTTPS Troubleshooting

If you still see "Secure Connection Failed" after importing:

* **Check the Date:** Ensure your system clock is correct. Certificates are time-sensitive.
* **Double Check Trust:** Go back to the Certificate Manager, find "PortSwigger," click **Edit Trust**, and ensure the checkbox is actually checked.
* **HSTS Sites:** Some sites (like Google or Facebook) use **HSTS**, which is extra strict. If the certificate isn't perfect, they will block it entirely with no "Advanced > Proceed" option.

---
# Burp Suite: The Basics — Task 14

## Example Attack: Bypassing Client-Side Filters

**TryHackMe Room Notes**

---

## 📌 The Vulnerability: Reflected XSS

This task demonstrates a classic **Cross-Site Scripting (XSS)** attack. In this scenario, the web application takes input from the user and "reflects" it back onto the page. If the input isn't properly cleaned, an attacker can inject JavaScript that the browser will execute.

### 🧱 Why Burp is Necessary

Many websites use **Client-Side Filtering** (JavaScript running in your browser) to validate inputs. For example, an email field might block the `<` or `>` characters.

* **The Weakness:** Client-side filters can be seen and bypassed by the user.
* **The Solution:** We send "clean" data to the browser's filter, catch the request in **Burp Proxy**, and swap it for our "malicious" payload before it ever reaches the server.

---

## ⚙️ The Attack Workflow

1. **Preparation:** Turn **Intercept ON** in Burp.
2. **The "Lies":** Enter a valid email (e.g., `test@example.com`) to satisfy the browser's filter.
3. **The Interception:** Click submit. Burp catches the request.
4. **The Swap:** Replace the email address with your payload: `<script>alert("Succ3ssful XSS")</script>`.
5. **The Encoding:** Highlight the payload and press **`Ctrl + U`**. This converts characters like `<` into `%3c` so the web server doesn't get confused by the raw HTML.
6. **The Execution:** Click **Forward**.

---

## 🧠 Security Perspective: Defense in Depth

This attack proves a fundamental rule of web security: **Never trust the client.** * A developer must implement **Server-Side Validation**.

* Even if the browser's JavaScript says the data is "safe," the server must re-check the data before displaying it or storing it in a database.

---

## 📝 Task 14 Answers

* **Click me to proceed to the next task.**
* `No answer needed`



---

## 🛠️ Burp Suite Basics Final Cheat Sheet

### ⌨️ Essential Hotkeys

| Action | Shortcut |
| --- | --- |
| **Forward Request** | `Ctrl + F` |
| **Send to Repeater** | `Ctrl + R` |
| **Send to Intruder** | `Ctrl + I` |
| **URL Encode** | `Ctrl + U` |
| **URL Decode** | `Ctrl + Shift + U` |

### 📂 Module Quick-Reference

* **Proxy:** Intercept and modify traffic "live."
* **Target:** View the site map and define what you are allowed to attack.
* **Repeater:** Manually resend a single request over and over with different payloads.
* **Intruder:** Brute-force logins or fuzz parameters using wordlists.
* **Decoder:** Quickly convert Base64, Hex, or URL encoding.
* **Settings:** Change your theme (Darcula), hotkeys, and CA certificates.

---
