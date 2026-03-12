# Web Application Basics — Task 1

## Introduction

**TryHackMe Room Notes**

---

## 📌 Room Overview

Transitioning from network-level exploitation (like EternalBlue) to **Web Application Security** requires a solid understanding of how the web actually functions. This room covers the fundamental "language" of the internet: **HTTP**.

### 🎯 Learning Objectives:

* **Web App Architecture:** How browsers interact with servers.
* **URL Anatomy:** Decoding the strings we type into the address bar.
* **The Request/Response Cycle:** The backbone of web communication.
* **HTTP Verbs:** Understanding GET, POST, PUT, and DELETE.
* **Status Codes:** What "404 Not Found" or "200 OK" actually tells us.
* **Headers & Security:** How metadata controls browser behavior and protects users.

---

## 🧱 Why This Matters for Pentesting

In previous rooms, we used Metasploit to attack services like SMB. In web hacking, your "exploit" is often a specially crafted **HTTP Request**. Whether you are performing SQL Injection, Cross-Site Scripting (XSS), or IDOR, you are essentially manipulating the components discussed in this room to make a web server behave in ways it wasn't intended to.

### The Basic Cycle:

1. **The Client (Browser):** Sends an **HTTP Request**.
2. **The Server:** Processes the request and sends back an **HTTP Response**.

---

## 📝 Task 1 Answers

* **I am ready to learn about Web Applications!**
* `No answer needed`



---

## 🛠️ Web Basics Cheat Sheet (Ongoing)

| Component | Description |
| --- | --- |
| **HTTP** | HyperText Transfer Protocol — the protocol used for transmitting web pages. |
| **URL** | Uniform Resource Locator — the address used to find a resource on the web. |
| **Client** | Usually a web browser (Chrome, Firefox, Brave) or a tool like `curl`. |
| **Server** | Software (Apache, Nginx) that "serves" the web content to the client. |

---
# Web Application Basics — Task 2

## Web Application Overview

**TryHackMe Room Notes**

---

## 📌 The Anatomy of a Web App

Using the planet analogy, a web application is split into what is visible on the "surface" and the complex systems working "underground."

### 🎨 The Front End (The Surface)

The front end is everything the user sees and interacts with directly in their **Web Browser**.

* **HTML (The Structure):** The "skeleton" or DNA. It tells the browser *what* content to show (headings, paragraphs, buttons).
* **CSS (The Style):** The "skin" and aesthetics. It handles colors, fonts, and the overall layout.
* **JavaScript (The Logic):** The "brain." It makes the page interactive, allowing for features like pop-ups, data validation, and dynamic content updates.

### ⚙️ The Back End (Under the Surface)

The back end is the engine room. It processes data and serves the front end to the user.

* **Web Server:** The software (like Apache or Nginx) that listens for requests and sends back the requested files.
* **Database:** The "library" or "filing cabinet" where user data, passwords, and site content are stored (e.g., MySQL, PostgreSQL).
* **Infrastructure:** The "roads and fuel"—the physical or virtual servers, networking cables, and storage that keep the application running.
* **WAF (Web Application Firewall):** The "atmosphere." It sits in front of the web server to filter out malicious traffic like SQL injection or Cross-Site Scripting (XSS).

---

## 📝 Task 2 Answers

* **Which component on a computer is responsible for hosting and delivering content for web applications?**
* `Web Server`


* **Which tool is used to access and interact with web applications?**
* `Web Browser`


* **Which component acts as a protective layer, filtering incoming traffic to block malicious attacks, and ensuring the security of the web application?**
* `WAF`



---

## 🛠️ Web Basics Cheat Sheet (Updated)

| Component | Responsibility |
| --- | --- |
| **HTML** | Structure and Content |
| **CSS** | Presentation and Styling |
| **JavaScript** | Interactivity and Logic |
| **Database** | Persistent Data Storage |
| **WAF** | Traffic Filtering and Security |

---
# Web Application Basics — Task 3

## Uniform Resource Locator (URL)

**TryHackMe Room Notes**

---

## 📌 Anatomy of a URL

A URL is more than just a "web address"; it is a structured set of instructions that tells your browser exactly which protocol to use, which server to contact, and which specific resource to retrieve.

### 🧱 Breaking Down the URL

| Component | Example | Description |
| --- | --- | --- |
| **Scheme** | `https://` | The protocol (rules) used. `HTTPS` is the secure, encrypted version of `HTTP`. |
| **User** | `admin@` | Optional authentication info. Rare today as it is a security risk. |
| **Host/Domain** | `tryhackme.com` | The unique name of the website server. |
| **Port** | `:443` | The specific "doorway" on the server. Default for HTTP is **80**; HTTPS is **443**. |
| **Path** | `/room/basics` | The specific location of the file or page on the server. |
| **Query String** | `?id=1&name=thm` | Key-value pairs used to pass data to the server (starts with `?`). |
| **Fragment** | `#task3` | An internal page anchor to jump to a specific section (starts with `#`). |

---

## 🧠 Security Implications

Understanding URLs is vital for cybersecurity:

* **Typosquatting:** Attackers register domains like `g00gle.com` instead of `google.com` to trick users into visiting phishing sites.
* **Injection Attacks:** Because users can edit the **Query String** and **Fragment** in their browser, attackers often try to insert malicious code (like SQLi or XSS) into these fields.
* **Sensitive Paths:** Sometimes developers leave sensitive paths (like `/admin` or `/.env`) exposed, which can be discovered through directory brute-forcing.

