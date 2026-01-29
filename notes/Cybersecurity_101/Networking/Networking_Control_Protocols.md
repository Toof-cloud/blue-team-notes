# Networking Control Protocols

### Domain Name System (DNS)
- Domain Name System (DNS) is the protocol responsible for resolving hostnames, such as tryhackme.com, to their respective IP addresses.
- Layer 7 application level of the OSI Model
- DNS traffic uses UDP port 53 by default and TCP port 53 as a default fallback. 
    - Records:
        - A record: The A (Address) record maps a hostname to one or more IPv4 addresses. For example, you can set example.com to resolve to 172.17.2.172.
        - AAAA Record: The AAAA record is similar to the A Record, but it is for IPv6. Remember that it is AAAA (quad-A), as AA and AAA would refer to a battery size; furthermore, AAA refers to Authentication, Authorization, and Accounting; neither falls under DNS.
        - CNAME Record: The CNAME (Canonical Name) record maps a domain name to another domain name. For example, www.example.com can be mapped to example.com or even to example.org.
        - MX Record: The MX (Mail Exchange) record specifies the mail server responsible for handling emails for a domain.

### WHOIS
- WHOIS records of any registered domain name using one of the online services or via the command-line tool whois, available on Linux systems, among others. As expected, a WHOIS record provides information about the entity that registered a domain name, including name, phone number, email, and address.     

### HTTP & HTTPS
- Hypertext Transfer Protocol (HTTP) is the protocol that specifies how a web browser and a web server communicate. This protocol relies on TCP and defines how your web browser communicates with the web servers.

    - GET retrieves data from a server, such as an HTML file or an image.
    - POST allows us to submit new data to the server, such as submitting a form or uploading a file.
    - PUT is used to create a new resource on the server and to update and overwrite existing information.
    - DELETE, as the name suggests, is used to delete a specified file or resource on the server.

### File Transfer Protocol (FTP)
- File Transfer Protocol (FTP) is designed to transfer files. As a result, FTP is very efficient for file transfer, and when all conditions are equal, it can achieve higher speeds than HTTP.
- FTP server listens on **TCP port 21** by default; data transfer is conducted via another connection from the client to the server.

    - USER is used to input the username
    - PASS is used to enter the password
    - RETR (retrieve) is used to download a file from the FTP server to the client.
    - STOR (store) is used to upload a file from the client to the FTP server.

- Unlike Telnet or HTTP, which are designed to "stream" text directly to your terminal window to be read immediately, <font color="red">FTP is designed for bulk data management. Its primary job is to move files from point A to point B so you can use them later</font>.
---
### Simple Mail Transfer Protocol (SMTP)
- Simple Mail Transfer Protocol (SMTP) is a protocol used to send the email to an SMTP server, more specifically to a Mail Submission Agent (MSA) or a Mail Transfer Agent (MTA).

    - HELO or EHLO = initiates an SMTP session
    - MAIL FROM = specifies the sender’s email address
    - RCPT TO = specifies the recipient’s email address
    - DATA = indicates that the client will begin sending the content of the email message
    - . = is sent on a line by itself to indicate the end of the email message
---
### Post Office Protocol Version 3 
- Post Office Protocol Version 3 (POP3) is an alternative protocol for receiving emails that downloads emails from the server to a local device. Using POP3, a recipient cannot access their emails again from a different device because they are stored locally and then deleted from the email server.

#### Common POP3 Commands

| Command | Argument | Description |
| :--- | :--- | :--- |
| **USER** | `<username>` | Identifies the user connecting to the mailbox. |
| **PASS** | `<password>` | Provides the user’s password for authentication. |
| **STAT** | *(None)* | Requests the number of messages and total size of the mailbox. |
| **LIST** | *(None)* | Lists all messages and their respective sizes. |
| **RETR** | `<msg_num>` | Retrieves the full content of the specified message. |
| **DELE** | `<msg_num>` | Marks a specific message for deletion. |
| **QUIT** | *(None)* | Ends the session and applies changes (like deletions). |