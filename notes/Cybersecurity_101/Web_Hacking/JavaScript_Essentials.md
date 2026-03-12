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
# JavaScript Essentials — Task 2

## Essential Concepts

**TryHackMe Room Notes**

---

## 📌 The Building Blocks of JS

To understand how to exploit or defend JavaScript, you first need to understand its core syntax. JS is dynamically typed and uses a C-style syntax.

### 🧱 1. Variables (The Containers)

Variables store data that can be referenced and manipulated. In modern JS, we use three keywords to declare them:

* **`var`**: The "old" way. It is function-scoped and can lead to bugs because it allows for variable hoisting.
* **`let`**: The modern standard. It is **block-scoped** (lives only within `{ }`), making code more predictable.
* **`const`**: Short for "constant." Once assigned, its value cannot be changed. Use this for data that should remain static.

### 📊 2. Data Types

JS handles different types of data automatically:

* **String**: Text inside quotes, e.g., `"Hello"`.
* **Number**: Integers or decimals, e.g., `10` or `3.14`.
* **Boolean**: Logic values, `true` or `false`.
* **Undefined**: A variable that has been declared but not assigned a value.
* **Null**: An intentional absence of any value.
* **Object**: Complex data structures, including **Arrays** (lists).

### ⚙️ 3. Functions

A function is a reusable block of code designed to perform a specific task. You "call" a function whenever you need that logic to run.

### 🔄 4. Loops

Loops allow you to repeat a task without writing the same code over and over.

* **`for` loop**: Used when you know exactly how many times you want to run (e.g., "Run this 100 times").
* **`while` loop**: Runs as long as a specific condition is `true`.

---

## 🧠 Security Perspective: Loop Logic & Undefined Data

In the example code provided in the task:

```javascript
const rollNumbers = [101, 102, 103];
for (let i = 0; i < 100; i++) {
    PrintResult(rollNumbers[i]);
}

```

**Observation:** The array only has 3 items, but the loop runs 100 times. From index 3 to 99, `rollNumbers[i]` will return `undefined`. In a real application, if the code doesn't handle `undefined` properly, it could lead to an application crash or reveal sensitive logic in the console errors—information an attacker can use to understand the internal data structure.

---

## 📝 Task 2 Answers

* **What term allows you to run a code block multiple times as long as it is a condition?**
* `Loops`



---

## 🛠️ JavaScript Syntax Cheat Sheet

| Feature | Syntax Example |
| --- | --- |
| **Declaration** | `let name = "THM";` |
| **Function** | `function greet() { ... }` |
| **For Loop** | `for (let i=0; i < 5; i++) { ... }` |
| **If Statement** | `if (condition) { ... } else { ... }` |

---
