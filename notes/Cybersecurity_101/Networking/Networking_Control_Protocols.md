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