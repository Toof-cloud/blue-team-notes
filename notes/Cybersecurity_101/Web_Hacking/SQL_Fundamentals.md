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
# SQL Fundamentals — Task 3

## SQL Overview

**TryHackMe Room Notes**

---

## 📌 The Bridge: DBMS and SQL

A database by itself is just a file or a collection of data. To actually "talk" to it, you need two things: a **DBMS** and a **Language**.

### 🧱 1. Database Management System (DBMS)

The DBMS is the software interface that handles the heavy lifting of storing, retrieving, and securing data.

* **Examples:** MySQL, PostgreSQL, Oracle, SQLite.
* **Security Context:** Misconfigured DBMS settings (like allowing remote root access or using default passwords) are common entry points for attackers.

### ⚙️ 2. Structured Query Language (SQL)

SQL is the standardized programming language used to manage relational databases. It is designed to be highly readable—almost like writing instructions in plain English.

* **Declarative:** You tell the database *what* you want (e.g., "Give me all usernames"), and the DBMS figures out *how* to get it.

---

## 🧠 Why SQL is a "Top-Tier" Skill

* **Performance:** Relational databases are optimized to search through millions of records in milliseconds.
* **Human-Readable:** Commands like `SELECT`, `INSERT`, and `DELETE` make the logic easy to follow.
* **Data Integrity:** Because of strict schemas (pre-defined structures), SQL databases prevent "garbage" data from being entered, ensuring accuracy for critical systems like banking.

---

## 🛠️ Hands-On: Accessing the Database

In a typical Linux environment (like the TryHackMe VM), you interact with the database through the terminal.

1. **Command:** `mysql -u root -p`
* `-u root`: Log in as the "root" (admin) user.
* `-p`: Prompt for a password.


2. **Semicolon ( ; ):** In SQL, every command **must** end with a semicolon. If you forget it, the DBMS will keep waiting for more input.

---

## 📝 Task 3 Answers

* **What serves as an interface between a database and an end user?**
* `Database Management System` (or `DBMS`)


* **What query language can be used to interact with a relational database?**
* `SQL`



---

## 🛠️ SQL Terminal Cheat Sheet

| Command | Action |
| --- | --- |
| `mysql -u [user] -p` | Log into the MySQL monitor. |
| `help;` or `\h` | View help documentation. |
| `\c` | Clear the current input statement (if you made a typo). |
| `exit` or `quit` | Leave the MySQL monitor. |

---
# SQL Fundamentals — Task 4

## Database and Table Statements

**TryHackMe Room Notes**

---

## 📌 Managing Databases

Before you can store data, you must build the "container" for it. In SQL, this involves a hierarchy: you create a **Database**, and inside that database, you create **Tables**.

### 🧱 Database Commands

| Command | Action |
| --- | --- |
| `CREATE DATABASE name;` | Creates a new database container. |
| `SHOW DATABASES;` | Lists all databases on the server. |
| `USE name;` | Selects a database to work with (Essential before running queries). |
| `DROP DATABASE name;` | **Destructive:** Deletes the database and all its data. |

---

## ⚙️ Table Statements

Tables require more detail because you must define the **Schema** (the structure of the columns).

### 🏗️ Creating a Table

When you create a table, you specify the column names, their data types, and any **constraints**:

* **`INT`**: For whole numbers.
* **`VARCHAR(size)`**: For text (up to a specific character limit).
* **`AUTO_INCREMENT`**: Automatically adds 1 to the ID for every new row.
* **`NOT NULL`**: Ensures the column cannot be left empty.
* **`PRIMARY KEY`**: Marks the column as the unique identifier for the table.

### 🛠️ Table Management

* **`SHOW TABLES;`**: Lists all tables in your current active database.
* **`DESCRIBE table_name;`**: Shows the structure (columns and types) of a table.
* **`ALTER TABLE table_name ADD column_name type;`**: Adds a new column to an existing table without deleting the data.
* **`DROP TABLE table_name;`**: Deletes the table entirely.

---

## 🧠 Security Perspective: Information Schema

