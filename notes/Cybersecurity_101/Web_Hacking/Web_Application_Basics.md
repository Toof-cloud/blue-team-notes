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
# Web Application Basics — Task 6

## HTTP Request: Headers and Body

**TryHackMe Room Notes**

---

## 📌 Request Headers

Headers provide essential metadata about a request. They help the server understand who is sending the request, where they came from, and what kind of data they are sending.

### 🧱 Common Request Headers

| Header | Purpose | Example |
| --- | --- | --- |
| **Host** | Tells the server which domain the user wants. Essential for servers hosting multiple sites on one IP. | `Host: tryhackme.com` |
| **User-Agent** | Identifies the browser and OS. Attackers often "spoof" this to bypass mobile-only or browser-specific restrictions. | `User-Agent: Mozilla/5.0...` |
| **Referer** | The URL of the previous page that linked to this request. | `Referer: https://google.com` |
| **Cookie** | Sends stored session data back to the server to prove you are logged in. | `Cookie: session=12345` |
| **Content-Type** | Tells the server how to read the data in the **Body**. | `Content-Type: application/json` |

---

## ⚙️ The Request Body

The body contains the actual data being sent to the server (common in `POST`, `PUT`, and `PATCH` requests). The format of this data is defined by the `Content-Type` header.

### 📊 Common Body Formats

1. **URL Encoded (`application/x-www-form-urlencoded`):** The default for simple HTML forms. Data looks like `field1=value1&field2=value2`.
2. **Form Data (`multipart/form-data`):** Used when uploading files. It uses a "boundary" string to separate different parts of the data (e.g., a text field and a binary image file).
3. **JSON (`application/json`):** The standard for modern APIs. Structured as `{"key": "value"}`.
4. **XML (`application/xml`):** An older, tag-based structure similar to HTML used in many legacy enterprise systems.

---

## 📝 Task 6 Answers

* **Which HTTP request header specifies the domain name of the web server...?**
* `Host`


* **What is the default content type for form submissions... encoded as key=value pairs?**
* `application/x-www-form-urlencoded`


* **Which part of an HTTP request contains additional information like host, user agent, and content type...?**
* `Headers`



---

## 🛠️ Content-Type Cheat Sheet

| Format | Header Value | Use Case |
| --- | --- | --- |
| **Simple Form** | `application/x-www-form-urlencoded` | Standard login or contact forms. |
| **File Upload** | `multipart/form-data` | Uploading profile pictures or documents. |
| **API Call** | `application/json` | Sending data to a mobile app backend. |
| **Legacy API** | `application/xml` | SOAP services or older web integrations. |

---
# Web Application Basics — Task 7

## HTTP Response: Status Line and Status Codes

**TryHackMe Room Notes**

---

## 📌 The Status Line

Just as a request has a request line, an HTTP response has a **Status Line**. This is the first thing your browser reads to determine if it should display a webpage, show an error, or redirect you elsewhere.

It consists of:

1. **HTTP Version:** (e.g., `HTTP/1.1`)
2. **Status Code:** A 3-digit integer representing the result.
3. **Reason Phrase:** A human-readable summary (e.g., `OK`, `Not Found`).

---

## 🧱 Status Code Categories

The first digit of the status code defines the "class" of the response. Memorizing these ranges is essential for quick troubleshooting and security analysis.

