# SQL Fundamentals — Task 1

## Introduction

**TryHackMe Room Notes**

---

## 📌 Why SQL Matters in Cyber Security

Databases are the "brain" of almost every modern application. They store everything from user passwords and credit card details to server logs and sensitive medical records. Because they hold the "crown jewels" of data, they are a primary target for attackers and a critical focus for defenders.

### ⚔️ The Offensive Perspective

Understanding SQL allows you to identify and exploit **SQL Injection (SQLi)** vulnerabilities. This is when an attacker "injects" their own code into a database query to:

* **Bypass authentication:** Logging in as "admin" without a password.
* **Exfiltrate data:** Dumping the entire list of user credentials.
* **Tamper with records:** Changing a bank balance or deleting logs to hide tracks.

### 🛡️ The Defensive Perspective

For a security analyst working in a **SOC** (Security Operations Center), SQL is essential for:

* **SIEM Queries:** Using SQL-like languages (e.g., KQL or SPL) to search through millions of logs for suspicious activity.
* **Forensics:** Navigating databases to find when and how a breach occurred.
* **Hardening:** Implementing "Least Privilege" access so that a web application can only see the data it absolutely needs.

---

## 🧱 Key Learning Objectives

In this room, you will transition from a "data consumer" to a "data commander" by mastering:

1. **CRUD Operations:** Create, Read, Update, and Delete data.
2. **Clauses:** Filtering and sorting data (e.g., `WHERE`, `ORDER BY`).
3. **Operators:** Performing logic (e.g., `AND`, `OR`, `LIKE`).
4. **Functions:** Calculating or transforming data (e.g., `COUNT`, `SUM`, `AVG`).

---

## 📝 Task 1 Answers

* **Teach me the basics of SQL!**
* `No answer needed` (This is the start of your journey!)



---

## 🛠️ SQL Quick-Look

| Term | Definition |
| --- | --- |
| **SQL** | Structured Query Language — the language used to talk to databases. |
| **Database** | A structured collection of data stored electronically. |
| **Table** | A collection of related data entries consisting of columns and rows. |
| **Query** | A specific request for information from a database. |

---