When an attacker gains access to a SQL terminal (via SQL Injection or compromised credentials), their first step is usually **Enumeration**.
They use `SHOW DATABASES;` and `SHOW TABLES;` to map out where the sensitive information is stored.

> **Pro Tip:** In MySQL, the `information_schema` database is a "meta-database" that contains information about all other databases. Attackers often query this to find table names without needing to Guess.

---

## 📝 Task 4 Answers

* **Using the statement you've learned to list all databases... what is the flag for a name?**
* `THM{SHOW_DATABASES_FLAG}`
* *(Note: Run `SHOW DATABASES;` in your terminal to see it).*


* **Set task_4_db as your active database and list all tables... what is the flag present here?**
* `THM{SHOW_TABLES_FLAG}`
* *(Note: Run `USE task_4_db;` then `SHOW TABLES;`).*



---

## 🛠️ Table Building Cheat Sheet

| SQL Fragment | Purpose |
| --- | --- |
| `book_id INT PRIMARY KEY` | Creates a unique ID number. |
| `book_name VARCHAR(100)` | Stores a title up to 100 characters. |
| `pub_date DATE` | Stores the date of publication. |
| `DESC table_name;` | Quick check of your table's design. |

---
# SQL Fundamentals — Task 5

## CRUD Operations

**TryHackMe Room Notes**

---

## 📌 The Core of Data Management: CRUD

**CRUD** is an acronym that describes the four basic operations you can perform on any data-driven system. In SQL, these map directly to specific statements.

### 🧱 1. Create (**INSERT**)

Used to add new rows of data into a table.

* **Syntax:** `INSERT INTO table_name (column1, column2) VALUES (value1, value2);`
* **Note:** Strings and dates must be enclosed in quotes (e.g., `"2024-10-14"`).

### 🔍 2. Read (**SELECT**)

Used to retrieve data. This is the most common operation in SQL.

* **Select All:** `SELECT * FROM table_name;` (The `*` is a wildcard for "all columns").
* **Select Specific:** `SELECT column1, column2 FROM table_name;`

### ⚙️ 3. Update (**UPDATE**)

Used to modify existing records.

* **Syntax:** `UPDATE table_name SET column_name = "new_value" WHERE condition;`
* **⚠️ CRITICAL:** Always use a `WHERE` clause. If you forget it, SQL will update **every single row** in the table with the new value.

### 🗑️ 4. Delete (**DELETE**)

Used to remove records.

* **Syntax:** `DELETE FROM table_name WHERE condition;`
* **⚠️ CRITICAL:** Like Update, if you omit the `WHERE` clause, you will delete **all data** in the table.

---

## 🧠 Security Perspective: The Danger of CRUD

In the hands of an attacker, these operations are devastating:

* **Unauthorized SELECT:** Leaking user passwords or PII (Personally Identifiable Information).
* **Unauthorized UPDATE:** Changing an account's permission level to "admin."
* **Unauthorized DELETE:** Wiping evidence from log tables or destroying a company's database.
* **Unauthorized INSERT:** Creating a "backdoor" admin user.

---

## 📝 Task 5 Answers

* **Using tools_db... what is the name of the tool in the hacking_tools table used for MITM attacks on wireless networks?**
* `WiFi PineApple`
* *(Method: `USE tools_db;` then `SELECT name FROM hacking_tools WHERE description LIKE '%wireless%';`)*


* **Using tools_db... what is the shared category for both USB Rubber Ducky and Bash Bunny?**
* `Physical Access`
* *(Method: `SELECT category FROM hacking_tools WHERE name = "USB Rubber Ducky";`)*



---

## 🛠️ CRUD Quick-Reference

| Operation | SQL Command | Example |
| --- | --- | --- |
| **Create** | `INSERT` | `INSERT INTO users (name) VALUES ("poopi");` |
| **Read** | `SELECT` | `SELECT * FROM hacking_tools;` |
| **Update** | `UPDATE` | `UPDATE users SET role = "admin" WHERE id = 5;` |
| **Delete** | `DELETE` | `DELETE FROM logs WHERE date < "2025-01-01";` |

---
