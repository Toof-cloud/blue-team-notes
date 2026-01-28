# OSI Model
- The OSI (Open Systems Interconnection) model is a conceptual model developed by the International Organization for Standardization (ISO) that describes how communications should occur in a computer network. In other words, the OSI model defines a framework for computer network communications. Although this model is theoretical, it is vital to learn and understand as it helps grasp networking concepts on a deeper level. The OSI model is composed of seven layers:

## OSI Model Layers
1. Physical Layer
2. Data Link Layer
3. Network Layer
4. Transport Layer
5. Session Layer
6. Presentation Layer
7. Application Layer

## TCP 
- Transmission Control Protocol (TCP) is a connection-oriented protocol requiring a TCP three-way-handshake to establish a connection. TCP provides reliable data transfer, flow control and congestion control. Higher-level protocols such as HTTP, POP3, IMAP and SMTP use TCP

## UDP
- User Datagram Protocol (UDP) is a connectionless protocol; UDP does not require a connection to be established. UDP is suitable for protocols that rely on fast queries, such as DNS, and for protocols that prioritise real-time communications, such as audio/video conferencing and broadcast.

## TCP & UDP Ports
- A port number uses two octets; consequently, it ranges between 1 and 65535; port 0 is reserved.

## IP Address
- An IP address (Internet Protocol address) is a unique numerical label assigned to each device connected to a computer network that uses the Internet Protocol for communication. It serves two main functions: identifying the host or network interface and providing the location of the device in the network. IP addresses can be either IPv4 (e.g., 192.168.1.1) or IPv6 (e.g., 2001:0db8:85a3:0000:0000:8a2e:0370:7334).
    - Private IP
        - A private IP is a local identifier used to distinguish devices within your own internal network, such as your home or office. These addresses are not unique globally and cannot be reached directly from the internet, which helps conserve the limited supply of IPv4 addresses.

            - Example: 192.168.1.15 (common for a home laptop) or 10.0.0.5 (common in large office buildings).

    - Public IP
        - A public IP address is a globally unique numerical label assigned to your internet connection by your Service Provider (ISP). It acts like a home's street address, allowing servers across the world to identify and send data back to your specific network.
            - Example: 172.217.1.14 (one of Google’s public addresses) or 93.184.216.34 (the public address for Example.com).

    - Router
        - The router acts as a gateway or "traffic controller" between your local private network and the vast public internet. It uses a process called Network Address Translation (NAT) to route incoming data from its single public IP to the correct private IP of the device that requested it.
            - Example: The physical box in your hallway from Comcast or AT&T, or a high-end enterprise device like a Cisco ISR.

## Telnet
- The TELNET (Teletype Network) protocol is a network protocol for remote terminal connection. In simpler words, telnet, a TELNET client, allows you to connect to and communicate with a remote system and issue text commands. Although initially it was used for remote administration, we can use telnet to connect to any server listening on a TCP port number.