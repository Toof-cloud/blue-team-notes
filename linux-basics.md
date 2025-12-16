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
       = /Users/tyronegabrielr.pascual/Desktop

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