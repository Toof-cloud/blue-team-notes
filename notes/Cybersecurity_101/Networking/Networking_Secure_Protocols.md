# Networking Secure Protocols

### Secure Socket Layer
### Internet Engineering Task Force
- The Internet Engineering Task Force (IETF) is a standards organization for the Internet and is responsible for the technical standards that comprise the Internet protocol suite.



### Transport Layer Security
- Transport Layer Security is a cryptographic protocol that secures communications over a network. It provides authentication through the use of certificates, integrity by detecting tampering and confidentiality by encrypting the data.

### Certificate Authority
- A CA, or Certificate Authority, is a trusted organisation that verifies the digital identity of entities like websites, individuals, or companies by issuing digital certificates.
- TLS Certifiate = Certificate Signing Request (CSR) -> Certificate Authority -> Once the (signed) certificate is received, it can be used to identify the server (or the client) to others, who can confirm the validity of the signature

### Hyper Text Transfer Protocol
- HTTP relies on TCP and uses port 80 by default
- All HTTP traffic was sent in cleartext for anyone to intercept and monitor. 
### Hyper Text Transfer Protocol Secure
- HTTPS stands for Hypertext Transfer Protocol Secure. It is basically HTTP over TLS. 
- Consequently, requesting a page over HTTPS will require the following three steps (after resolving the domain name):
    1. Establish a TCP three-way handshake with the target server
    2. Establish a TLS session
    3. Communicate using the HTTP protocol; for example, issue HTTP requests, such as GET / HTTP/1.1
