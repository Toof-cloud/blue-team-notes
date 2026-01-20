# Active Directory 
- is a directory service developed bu Microsoft. It stores information about network object such as computers, users, and groups. It provodes authentication and authorisation services and allows administrators to manage network resources centrally.

## Active Directory Objects 
1. Users - also knows as security principals and can act upon resouces in the network.
    - Poeple 
    - Services

2. Machines - each computer that joins the active directory domain a machine object will be created.
Can also be a security principal.
- Note: Machine Account passwords are automatically rotated out and are generally comprised of 120 random characters.
- The machine account name is the computer's name followed by a dollar sign. For example, a machine named DC01 will have a machine account called DC01$.

3. Security Groups - Security groups are also considered security principals and, therefore, can have privileges over resources on the network.

## Security Groups 
1. Domain Admins - Users of this group have administrative privileges over the entire domain. By default, they can administer any computer on the domain, including the DCs.
2. Server Operators - Users in this group can administer Domain Controllers. They cannot change any administrative group memberships.
3. Backup Operators - Users in this group are allowed to access any file, ignoring their permissions. They are used to perform backups of data on computers.
4. Account Operators - can modify or create other accounts in the domain.
5. Domain Users - all existing computers inside the domain.
6. Domain Computers - all existing compouters inside the domain.
7. Domain Controllers - all the existing DCs on the domain.

---
# Domain Controller

Domain Controller - The server that runs the Active Directory.

Windows Domain - a group of users and computers under the administration of a given business. Centralise the administration of a given business. 

Remote Desktop Protocol - a protocol used to establish remote graphical sessions over the network.

1. Workstations
- Workstations are one of the most common devices within an Active Directory domain. Each user in the domain will likely be logging into a workstation. This is the device they will use to do their work or normal browsing activities. These devices should never have a privileged user signed into them.

2. Servers
- Servers are the second most common device within an Active Directory domain. Servers are generally used to provide services to users or other servers.

3. Domain Controllers
- Domain Controllers are the third most common device within an Active Directory domain. Domain Controllers allow you to manage the Active Directory Domain. These devices are often deemed the most sensitive devices within the network as they contain hashed passwords for all user accounts within the environment.

---
# Kerberos Authentication

Kerberos authentication 
- is the default authentication protocol for any recent version of Windows. Users who log into a service using Kerberos will be assigned tickets. Think of tickets as proof of a previous authentication. Users with tickets can present them to a service to demonstrate they have already authenticated into the network before and are therefore enabled to use it.

KDC - Key Distribution Center 
- installed on the DC in charge of creating Kerberos tickets to the network

TGT - Ticket Granting Ticket 
- sent by the KDC that allows the user to request additional tikets for specific services - and along with the TGT from the KDC is a session key, they need it to generate the following requests 
- TGT is encrypted by the KDC 

TGS - Ticket Granting Service
- are tickets that allow connection only to specific service they were created for
- username and timestamp is required to request a TGS and is encrypted by the session key, along with the TGT and SPN (Service Principal Name) that indicates the service and server name that is intented to access.
- TGS is encrypted using the service owner hash

NetNTLM 
- Legacy authentication protocol kept for compatibility purposes.

---

# GPO distribution

GPOs are distributed to the network via a network share called SYSVOL, which is stored in the DC. All users in a domain should typically have access to this share over the network to sync their GPOs periodically. The SYSVOL share points by default to the C:\Windows\SYSVOL\sysvol\ directory on each of the DCs in our network.

Once a change has been made to any GPOs, it might take up to 2 hours for computers to catch up. If you want to force any particular computer to sync its GPOs immediately, you can always run the following command on the desired computer:

Trees 
- if the company grows and their network expands into different countries you will do organize them by parting it into subdomains.

Enterprise Admins group 
- has the privillege to control in the whole domain while Domain Admins only control their subdomains.

Forests 
- The union of several trees with different namespaces into the same network.

Trust Relationships 
- if the other a tree in a forest wants to access a another tree in another forest's files they need 

---
# Windows Command Line

Windows Powershell 
- PowerShell is a cross-platform task automation solution made up of a command-line shell, a scripting language, and a configuration management framework.”
- PowerShell was developed to overcome the limitations of existing command-line tools and scripting environments in Windows.w

Common commands
- Get-ChildItem = lists the files and directories in a location specified with the -Path parameter
- Set-Location -Path = changes the current directory
- New-Item - Path = removes both directory and files
- Copy-Item = copy the file
- Move-Item = move the file to other dir or path
- Get-Content = similar to type/cat

### Piping
- is a technique used in command-line environments that allows the output of one command to be used as the input for another. This creates a sequence of operations where the data flows from one command to the next. Represented by the | symbol, piping is widely used in the Windows CLI, as introduced earlier in this module, as well as in Unix-based shells.
###
    - Get-ChildItem | Where-Object -Property "Extension"
    -eq ".txt"

- "Where-Object" filters the files by their Extension property, ensuring that only files with extension equal (-eq) to .txt are listed.

- -eq (i.e. "equal to") is part of a set of comparison operators that are shared with other scripting languages (e.g. Bash, Python).

- ne: "not equal". This operator can be used to exclude objects from the results based on specified criteria.
- gt: "greater than". This operator will filter only objects which exceed a specified value. It is important to note that this is a strict comparison, meaning that objects that are equal to the specified value will be excluded from the results.
- ge: "greater than or equal to". This is the non-strict version of the previous operator. A combination of -gt and - eq.
- lt: "less than". Like its counterpart, "greater than", this is a strict operator. It will include only objects which are strictly below a certain value.
- le: "less than or equal to". Just like its counterpart -ge, this is the non-strict version of the previous operator. A combination of -lt and -eq.

# Properties in Powershell
- Name:
The file or folder name only, without the full path. This is useful when you need to display, compare, or filter items by their names.

- Length:
The size of a file measured in bytes. This property applies to files (not folders) and is commonly used to filter files based on size, such as finding large files.

- CreationTime:
The date and time when the file or folder was originally created. This helps determine how old an item is.

- LastAccessTime:
The date and time when the file or folder was last opened or accessed. This is useful for identifying unused or rarely accessed files.

- LastWriteTime:
The date and time when the file or folder was last modified. This is often used to track recent changes.

- FullName:
The complete path of the file or folder, including the drive and directories. This is important when you need the exact location of an item.

- Extension: 
The file extension (such as .txt, .jpg, or .exe) that indicates the file type and is useful for filtering files by format.