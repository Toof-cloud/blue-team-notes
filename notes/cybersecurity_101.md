Active Directory - is a directory service developed bu Microsoft. It stores information about network object such as computers, users, and groups. It provodes authentication and authorisation services and allows administrators to manage network resources centrally.

Active Directory Objects - 
1. Users - also knows as security principals and can act upon resouces in the network.
    1.1 Poeple 
    1.2 Services

2. Machines - each computer that joins the active directory domain a machine object will be created.
Can also be a security principal.
- Note: Machine Account passwords are automatically rotated out and are generally comprised of 120 random characters.
- The machine account name is the computer's name followed by a dollar sign. For example, a machine named DC01 will have a machine account called DC01$.

3. Security Groups - Security groups are also considered security principals and, therefore, can have privileges over resources on the network.

Security Groups -
1. Domain Admins - Users of this group have administrative privileges over the entire domain. By default, they can administer any computer on the domain, including the DCs.
2. Server Operators - Users in this group can administer Domain Controllers. They cannot change any administrative group memberships.
3. Backup Operators - Users in this group are allowed to access any file, ignoring their permissions. They are used to perform backups of data on computers.
4. Account Operators - can modify or create other accounts in the domain.
5. Domain Users - all existing computers inside the domain.
6. Domain Computers - all existing compouters inside the domain.
7. Domain Controllers - all the existing DCs on the domain.

Domain Controller - The server that runs the Active Directory.

Windows Domain - a group of users and computers under the administration of a given business. Centralise the administration of a given business. 

Remote Desktop Protocol - a protocol used to establish remote graphical sessions over the network.

1. Workstations

Workstations are one of the most common devices within an Active Directory domain. Each user in the domain will likely be logging into a workstation. This is the device they will use to do their work or normal browsing activities. These devices should never have a privileged user signed into them.

2. Servers

Servers are the second most common device within an Active Directory domain. Servers are generally used to provide services to users or other servers.

3. Domain Controllers

Domain Controllers are the third most common device within an Active Directory domain. Domain Controllers allow you to manage the Active Directory Domain. These devices are often deemed the most sensitive devices within the network as they contain hashed passwords for all user accounts within the environment.
