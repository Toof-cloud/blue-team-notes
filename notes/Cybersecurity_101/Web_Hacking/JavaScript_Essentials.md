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
# JavaScript Essentials — Task 5

## Abusing Dialogue Functions

**TryHackMe Room Notes**

---

## 📌 Interactive Dialogue Functions

JavaScript provides three primary functions for interacting with users via pop-up boxes. While they are useful for debugging or simple user input, they are also the most common "proof of concept" used during web penetration testing to demonstrate **Cross-Site Scripting (XSS)**.

### 🧱 The Three Main Functions

| Function | Purpose | Return Value | Pentesting Context |
| --- | --- | --- | --- |
| **`alert()`** | Displays information/warnings. | `undefined` | Used to prove a script can execute in a victim's browser. |
| **`prompt()`** | Asks for user input. | Entered String or `null` | Can be used to trick users into typing passwords or sensitive data. |
| **`confirm()`** | Asks for a Yes/No choice. | `true` or `false` | Can be used to trick a user into clicking "OK" for a malicious action. |

---

## 🧠 Security Perspective: Denial of Service (DoS)

As shown in the `invoice.html` example, simple loops can turn helpful functions into an "Inconvenience Attack." By wrapping an `alert()` inside a large `for` loop, an attacker can effectively lock a user's browser tab, as most browsers will not let you interact with the page until the dialogue is closed.

```javascript
for (let i = 0; i < 500; i++) {
    alert("This page is locked!");
}

```

### 🛡️ Why This Matters for XSS

When a security researcher finds a vulnerability, they often use `<script>alert(1)</script>`. This isn't meant to be malicious; it is a safe way to show that a vulnerability exists. If the `alert` pops up, it means the server didn't sanitize the input, and a real attacker could swap that `alert` for a script that steals your **session cookies**.

---

## 📝 Task 5 Answers

* **In the file invoice.html, how many times does the code show the alert Hacked?**
* `3`


* **Which of the JS interactive elements should be used to display a dialogue box that asks the user for input?**
* `prompt`


* **If the user enters Tesla, what value is stored in the carName variable?**
* `Tesla`



---

## 🛠️ Dialogue Quick-Code

| Task | Code Snippet |
| --- | --- |
| **Simple Notification** | `alert("System Update Required");` |
| **Data Capture** | `let user = prompt("Enter Username:");` |
| **Action Verification** | `let deleteFile = confirm("Delete permanently?");` |

---
# JavaScript Essentials — Task 6

## Bypassing Control Flow Statements

**TryHackMe Room Notes**

---

## 📌 Logic and Control Flow

Control flow is the "decision-making" engine of a script. It determines which path the code takes based on specific conditions. In cybersecurity, we often look for ways to manipulate these conditions to bypass security checks.

### 🧱 Conditional Statements

The most common structure is the `if-else` statement. It evaluates a condition in the parentheses; if it is **true**, the first block runs; if **false**, the `else` block runs.

* **Example:**

```javascript
if (age >= 18) {
    // This code runs if age is 18 or older
} else {
    // This code runs if age is 17 or younger
}

```

---

## 🧠 Security Perspective: Client-Side Bypass

One of the most critical lessons in web security is: **Never trust the client.**

If a developer writes login logic or "premium feature" checks entirely in JavaScript, a user can easily bypass them. Because JavaScript runs in *your* browser, you have full control over it.

### How to Bypass JS Logic:

1. **View Source:** Right-click and "View Page Source" to see the hardcoded credentials or the logic being used.
2. **Console Manipulation:** You can open the DevTools Console and simply overwrite the variables or functions. If a script checks `if (isLoggedIn)`, you can type `isLoggedIn = true` in the console to bypass the check.
3. **Breakpoint Debugging:** You can use the "Sources" tab in DevTools to pause the code right at the `if` statement and force it to take the "true" path.

---

## 📝 Task 6 Answers

* **What is the message displayed if you enter the age less than 18?**
* `You are a minor.`


* **What is the password for the user admin?**
* `p@ssw0rd123`
* *(Note: To find this, open the `login.html` file in the exercise folder, right-click, and select **View Page Source**. Look for the `if` statement comparing the password variable).*



---

## 🛠️ Comparison Operators Cheat Sheet

| Operator | Meaning | Example |
| --- | --- | --- |
| `==` | Equal to | `x == 5` |
| `===` | Strict equal (value & type) | `x === "5"` |
| `!=` | Not equal | `x != 10` |
| `>=` | Greater than or equal | `age >= 18` |
| `&&` | Logical AND | `user == "admin" && pass == "123"` |
| ` |  | ` |

---
# JavaScript Essentials — Task 7

## Exploring Minified & Obfuscated Files

**TryHackMe Room Notes**

---

## 📌 Minification vs. Obfuscation

In a production environment, you rarely see perfectly formatted JavaScript. Developers use tools to transform the code for two main reasons: performance and secrecy.

### 🧱 1. Minification

