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
