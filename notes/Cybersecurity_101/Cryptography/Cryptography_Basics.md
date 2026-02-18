# TryHackMe: Cryptography Basics

## 1. The Core Process
Cryptography involves two main functions:
* **Encryption:** Converting readable data (**Plaintext**) into an unreadable format (**Ciphertext**) using an algorithm and a secret key.
* **Decryption:** The reverse process—turning Ciphertext back into Plaintext using the correct key.

---

## 2. Classic Ciphers: The Caesar Cipher
The Caesar Cipher is a **Substitution Cipher**. Each letter in the plaintext is "shifted" a certain number of places down the alphabet.

* **The Key:** The number of shifts (e.g., a shift of 3).
* **Example (Shift 3):** * `A` becomes `D`
    * `B` becomes `E`
    * `HELLO` becomes `KHOOR`
* **Weakness:** With only 25 possible shifts (in the English alphabet), it is extremely vulnerable to **Brute Force** attacks.

---

## 3. Mathematical Foundations

### Modulo Operator (`%`)
Often called "Clock Arithmetic." It finds the **remainder** after a division.
* **Example:** `14 % 12 = 2` (Like 14:00 being 2:00 PM).
* **Importance:** In crypto, modulo keeps numbers within a specific range (like 0-25 for the alphabet), ensuring the "shifts" wrap around from Z back to A.

### XOR (Exclusive OR)
A logical operation used in almost all modern encryption. 
* **Rule:** If the bits are the same, the result is `0`. If they are different, the result is `1`.
* **Why it's used:** XOR is fast and reversible. If you XOR plaintext with a key, you get ciphertext. If you XOR that ciphertext with the same key again, you get the original plaintext back!

---

## 4. Modern Symmetric Encryption
Symmetric encryption uses the **same key** for both encryption and decryption.

### DES (Data Encryption Standard)
* **History:** Developed in the 1970s.
* **Method:** A Block Cipher that breaks data into 64-bit chunks.
* **Status:** **Legacy/Insecure.** It uses a 56-bit key, which is now considered too short and can be cracked by modern computers in a very short time.

### AES (Advanced Encryption Standard)
* **History:** The successor to DES; the current global standard.
* **Method:** A Block Cipher that is much more complex and secure.
* **Key Sizes:** Supports 128, 192, and 256-bit keys.
* **Status:** **Highly Secure.** It is used by governments and banks worldwide. Even with the fastest supercomputers, it would take billions of years to brute-force AES-256.

---

### Comparison Summary

| Algorithm | Type | Key Size | Security Level |
| :--- | :--- | :--- | :--- |
| **Caesar** | Substitution | N/A (1-25) | None (Historical) |
| **DES** | Symmetric Block | 56-bit | Low (Obsolete) |
| **AES** | Symmetric Block | 128-256 bit | Extremely High |

---

## Task 2: Common Use of Asymmetric Encryption

Asymmetric encryption is computationally expensive (slow). In the real world, we don't use it to encrypt large files; instead, we use it as a **secure handshake** to exchange keys for faster symmetric encryption.

### The Locked Box Analogy
How do two people agree on a secret key without a "snooper" seeing it?

| Analogy Component | Cryptographic Equivalent |
| :--- | :--- |
| **The Secret Code** | Symmetric Cipher & Key (e.g., AES) |
| **The Padlock** | Public Key (Given to everyone) |
| **The Padlock's Key** | Private Key (Kept secret by the owner) |

**The Workflow:**
1. You ask a server for its **Public Key** (the lock).
2. You put your chosen symmetric key in a box and lock it with that Public Key.
3. Only the server, holding the **Private Key**, can open that box to get the symmetric key.
4. Now, both parties have the same secret key and can switch to fast **Symmetric Encryption**.



---

## Task 3: RSA (Rivest-Shamir-Adleman)

RSA is the most famous public-key algorithm. Its security relies on the **Factoring Problem**.

### The Core Logic
* It is mathematically easy to multiply two massive prime numbers (e.g., $p \times q = n$).
* It is "computationally infeasible" (nearly impossible for current computers) to do the reverse: taking a massive number $n$ and figuring out which two primes ($p$ and $q$) were multiplied to create it.

### RSA Variables for CTFs
When solving cryptography challenges, you will often see these variables:

| Variable | Definition |
| :--- | :--- |
| **p, q** | Two large prime numbers. |
| **n** | The product ($p \times q$). Part of both keys. |
| **e** | The Public Exponent. Used for encryption. |
| **d** | The Private Exponent. Used for decryption. |
| **m (or x)** | The **Plaintext** (message). |
| **c (or y)** | The **Ciphertext** (encrypted message). |



### The Math in Action
To encrypt a message ($m$):
$$c = m^e \pmod{n}$$

To decrypt a ciphertext ($c$):
$$m = c^d \pmod{n}$$

> [!TIP]
> **Tools for RSA CTFs:**
> If you are given $n$, $e$, and $c$ and asked to find the flag, tools like **RsaCtfTool** or **rsatool** can automate the process of factoring $n$ (if it is small enough) to calculate the private key $d$.