Minification is about **efficiency**. It removes all "noise" that the computer doesn't need to run the code.

* **Actions:** Removes spaces, newlines, and comments.
* **Goal:** Smaller file size = faster page loads.
* **Pentesting Tip:** Most browsers have a **"{ }" (Pretty Print)** button in the Sources tab that can instantly reverse minification by adding line breaks back in.

### ⚙️ 2. Obfuscation

Obfuscation is about **concealment**. It purposefully makes the code confusing for humans to prevent reverse-engineering.

* **Actions:** Renames `username` to `_0x1a2b`, converts strings to hex codes, and adds "junk" logic that does nothing.
* **Goal:** Protect intellectual property or hide malicious intent.
* **Pentesting Tip:** Attackers use obfuscation to hide malware. As a defender, you use "Deobfuscators" or "Beautifiers" to strip away the layers and find the original logic.

---

## 🧠 Decoding Obfuscated Values

In the task, you are given a mathematical expression disguised as obfuscated code:
`age = 0x1 * 0x247e + 0x35 * -0x2e + -0x1ae3;`

To solve this, you can simply paste the expression into your **Browser Console**. The browser will do the math for you.

1. `0x1 * 0x247e` = $9342$
2. `0x35 * -0x2e` = $53 * -46 = -2438$
3. `-0x1ae3` = $-6883$
4. **Total:** $9342 - 2438 - 6883 = 21$

---

## 📝 Task 7 Answers

* **What is the alert message shown after running the file hello.html?**
* `Welcome to THM`


* **What is the value of the age variable in the following obfuscated code snippet?**
* `21`
* *(Note: You can calculate this by typing the expression directly into the Chrome Console).*



---

## 🛠️ Deobfuscation Toolkit

| Tool Type | Purpose | Example Tool |
| --- | --- | --- |
| **Pretty Printer** | Fixes indentation/spacing. | Browser DevTools `{ }` |
| **Deobfuscator** | Renames variables and simplifies logic. | deobfuscate.io |
| **Hex Converter** | Decodes `\x41` into `A`. | CyberChef |

---
# JavaScript Essentials — Task 8

## Best Practices & Security

**TryHackMe Room Notes**

---

## 📌 Reducing the Attack Surface

When developing or auditing a web application, how JavaScript is handled determines whether the site is a "fortress" or a "screen door."

### 🧱 1. The Golden Rule: Never Trust the Client

Client-side validation (e.g., checking if an email has an `@` symbol) is great for user experience, but it is **not** security.

* **The Risk:** An attacker can use the browser console to bypass `if` statements or use tools like Burp Suite to send data directly to the server, skipping the JS checks entirely.
* **The Fix:** Always perform **Server-Side Validation**.

### ⚙️ 2. Supply Chain Security

Using the `src` attribute to link libraries (like jQuery or Bootstrap) is common, but risky.

* **The Risk:** Including a script from an untrusted or compromised CDN can lead to a **Supply Chain Attack**, where the malicious script steals your users' data.
* **The Fix:** Only use trusted sources and use **Subresource Integrity (SRI)** hashes to ensure the file hasn't been tampered with.

### 🔑 3. No Secrets in the Source

If you can see it in "View Page Source," so can the hackers.

* **The Risk:** Hardcoding API keys, passwords, or "hidden" admin URLs in `.js` files makes them public information.
* **The Fix:** Store secrets in environment variables on the server and use backend proxies for API calls.

---

## 📝 Task 8 Answers

* **Is it a good practice to blindly include JS in your code from any source (yea/nay)?**
* `nay`



---

## 🛠️ JavaScript Essentials: Room Cheat Sheet

### 1. Variables & Data

* **`let` / `const**`: Modern, block-scoped declarations.
* **`var`**: Older, function-scoped (avoid).
* **`console.log()`**: Prints data to the browser's developer console.

### 2. Dialogue Functions (XSS Proof-of-Concepts)

* **`alert()`**: Pop-up box for notifications.
* **`prompt()`**: Pop-up box for user input (returns a string).
* **`confirm()`**: Pop-up box for Yes/No (returns `true`/`false`).

### 3. Control Flow & DOM

* **`if (condition) { ... } else { ... }`**: Decision-making logic.
* **`for (let i=0; i < 10; i++) { ... }`**: Repeating actions.
* **`document.getElementById("id")`**: How JS finds HTML elements to modify them.

### 4. Code Protection

* **Minification**: Compressing code (removing spaces) for speed.
* **Obfuscation**: Making code unreadable to humans to hide logic.
* **Deobfuscation**: Using tools or the browser's "Pretty Print" `{ }` to make code readable again.

### 5. Pentester's Checklist

* [ ] Check "View Source" for hardcoded credentials/API keys.
* [ ] Look for external scripts (`src=`) from suspicious domains.
* [ ] Try to bypass client-side form validation by manipulating variables in the Console.
* [ ] Use "Pretty Print" on minified files to find hidden endpoints.

---
