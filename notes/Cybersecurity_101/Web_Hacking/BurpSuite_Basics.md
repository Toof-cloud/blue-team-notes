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
