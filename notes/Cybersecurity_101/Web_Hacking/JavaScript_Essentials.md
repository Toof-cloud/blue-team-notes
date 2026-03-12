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
# JavaScript Essentials — Task 3

## JavaScript Overview

**TryHackMe Room Notes**

---

## 📌 Interpreted vs. Compiled

Unlike languages like C++ or Java that need to be "compiled" into machine code before they can run, JavaScript is an **interpreted** language. This means the browser's engine (like Chrome's V8 engine) reads and executes the code line-by-line in real-time.

### 🖥️ The Browser Console: A Pentester's Playground

The Browser Console is the most direct way to interact with a web application's logic. By opening the DevTools (**Ctrl + Shift + I**), you can:

* **Test Snippets:** Run small pieces of code to see how the site behaves.
* **Modify Variables:** Change the values of variables in memory to bypass client-side checks.
* **Debug Logic:** See error messages that might reveal information about the server-side backend.

---

## 🧱 Dissecting the Code

In the example provided:

```javascript
let x = 10; // Variable declaration
let y = 10; 
let result = x + y; // Arithmetic expression
console.log("The result is: " + result); // Output function

```

* **`let`**: Declares the variables $x$ and $y$.
* **`console.log()`**: This is the standard way to output data to the developer tools. It does not appear on the actual webpage, making it a "hidden" log for developers (and curious hackers).

---

## 📝 Task 3 Answers

* **What is the code output if the value of x is changed to 10?**
* `The result is: 20`
* *(Calculation: $10 + 10 = 20$)*


* **Is JavaScript a compiled or interpreted language?**
* `Interpreted`



---

## 🛠️ Browser Console Shortcuts

| Action | Shortcut (Windows/Linux) |
| --- | --- |
| **Open DevTools** | `Ctrl + Shift + I` |
| **Clear Console** | `Ctrl + L` |
| **Multiline Code** | `Shift + Enter` |
| **Inspect Element** | `Ctrl + Shift + C` |

---
# JavaScript Essentials — Task 4

## Integrating JavaScript in HTML

**TryHackMe Room Notes**

---

## 📌 How JavaScript Lives in HTML

JavaScript doesn't just run in a vacuum; it needs to be "hooked" into an HTML document. There are two primary ways a developer (or an attacker) can inject logic into a page.

### 🧱 1. Internal JavaScript

Code is written directly inside the HTML file using `<script>` tags.

* **Pros:** Easy for small tasks; all code is in one place.
* **Cons:** Makes HTML files bulky and hard to manage as they grow.
* **Pentesting Tip:** When you see internal scripts, look for "hardcoded" secrets like API keys or sensitive logic directly in the source code.

### ⚙️ 2. External JavaScript

Code is stored in a separate `.js` file and linked using the `src` attribute.

* **Syntax:** `<script src="filename.js"></script>`
* **Pros:** Organized, cached by the browser for speed, and reusable across multiple pages.
* **Pentesting Tip:** Attackers check external files for vulnerabilities in the logic. If a site loads a script from a third-party (like a CDN), an attacker might try to compromise that third party to inject malicious code into the target site.

---

## 🧠 Interacting with the DOM

In the example code:
`document.getElementById("result").innerHTML = ...`
This is a core JS concept called **DOM Manipulation**.

* **`document`**: Refers to the entire HTML page.
* **`getElementById("result")`**: Finds the specific HTML tag with `id="result"`.
* **`.innerHTML`**: Changes the text inside that tag.

---

## 📝 Task 4 Answers

* **Which type of JavaScript integration places the code directly within the HTML document?**
* `Internal JavaScript`


* **Which method is better for reusing JS across multiple web pages?**
* `External JavaScript`


* **What is the name of the external JS file that is being called by external_test.html?**
* `test.js`
* *(Note: You can find this by right-clicking `external_test.html` in the exercise folder and selecting **View Page Source**)*.


* **What attribute links an external JS file in the <script> tag?**
* `src`



---

## 🛠️ JS Integration Reference

| Method | Syntax | Best Used For |
| --- | --- | --- |
| **Internal** | `<script> console.log("Hi"); </script>` | Page-specific logic or rapid testing. |
| **External** | `<script src="assets/app.js"></script>` | Reusable logic and professional apps. |
| **Inline** | `<button onclick="alert('Hi')">` | Simple interactions (avoid for security). |

---
