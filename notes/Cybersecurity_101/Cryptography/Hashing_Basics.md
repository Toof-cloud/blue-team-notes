
---

# 🛡️ Study Notes: Hashing Basics

## 🔍 Task 1 & 2: What is a Hash Function?

A hash function is a **one-way** process that takes an input of any size and turns it into a **fixed-size** string (a digest). Unlike encryption, it is designed to be impossible to reverse.

### Key Characteristics:

* **Fixed Output Size:** Whether you hash a single letter or a 6 GB file, the output length is always the same for that algorithm.
* **Deterministic:** The same input always results in the same hash.
* **Avalanche Effect:** A tiny change in input (even 1 bit) results in a completely different hash.
* **Collision Resistance:** It should be nearly impossible for two different inputs to produce the same hash.

### Common Algorithms & Linux Commands:

| Algorithm | Command | Example Output Length |
| --- | --- | --- |
| **MD5** | `md5sum` | 32 Hex characters (128-bit) |
| **SHA-1** | `sha1sum` | 40 Hex characters (160-bit) |
| **SHA-256** | `sha256sum` | 64 Hex characters (256-bit) |

---

## 🛑 Task 3 & 4: Password Security & Storage

Storing passwords in **plaintext** is a critical security failure. If a database is leaked, every account is compromised.

### Defenses and Definitions:

* **Rainbow Tables:** Large pre-computed databases of hashes and their corresponding plaintexts. Used to "crack" unsalted hashes instantly.
* **Salting:** Adding a random unique string (the **salt**) to the password before hashing.
* *Effect:* Two users with the same password will have completely different hashes.
* *Defense:* Makes Rainbow Tables useless because the table would have to be re-generated for every possible salt.


* **Secure Algorithms:** Argon2, Scrypt, Bcrypt, and PBKDF2 are preferred because they are "slow," making brute-force attacks difficult.

---

## 🆔 Task 5: Recognizing Hashes

To crack a hash, you must first identify it.

### Linux Shadow Files (`/etc/shadow`)

Linux stores hashes in a specific format: `$id$options$salt$hash`.

| Prefix | Algorithm |
| :--- | :--- |
| `$y$` | Yescrypt (Modern default) |
| `$7$` | Scrypt |
| `$2a$` or `$2b$` | Bcrypt |
| `$6$` | SHA-512 |
| `$5$` | SHA-256 |
| `$1$` | MD5 |
| `$3$` | MD5 (Sun MD5) |

### Windows Hashes

Windows uses **NTLM** (NT LAN Manager). These are visually identical to MD4/MD5 (32 hex characters), so context is key.

---

## 🔨 Task 6: Password Cracking

Since hashes cannot be decrypted, we crack them by guessing (hashing a wordlist) and comparing the results.

### Tools:

* **John the Ripper:** Primarily uses the CPU.
* **Hashcat:** "The world's fastest cracker." Uses the **GPU** to perform thousands of mathematical calculations simultaneously.

**Hashcat Syntax Example:**
`hashcat -m 1000 -a 0 hash_to_crack.txt rockyou.txt`

* `-m 1000`: Specifies NTLM (Mode 1000).
* `-a 0`: "Straight" attack mode (uses a wordlist).

---

## 🧪 Task 7: Data Integrity & HMAC

Hashing is the primary way to verify that a file has not been tampered with or corrupted during download.

### HMAC (Keyed-Hash Message Authentication Code)

An HMAC combines a **Hash function** with a **Secret Key**.

* **Integrity:** Proves the message wasn't changed.
* **Authenticity:** Proves the sender knows the secret key.

**Mathematical Expression:** 

---

## ⚠️ Task 8: The Big Three (Summary)

| Process | Reversible? | Purpose |
| --- | --- | --- |
| **Encoding** | ✅ Yes | Compatibility (e.g., Base64). Not for security. |
| **Encryption** | ✅ Yes | Confidentiality (requires a key). |
| **Hashing** | ❌ No | Integrity & Secure Authentication. |

---
