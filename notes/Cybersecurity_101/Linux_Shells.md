### Linux Shells
- When interacting with a shell, you must be in the directory where you want to perform operations. By default, when you open a shell in most of the Linux distributions, you will be in your home directory. To see your current working directory, you can execute pwd, which stands for Print Working Directory, as shown in the terminal below:.

# Linux Commands
- echo $SHELL = shows what shell you are currently using
- cat = read a file
- cat /etc/shells = list down all the shells you have
- cd (file) = go to a directory
- ls = read the contents of the directory
- grep = search any word or a pattern in the current directory
- Ctrl + D  or exit = logout of the shell and go back to the default shell


## Shell Scripting
- A shell script is nothing but a set of commands.
- Variables
    - A variable stores a value inside it. Suppose you need to use some complex values, like a URL, a file path, etc., several times in your script. Instead of memorizing and writing them repeatedly, you can store them in a variable and use the variable name wherever you need it.
- To execute a script check first its permission if you can run it. (chmod +x (scriptfile))
- To run the script after fixing the permissions (./(filename)). Use "./" before the script to run, this tells the shell to execute the file.
- Loops 
    - You can also perform iterations in scripting.
- Conditional Statements
    - Run or Continue specific line of code when the condition is met.
    - 'fi' is used to end the condition
    - shebang = A shebang is the first line of a script that tells Linux which interpreter should run the script.


## Types of Linux Shells 
- Bourne Again Shell (Bash) - is the default shell for most Linux distributions. Bash came as an enhanced replacement for these shells, borrowing capabilities from all of them.
    - Has scripting capabilities
    - Offers tab completion features
    - Keeps a history file and logs all commands.

- Friendly Interactive Shell (Fish) - is also not default in most Linux distributions. As its name suggests, it focuses more on user-friendliness than other shells. 
    - Simple syntax
    - Has auto spell correction
    - Customizable command prompt
    - Also has tab completion, scripting, and command history

- Z Shell (Zsh) - is not installed by default in most Linux distributions. It is considered a modern shell that combines the functionalities of some previous shells.
    - Provides advanced tab completion and is also capable of writing scripts, also has history functionality and auto spell correction.