---

## 📝 Task 3 Answers

* **Which protocol provides encrypted communication to ensure secure data transmission between a web browser and a web server?**
* `HTTPS`


* **What term describes the practice of registering domain names that are misspelt variations of popular websites to exploit user errors and potentially engage in fraudulent activities?**
* `Typosquatting`


* **What part of a URL is used to pass additional information, such as search terms or form inputs, to the web server?**
* `Query String`



---

## 🛠️ URL Reference Table

| Protocol | Default Port | Security Level |
| --- | --- | --- |
| **HTTP** | 80 | Unencrypted (Vulnerable to sniffing) |
| **HTTPS** | 443 | Encrypted (TLS/SSL) |
| **FTP** | 21 | File Transfer |
| **SSH** | 22 | Secure Remote Access |

---
# Web Application Basics — Task 4

## HTTP Messages

**TryHackMe Room Notes**

---

## 📌 The Dialogue of the Web

Communication between your browser (the client) and a web server happens through **HTTP Messages**. These are structured data packets that ensure both sides understand the intent of the communication.

### 🧱 The 4-Part Message Structure

Whether it is a request or a response, every HTTP message follows the same general layout:

1. **Start Line:** * **In a Request:** Contains the method (GET/POST), the path, and the HTTP version.
* **In a Response:** Contains the HTTP version and the Status Code (e.g., 200 OK).


2. **Headers:** Key-value pairs that act as metadata. They describe things like the type of browser being used, the type of data being sent, or security requirements.
3. **Empty Line:** A mandatory blank line that tells the computer: "The headers are finished; the actual content (body) starts next."
4. **Body (Optional):** The actual payload.
* In a **Request**, this might be the password you typed into a login form.
* In a **Response**, this is usually the HTML code for the webpage you want to see.



---

## 🧠 Why the "Empty Line" is Critical

From a technical and security perspective, the empty line is a strict delimiter. If a message is malformed and lacks this line, the server may fail to process the request, or worse, it could lead to **HTTP Request Smuggling** vulnerabilities, where an attacker "hides" a second request inside the body of the first.

---

## 📝 Task 4 Answers

* **Which HTTP message is returned by the web server after processing a client's request?**
* `HTTP Response`


* **What follows the headers in an HTTP message?**
* `Empty Line`



---

## 🛠️ HTTP Message Anatomy Quick-Look

| Part | Purpose | Example |
| --- | --- | --- |
| **Start Line** | Defines the action/status | `GET /index.html HTTP/1.1` |
| **Headers** | Metadata & Instructions | `Host: tryhackme.com` |
| **Empty Line** | The separator | *(Blank Space)* |
| **Body** | The actual content | `<html>...</html>` |

---
# Web Application Basics — Task 5

## HTTP Request: Request Line and Methods

**TryHackMe Room Notes**

---

## 📌 The Request Line

The request line is the very first line of an HTTP request. It acts as the "command" sent to the server, defining what action to take and where to take it.

It consists of three distinct parts:

1. **Method:** The verb (action) being performed (e.g., `GET`, `POST`).
2. **Path:** The specific location of the resource (e.g., `/login` or `/api/users`).
3. **Version:** The protocol version being used (e.g., `HTTP/1.1`).

---

## 🧱 HTTP Methods (The Verbs)

The method tells the server what the user intends to do. From a security perspective, understanding these is crucial because each one presents different risks.

### Primary Methods

| Method | Purpose | Security Note |
| --- | --- | --- |
| **GET** | Retrieve data. | **Never** use for sensitive data; parameters are visible in the URL and browser history. |
| **POST** | Submit data (create/update). | Vulnerable to **SQL Injection** and **XSS** if input is not sanitized. |
| **PUT** | Replace a resource. | Ensure strict **Authorization** so users can't overwrite files they don't own. |
| **DELETE** | Remove a resource. | Improper access control here can lead to massive data loss. |

### Secondary & Management Methods

* **PATCH:** Makes partial updates to a resource (more efficient than PUT).
* **HEAD:** Same as GET but returns **only headers** (no body). Used to check if a file exists or its size.
* **OPTIONS:** Asks the server which methods are supported for a specific URL.
* **TRACE:** Echoes the request back to the client. **Security Risk:** Usually disabled to prevent "Cross-Site Tracing" (XST) attacks.

---

## 🧠 Evolution of HTTP Versions

* **HTTP/1.1:** The "Workhorse." Introduced **persistent connections**, allowing multiple requests over a single connection.
* **HTTP/2:** Focuses on speed via **Multiplexing** (sending many requests at once) and header compression.
* **HTTP/3:** Uses the **QUIC** protocol (based on UDP) to reduce latency and improve security in unstable network environments.

---

## 📝 Task 5 Answers

* **Which HTTP protocol version became widely adopted and remains the most commonly used version...?**
* `HTTP/1.1`


* **Which HTTP request method describes the communication options for the target resource...?**
* `OPTIONS`


* **In an HTTP request, which component specifies the specific resource or endpoint...?**
* `URL Path`



---

## 🛠️ HTTP Methods Cheat Sheet

| Verb | Action | Typical Use Case |
| --- | --- | --- |
| `GET` | Read | Viewing a blog post or profile. |
| `POST` | Create | Submitting a registration form. |
| `PUT` | Update | Changing your entire user profile. |
| `DELETE` | Delete | Closing an account or deleting a comment. |
| `OPTIONS` | Query | Pre-flight check for CORS (Cross-Origin Resource Sharing). |

---
