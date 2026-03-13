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
# SQL Fundamentals — Task 2

## Databases 101

**TryHackMe Room Notes**

---

## 📌 What is a Database?

A database is an organized collection of structured information designed for easy access, management, and analysis. Think of it as a highly advanced digital filing cabinet.

From a security perspective, understanding the **structure** of a database is the first step toward protecting it from unauthorized manipulation.

---

## 🧱 SQL vs. NoSQL: The Two Main Types

Choosing a database depends entirely on the **consistency** of the data being stored.

| Feature | Relational (SQL) | Non-Relational (NoSQL) |
| --- | --- | --- |
| **Structure** | Tabular (Rows & Columns) | Document, Key-Value, or Graph |
| **Schema** | Rigid/Pre-defined | Flexible/Dynamic |
| **Best For** | Consistent data (e.g., Banking, E-commerce) | Varying data (e.g., Social Media, Big Data) |
| **Example** | MySQL, PostgreSQL, SQLite | MongoDB, Cassandra, Redis |

---

## 📊 Tables, Rows, and Columns

In a relational database, data is organized into **Tables**.

* **Columns:** Define the *category* of data (e.g., `username`, `email`, `id`). Each column has a specific **Data Type** (String, Integer, Date).
* **Rows:** Represent a *single record* of data (e.g., one specific user's details).

---

## 🔑 Primary and Foreign Keys: The "Glue"

Relational databases are called "relational" because tables can be linked together. We use **Keys** to create these connections.

1. **Primary Key (PK):** A unique identifier for every record in a table. It ensures no two rows are identical (like a SSN or a Student ID). **Rule:** Only one per table.
2. **Foreign Key (FK):** A column in one table that points to the Primary Key of *another* table. This creates the link between them.

> **Example:** In a bookstore database, the `Books` table might have an `author_id` (Foreign Key) that links to the `id` (Primary Key) in the `Authors` table.

---

## 📝 Task 2 Answers

* **What type of database should you consider using if the data... will vary greatly in its format?**
* `Non-relational databases`


* **What type of database should you consider using if the data... will reliably be in the same structured format?**
* `Relational databases`


* **In our example, once a record of a book is inserted... it would be represented as a ___?**
* `row`


* **Which type of key provides a link from one table to another?**
* `Foreign Keys`


* **Which type of key ensures a record is unique within a table?**
* `Primary Keys`



---

## 🛠️ Data Type Cheat Sheet

| Type | Description | Example |
| --- | --- | --- |
| **String/Varchar** | Text and characters | `"Alice"`, `"p@ssword123"` |
| **Integer** | Whole numbers | `1`, `42`, `-500` |
| **Float/Decimal** | Numbers with decimals | `19.99`, `3.14` |
| **Date/Time** | Calendar dates and timestamps | `2026-03-13` |

---
