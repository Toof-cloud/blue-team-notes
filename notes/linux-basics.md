Linux basic commands:

echo = output any text you provide 
e.g | echo hello 
output = hello

whoami = outputs as text the current user 
e.g | whoami
output = tyronegabrielr.pascual

ls = fname == listing
e.g | ls
output = Desktop		Downloads	Movies		Pictures	Public
Documents	Library		Music		Postman


cd = changing our current directory | go to a certaing dir
e.g | cd Desktop
output = goes to the Desktop dir
        = tyronegabrielr.pascual@Tyrones-MacBook-Air ~ % cd Desktop
          tyronegabrielr.pascual@Tyrones-MacBook-Air Desktop % 

pwd = Finding out the full Path to our Current Working Directory 
e.g | pwd
output = tyronegabrielr.pascual@Tyrones-MacBook-Air Desktop % pwd
       = /Users/tyronegabrielr.pascual/Desktoprfr

cat = concatenate, seeing contents of a file
e.g | cat sample.txt
output = This is a sample text document.

less = scrolling through a file
e.g | less sample.txt
output = (you can scroll through a file, like logs or long texts)

head = shows the first 10 lines of a file by default || for specification use -n x (number of lines) 
e.g | head -n 5 sample.txt
sample.txt =  Line 1: User login detected
              Line 2: SSH connection established
              Line 3: Failed password attempt
              Line 4: Successful authentication
              Line 5: Session opened
              Line 6: Command executed
              Line 7: Session closed

output =  Line 1: User login detected
          Line 2: SSH connection established
          Line 3: Failed password attempt
          Line 4: Successful authentication
          Line 5: Session opened


tail = showst he last few lines of a file | for specification use -n x (number of lines)
e.g | tail - 3 sample.txt
output =  Line 5: Session opened
          Line 6: Command executed
          Line 7: Session closed

find = finds what you want in all directories 
e.g | find -name password.txt
output = /Users/tyronegabrielr.pascyal/Desktop/password.txt

rwx = read, write, execute

r = read, view the file content or list directory contents
w = write, modify the file and create or delete files
execute = run the file as a program, enter the directory

Permission Groups = Owner | Group | Others
Example: -rwxr-x-r--
Breakdown:    - -> file type
              rwx -> owner
              r-x -> group
              r-- -> others

ls -l = ls -> lists files and directories
       = l -> long listing format
Example: ls -l
Output: 
-rwxr-xr-- 1 tyrone staff  4096 Dec 17 10:21 script.sh
drwxr-x--- 2 tyrone staff  4096 Dec 16 18:00 projects
Additional Info: ls -la -> view hidden files too, ls -lh -> instead of bytes (4K, 1M, 2G), ls -lt -> sort by newest time files first.

chmod = changing permissions
Example: 
chmod u+x file.sh == add execute to owner
chmod g-w file.sh == remove write from any group
cdmod o=r file.sh == set read only for others
Example 2:
chmod u=rw,g=r,o=r public.txt
chmod u=rw,go= secret.txt
chmod u=rwx,go=rx script.sh

Symbols: u -> owner/user, g -> group, o = others, a = all

Numeric Method:
Number - Permission:
4        read (r)
2        write (w)
1        execute (x)

Example: chmod 755 script.sh
Owner: 4+2+1 = 7 (rwx)
Group: 4+1 = 5 (r-x)
Others: 4+1 = 5 (r-x)

Additional Information:
Number	       Meaning
777	       Full access (❌ insecure)
755	       Scripts & binaries
644	       Text files
600	       Sensitive files (SSH keys)

Permission is importang in security as it orginazies who can read, write, and execute command to a file, having the right permissions to correct individuals organizes and is best for safety practices.


## Linux Logs (macOS Practice)

Linux systems store logs in `/var/log`.  
macOS uses a similar structure, making it useful for local practice.

### Authentication Logs
- Linux: `/var/log/auth.log`
- macOS: `/var/log/secure.log`
- Purpose:
  - Tracks login attempts
  - Records sudo usage
  - Useful for detecting unauthorized access

### System Logs
- Linux: `/var/log/syslog`
- macOS: `/var/log/system.log`
- Purpose:
  - System events
  - Service activity
  - Error messages

### Common SOC Commands
- `less` – safely view logs
- `grep` – search patterns
         - Global Regular Expression Print
         - Only prints the files that exist ad contain the pattern you ask for
         - If nothing matches it prints nothing

- `tail` – view recent entries
- `tail -f` – live monitoring
