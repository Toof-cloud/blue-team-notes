# Netwroking Essentials

### DCHP
- Dynamic Host Configuration Protocol (DHCP). DHCP is an application-level protocol that relies on UDP; the server listens on UDP port 67, and the client sends from UDP port 68. Your smartphone and laptop are configured to use DHCP by default.
- DHCP follows four steps: Discover, Offer, Request, and Acknowledge (DORA):

    - DHCP Discover: The client broadcasts a DHCPDISCOVER message seeking the local DHCP server if one exists.
    - DHCP Offer: The server responds with a DHCPOFFER message with an IP address available for the client to accept.
    - DHCP Request: The client responds with a DHCPREQUEST message to indicate that it has accepted the offered IP.
    - DHCP Acknowledge: The server responds with a DHCPACK message to confirm that the offered IP address is now assigned to this client.