| Range | Category | Meaning |
| --- | --- | --- |
| **100 - 199** | **Informational** | Request received, continuing process. |
| **200 - 299** | **Success** | The action was successfully received, understood, and accepted. |
| **300 - 399** | **Redirection** | Further action needs to be taken to complete the request (e.g., the page moved). |
| **400 - 499** | **Client Error** | The request contains bad syntax or cannot be fulfilled (e.g., you asked for a page that doesn't exist). |
| **500 - 599** | **Server Error** | The server failed to fulfill an apparently valid request. |

---

## 🧠 Common Codes for Pentesters

* **200 OK:** The "Holy Grail." The request worked.
* **301/302 Redirect:** Often used to redirect users from `http` to `https`.
* **401 Unauthorized / 403 Forbidden:** Key indicators that you've hit a protected area. 401 means "Who are you?" (needs login), 403 means "I know who you are, but you're not allowed here."
* **404 Not Found:** Useful during **directory brute-forcing**; it tells you which paths *don't* exist.
* **500 Internal Server Error:** This often happens when a web exploit (like SQLi) causes the server's backend code to crash. It’s a huge "hint" that the application is struggling with your input.

---

## 📝 Task 7 Answers

* **What part of an HTTP response provides the HTTP version, status code, and a brief explanation...?**
* `Status Line`


* **Which category of HTTP response codes indicates that the web server encountered an internal issue...?**
* `Server Error Responses (500-599)`


* **Which HTTP status code indicates that the requested resource could not be found...?**
* `404`



---

## 🛠️ Status Code Cheat Sheet

| Code | Phrase | Security Context |
| --- | --- | --- |
| **200** | OK | Standard successful response. |
| **301** | Moved Permanently | Target page has a new URL. |
| **400** | Bad Request | The server didn't understand your "malformed" exploit. |
| **401** | Unauthorized | Target requires a valid session or login. |
| **404** | Not Found | Page missing (or hidden). |
| **500** | Internal Server Error | Potential code-level vulnerability or crash. |

---
# Web Application Basics — Task 8

## HTTP Response: Headers and Body

**TryHackMe Room Notes**

---

## 📌 Response Headers

While Request Headers tell the server about the client, **Response Headers** tell the browser about the server and how to handle the data it just received. For a security professional, these headers are a goldmine of information.

### 🧱 Essential Response Headers

| Header | Purpose | Security Context |
| --- | --- | --- |
| **Server** | Identifies the software (Nginx, Apache). | **Risk:** Reveals version numbers (e.g., `Server: Apache/2.4.1`) which helps attackers find specific exploits. |
| **Set-Cookie** | Instructs the browser to store a piece of data. | **Crucial:** Used for session management. Must be protected by security flags. |
| **Content-Type** | Tells the browser how to render the body. | Prevents "MIME-sniffing" attacks where a browser might mistakenly run a text file as a script. |
| **Location** | Used in 3xx redirects to provide the new URL. | **Risk:** Can lead to "Open Redirect" vulnerabilities if not validated. |

---

## 🍪 Securing the Cookie

The `Set-Cookie` header is the primary target for attackers looking to hijack sessions. To defend against this, developers use specific "flags" within the header:

1. **HttpOnly:** This flag prevents JavaScript (and therefore **XSS** attacks) from reading the cookie. If an attacker injects a script, they cannot steal the session token if this flag is present.
2. **Secure:** This ensures the cookie is **only** sent over encrypted HTTPS connections. It prevents the cookie from being sniffed out of the air on public Wi-Fi.

---

## ⚙️ The Response Body

This is the "payload" the server delivers to the user.

* **Web Pages:** Usually HTML code.
* **APIs:** Usually JSON or XML data.
* **Files:** Binary data for images, PDFs, or downloads.

**Security Warning:** If the body contains user-supplied data that hasn't been properly "escaped," the browser might execute that data as code, leading to **Stored Cross-Site Scripting (XSS)**.

---

## 📝 Task 8 Answers

* **Which HTTP response header can reveal information about the web server's software and version...?**
* `Server`


* **Which flag should be added to cookies... to ensure they are only transmitted over HTTPS?**
* `Secure`


* **Which flag should be added to cookies... to prevent them from being accessed via JavaScript?**
* `HttpOnly`



---

## 🛠️ Cookie Security Cheat Sheet

| Flag | Function | Attack Prevented |
| --- | --- | --- |
| **`HttpOnly`** | Blocks JS access to `document.cookie`. | Session Hijacking via XSS |
| **`Secure`** | Forces transmission over HTTPS only. | Man-in-the-Middle (MitM) sniffing |
| **`SameSite=Strict`** | Prevents the cookie from being sent on cross-site requests. | Cross-Site Request Forgery (CSRF) |

---
# Web Application Basics — Task 9

## Security Headers

**TryHackMe Room Notes**

---

## 📌 Hardening the Web Server

Security headers are an additional layer of defense (Defense in Depth). Even if a web application has a vulnerability, these headers can instruct the browser to block the exploit from succeeding.

### 🧱 Key Security Headers

#### 🛡️ Content-Security-Policy (CSP)

The CSP is a powerful "allow-list" for your browser. It tells the browser exactly which domains are trusted to run scripts, load images, or use CSS.

* **Purpose:** Primarily prevents **Cross-Site Scripting (XSS)** and data injection attacks.
* **Example:** `Content-Security-Policy: script-src 'self' https://scripts.trusted.com`
* This means the browser will **only** execute scripts from the same origin or the specific trusted URL. Any other script (like one injected by a hacker) will be blocked.



#### 🔒 Strict-Transport-Security (HSTS)

HSTS tells the browser: "Never communicate with this site over unencrypted HTTP."

* **Purpose:** Prevents **Man-in-the-Middle (MitM)** attacks and SSL stripping.
* **Directive:** `includeSubDomains` ensures the policy covers `blog.site.com` as well as `site.com`.

#### 🕵️ X-Content-Type-Options

Browsers sometimes try to "guess" the file type (MIME-sniffing). If an attacker uploads a malicious script disguised as a `.jpg`, the browser might try to run it.

* **Directive:** `nosniff` forces the browser to strictly follow the `Content-Type` header provided by the server.

#### 🔗 Referrer-Policy

When you click a link, your browser usually tells the new site where you came from. This can leak sensitive internal URLs or tokens.

* **Purpose:** Controls how much "referral" data is shared with other sites.
* **Common Setting:** `strict-origin-when-cross-origin` (shares full info within your own site, but only the domain name when leaving).

---

## 📝 Task 9 Answers

* **In a Content Security Policy (CSP) configuration, which property can be set to define where scripts can be loaded from?**
* `script-src`


* **When configuring the HSTS header... which directive should be included to apply the security policy to both the main domain and its subdomains?**
* `includeSubDomains`


* **Which HTTP header directive is used to prevent browsers from interpreting files as a different MIME type... mitigating content type sniffing attacks?**
* `nosniff`



---

## 🛠️ Security Header Audit Checklist

| Header | Recommended Setting | Protection Provided |
| --- | --- | --- |
| **CSP** | `default-src 'self' ...` | XSS, Clickjacking, Injection |
| **HSTS** | `max-age=31536000; includeSubDomains` | Protocol Downgrade / Sniffing |
| **X-Content-Type** | `nosniff` | MIME-Sniffing / File Upload Exploits |
| **Referrer-Policy** | `no-referrer` or `same-origin` | Information Leakage |

---
## Web Application Basics: Master Cheat Sheet

**TryHackMe Study Guide**

---

### 🌐 Web Architecture (The Planet Analogy)

* **Front End (The Surface):**
* **HTML:** The structure/skeleton.
* **CSS:** The styling/skin.
* **JavaScript:** The interactivity/logic.


* **Back End (The Engine):**
* **Web Server:** Delivers content (e.g., Apache, Nginx).
* **Database:** Stores info (e.g., MySQL).
* **WAF:** The protective atmosphere filtering malicious traffic.



---

### 📍 URL Anatomy

**Example:** `https://admin@tryhackme.com:443/rooms/basics?id=1#task3`

| Component | Example | Description |
| --- | --- | --- |
| **Scheme** | `https://` | Protocol (HTTP/HTTPS). |
| **User** | `admin@` | Optional (and risky) auth info. |
| **Host/Domain** | `tryhackme.com` | The destination server. |
| **Port** | `:443` | The "doorway" (80 for HTTP, 443 for HTTPS). |
| **Path** | `/rooms/basics` | File/resource location. |
| **Query String** | `?id=1` | Data passed to server (starts with `?`). |
| **Fragment** | `#task3` | Internal page anchor (starts with `#`). |

---

### ✉️ HTTP Message Structure

1. **Start Line:** Method/Path/Version (Request) OR Version/Status (Response).
2. **Headers:** Metadata key-value pairs.
3. **Empty Line:** **Required** separator between headers and body.
4. **Body:** The actual data (HTML, JSON, Form Data).

---

### 🛠️ HTTP Request Methods (Verbs)

| Method | Use Case | Security Note |
| --- | --- | --- |
| **GET** | Retrieve data | Parameters visible in URL (plaintext). |
| **POST** | Submit/Create data | Data in body; needs input sanitization. |
| **PUT** | Replace resource | Requires strict authorization. |
| **DELETE** | Remove resource | High risk; verify permissions. |
| **OPTIONS** | Check supported methods | Used for CORS pre-flight checks. |
| **HEAD** | Get headers only | Check file size/existence without download. |

---

### 🚦 HTTP Response Status Codes

| Range | Category | Common Examples |
| --- | --- | --- |
| **1xx** | Informational | `100 Continue` |
| **2xx** | Success | `200 OK` |
| **3xx** | Redirection | `301 Permanent`, `302 Temporary` |
| **4xx** | Client Error | `400 Bad Request`, `401 Unauthorized`, `404 Not Found` |
| **5xx** | Server Error | `500 Internal Error`, `503 Service Unavailable` |

---

### 🛡️ Security & Response Headers

| Header | Recommendation | Protection Provided |
| --- | --- | --- |
| **Server** | Remove or Obscure | Prevents version-specific exploit research. |
| **Set-Cookie** | `HttpOnly; Secure` | Prevents XSS theft and MitM sniffing. |
| **CSP** | `script-src 'self'` | Blocks malicious script execution (XSS). |
| **HSTS** | `max-age=...` | Forces encrypted HTTPS connections. |
| **X-Content-Type** | `nosniff` | Blocks browsers from "guessing" file types. |
| **Referrer-Policy** | `same-origin` | Prevents leaking sensitive URLs to other sites. |

---
