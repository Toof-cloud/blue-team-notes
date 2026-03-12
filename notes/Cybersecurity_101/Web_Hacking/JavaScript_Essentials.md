# JavaScript Essentials — Task 1

## Introduction

**TryHackMe Room Notes**

---

## 📌 The "Brain" of the Web

While HTML provides the structure and CSS provides the style, **JavaScript (JS)** provides the logic. It is a client-side scripting language, meaning the code is executed directly in the user's browser rather than on the server.

From a security perspective, JavaScript is the primary vector for **Client-Side Attacks**. Because the browser trusts and executes the JS it receives, attackers can use it to steal cookies, redirect users, or capture keystrokes.

### 🎯 Learning Objectives:

* **JS Fundamentals:** Variables, data types, and functions.
* **HTML Integration:** How scripts are loaded and executed within a page.
* **Dialogue Abuse:** Understanding `alert()`, `prompt()`, and `confirm()` (and how they are used in XSS).
* **Control Flow Bypassing:** Analyzing how logic gates (if/else) can be manipulated.
* **Deobfuscation:** Learning to read "minified" or "obfuscated" code to find hidden API keys or logic.

---

## 🛠️ Security Context: The Cyber Perspective

In this room, we aren't just learning to code; we are learning to **reverse-engineer** intent.

1. **Legitimate Use:** A developer uses JS to validate a password format before it's sent to the server.
2. **Malicious Use:** A hacker bypasses that JS validation to send a "malformed" payload (like SQL injection) directly to the database.

> **Note:** If you are using the AttackBox or your own VM, ensure you can access the `exercise` folder on the Desktop, as it contains the source code for the practical challenges ahead.

---

## 📝 Task 1 Answers

* **I have successfully started the attached VM.**
* `No answer needed`



---

## 🛠️ JavaScript Quick-Look

| Feature | Description |
| --- | --- |
| **Client-Side** | Executed by the browser (Chrome, Firefox, Brave). |
| **Interactivity** | Handles clicks, form submissions, and animations. |
| **XSS Vector** | The primary language used in Cross-Site Scripting attacks. |
| **DOM** | The "Document Object Model" — how JS "talks" to HTML elements. |

---
