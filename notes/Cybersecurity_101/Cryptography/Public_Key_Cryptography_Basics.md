# Study Notes: Public Key Cryptography Basics 🗝️

## Task 2: Asymmetric Encryption Concepts

Asymmetric encryption is primarily used for the "secure handshake." Because it is computationally slow, it is used to negotiate a Symmetric Key which then handles the bulk of the data transfer.

### The Analogy

To send a secret without a pre-shared password:

- **The Lock (Public Key):** You ask your friend for a padlock. Anyone can see the lock.
- **The Box:** You put your secret in a box and snap your friend's lock onto it.
- **The Key (Private Key):** Only your friend has the key to that specific lock. Even though everyone saw the lock, only the key holder can open the box.

---

## Task 3: The RSA Algorithm 🔢

RSA security is based on the **Prime Factorization Problem**: it is easy to multiply two large primes, but nearly impossible for a computer to reverse the process for very large numbers.

### RSA Math Reference

| Variable | Definition | Formula / Note |
| :--- | :--- | :--- |
| $p, q$ | Prime Numbers | Secret starting components |
| $n$ | Modulus | $n = p \times q$ |
| $\phi(n)$ | Euler's Totient | $\phi(n) = (p - 1) \times (q - 1)$ |
| $e$ | Public Exponent | Used for Encryption |
| $d$ | Private Exponent | Used for Decryption |
| $m$ | Message | The Plaintext |
| $c$ | Ciphertext | The Encrypted data |

**Standard CTF Tools:** RsaCtfTool, rsatool.

---

## Task 4: Diffie-Hellman Key Exchange 🤝

A method to establish a Shared Secret over an insecure channel. Unlike RSA, Diffie-Hellman does not "encrypt" data; it "agrees" on a key.

- **Public Variables:** A prime ($p$) and a generator ($g$).
- **Private Variables:** Alice chooses ($a$), Bob chooses ($b$).
- **The Exchange:** Alice sends ($g^a \pmod p$), Bob sends ($g^b \pmod p$).
- **The Result:** Both arrive at the same shared secret: $g^{ab} \pmod p$.

---

## Task 5: SSH (Secure Shell) 💻

SSH uses asymmetric keys to replace vulnerable passwords.

### Key Files & Permissions 📂

- **id_rsa** or **id_ed25519:** Private Key. NEVER SHARE. (Permission: 600).
- **id_rsa.pub:** Public Key. Placed on the server you want to access.
- **authorized_keys:** A file on the server containing the public keys of all allowed users.

**Command to generate:**
```bash
ssh-keygen -t ed25519
```

---

## Task 6: Digital Signatures & Certificates 📜

**Digital Signature:** Created by encrypting a hash of a document with a Private Key. It proves Integrity (not changed) and Authenticity (who sent it).

**Certificates:** A file that binds a Public Key to an identity (like a website).

**Chain of Trust:** Your browser trusts a Certificate Authority (CA) → The CA trusts the website.

---

## Task 7: PGP and GPG 🔐

PGP (Pretty Good Privacy) and GPG (GnuPG) are used for encrypting files and emails.

**Common Commands:**
- Importing a key: `gpg --import [file]`
- Decrypting: `gpg --decrypt [file].gpg`
- Cracking Passphrases: Use `gpg2john` followed by John the Ripper.

---

## Task 8: Key Terminology ⚠️

- **Cryptography:** Securing communication.
- **Cryptanalysis:** Breaking/bypassing security systems.
- **Brute-Force:** Trying every possible combination.
- **Dictionary Attack:** Trying a list of specific, likely words.

---

