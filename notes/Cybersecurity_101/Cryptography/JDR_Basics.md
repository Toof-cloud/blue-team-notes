# 🕵️ John the Ripper: The Basics - Study Notes

## 🛠️ Task 04: Basic Hashing

Cracking raw hashes with specific formats.

| File | Hash Type | John Command |
| --- | --- | --- |
| **hash1.txt** | MD5 | `john --format=Raw-MD5 --wordlist=/usr/share/wordlists/rockyou.txt hash1.txt` |
| **hash2.txt** | SHA-1 | `john --format=Raw-SHA1 --wordlist=/usr/share/wordlists/rockyou.txt hash2.txt` |
| **hash3.txt** | SHA-256 | `john --format=Raw-SHA256 --wordlist=/usr/share/wordlists/rockyou.txt hash3.txt` |
| **hash4.txt** | SHA-512 | `john --format=Raw-SHA512 --wordlist=/usr/share/wordlists/rockyou.txt hash4.txt` |

---

## 🖥️ Task 05: Windows Hashes (NTLM)

Cracking Windows passwords.

```bash
john --format=nt --wordlist=/usr/share/wordlists/rockyou.txt ntlm.txt

```

---

## 🐧 Task 06: Linux Hashes (Unshadowing)

Combining `/etc/passwd` and `/etc/shadow` for cracking.

```bash
# 1. Combine the files
unshadow local_passwd local_shadow > unshadowed.txt

# 2. Crack the password
john --wordlist=/usr/share/wordlists/rockyou.txt --format=sha512crypt unshadowed.txt

```

---

## 🤡 Task 07: Single Crack Mode

Using word mangling based on the username.
*Note: Ensure the file format is `username:hash` (e.g., `joker:7bf6...`)*

```bash
john --single --format=raw-md5 hash07.txt

```

---

## 📏 Task 08: Custom Rules

Exploiting password complexity patterns.
*Add rules to `/etc/john/john.conf` under `[List.Rules:THMRules]`.*

```bash
john --wordlist=/usr/share/wordlists/rockyou.txt --rule=THMRules hash8.txt

```

---

## 📦 Task 09: ZIP Files

```bash
# 1. Extract hash
zip2john secure.zip > zip_hash.txt

# 2. Crack hash
john --wordlist=/usr/share/wordlists/rockyou.txt zip_hash.txt

# 3. Open file
unzip secure.zip

```

---

## 📚 Task 10: RAR Files

```bash
# 1. Extract hash
rar2john secure.rar > rar_hash.txt

# 2. Crack hash
john --wordlist=/usr/share/wordlists/rockyou.txt rar_hash.txt

# 3. Open file
unrar x secure.rar

```

---

## 🔑 Task 11: SSH Private Keys

```bash
# 1. Extract hash (using the Kali path)
python3 /usr/share/john/ssh2john.py id_rsa > id_rsa_hash.txt

# 2. Crack hash
john --wordlist=/usr/share/wordlists/rockyou.txt id_rsa_hash.txt

```

---

## 💡 Essential Troubleshooting

* **Show already cracked passwords:** `john --show [filename]`
* **Resume a crashed session:** `john --restore`
* **Check status while running:** Press `Space`
* **Identify a hash manually:** `hash-identifier`

---
