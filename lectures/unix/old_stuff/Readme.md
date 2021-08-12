# Welcome

Welcome to week 1, day 1 of the Galvanize Data Science immersive. To set the expectations early,
this is a _programming_ course. You cannot complete this course just be lisetening to lectures or
doing the readings. Every day in this course, multiple times a day, you are going to be writing
code, reading code and using code written by other people.

Writing and reading code is both an art and a science. The best and fastest way to learn it  
is to get started quickly, make a lot of mistakes, investigate your mistakes and learn from them.
To that end, we are not going to spend a lot of time learning in-depth computer science. Some of that
will come naturally during the course of the class. Other aspects you may learn through years of
experience or by taking specialized courses outside of Galvanize.

For today, however, the goal is to get you up and running on your computer just enough to get started using python.

# Operating Systems

Every computer has an _operating system_ (OS), which is a complex set of programs that run the basic functions of your computer. There are dozens, or perhaps hundreds of different operating systems. Generally speaking, they all include the follow core components:

- Kernel (CPU, memory, processes, users)
- Device drivers (keyboard, mouse, displays, ...)
- File manager
- System processes
- User interface (shells and GUI)
- Permissions and security
- Standard programs

Fortunately, the OS handles much of this behind the scenes, so we rarely, if ever, need to manage these directly.

As a computer user, you're probably familiar with two of the world's most popular operating systems, Windows and Mac. There's a third operating system, really a vast family of operating systems, called Unix or Linux which you have probably heard of.

## Windows

Windows is the most popular operating system in the world, (at least on desktop sytems.) It gained enormous popularity in the '90s because its Graphical User Interface (GUI) made it easy for business users (rather than computer scientists) to use and it was aggressively marketed with business tools such as Excel, Word and Powerpoint. For many users, it bacame the default choice because it was pre-installed on computers and used by employers.

While this OS is enormously popular in business, it is not favored for programming for a variety of reasons. Recently, Microsoft has started adopting elements of Linux into Windows, the Windows Subsystem for Linux (WSL), however this arrangement is not yet mature or full-featured enough for this course. We will not be using Microsoft Windows, and hopefully that is the last time Excel will be mentioned in this class.

## Mac/Unix/Linux

In this class, we will be using operating systems from the Unix family of operating systems. Unix is a relatively old operating system, first developed in the 1970s. For a long time Unix had a reputation as being difficult, confusing and suitable only for serious computer scientists.

In 1991, Linus Torvalds, a Finnish computer scientist, started developing a new operating system called Linux based on Unix. Unlike Unix, which was proprietary and closed, Linux was free and open source so that users all over the world could contribute to its development. Linux, and the concept of free, open-source has been enormously popular. The Linux family of operating systems has grown and evolved so there are now dozens, or hundreds, of OSs in this family. You may have heard of some of the major ones such as FreeBSD, Red Hat, Debian, Fedora and Ubuntu. There are other versions, such as CentOS and Alpine, which are optimized for special use cases.

You're probably also familiar with the Apple Macintosh and the macOS operating system, which has historically been popular with creative computer users such as graphical artists, industrial designers, music and video producers and photographers because of its easy to use (and pretty) GUI. What you might not be aware of, is that since 2001, the macOS has actually been a version of Linux under the hood, with some proprietary addtions from Apple. For this reason, Mac is now also a popular choice for programmers.

In this class, we will be using either Linux or MacOS. Of the many choices of Linux, Ubuntu is encouraged. It works well "out of the box" with minimal setup, enjoys support from a very wide base of users and contributors and includes a variety of business programs. Many users find it can fully replace Windows. (And it's free!)

One important aspect of Linux is that everything is a file. This makes it relatively easy to access and control the settings and configurations of pretty much everything on your computer. Instead of clicking through menus, you edit text documents.

While both macOS and Ubuntu provide a graphical user interface, we strongly encourage users to use the _command line_ as the primary way of interacting with the computer. While this may be difficult at first, with practice you will come to appreciate its benefits.

## The Terminal Window

The terminal window is your primary tool for interacting with the computer. You should be in the habit of opening a terminal window as the first step of any task.

This lecture is about commands that can be used in the terminal. To work through it, open a terminal window side-by-side with this document.

- On Linux, use `\<ctrl>\<alt>'t'` to open a terminal window.
- On Mac, use `\<Cmd>\<space>` to open spotlight and then start typing 'terminal' and hit enter

To close a terminal window:
- On Linx, type `exit`
- On Mac, type `\<Cmd> -'w'`

You can have many terminal windows open at the same time. They can all be working on the same, or different, directories simultaneously.

The terminal window is (should be) the primary way you, as a developer, interact with your computer. Many computer users spend the majority of their time using applications (web browser, word processor, spreadsheet, file manager, etc). We will try to break that habit and use the command line more. This may take some time to adapt, but over time, you will find it is faster, more efficient, reduces distractions and gives you a better understandng of how your computer really works.

In some situations (i.e, inside Docker or on a remote connection) you will not have access to graphical tools like the file manager, so you will need to know how to work with files from the terminal.



### Protip:

> Be able to see your work and avoid distractions by keeping your terminal window maximized or docked. Use `\<Windows>` with arrow keys to maximize, dock-left or dock-right). If you have two monitors, use `\<Windows>\<shift>\<arrow>` to move a window from one monitor to the other.


\<!-- Terminal window commands can also be executed from inside ipython or jupyter notebook by pre-pending
an exclamation point (also kown as a 'bang') to a command.

`code
# Print Working Directory (pwd)
pwd
`

`code
# list files in the current directory

ls
` -->

# Linux fundamentals

Now that we have access to the terminal window, we can talk directly to our computers. Let's explore some of the basic commands. Because the terminal window is the primary way of interacting with a computer, it is an extremely powerful tool with hundreds of commands that can be combined to control any function a computer can do. That is not the goal of this course. In this course, we are going to focus on using the terminal window for python programming and to setup and organize our work. To that end, we are going to narrow the scope of our use of the terminal window.

## Objectives

- Perform basic directory operartions from the command line
- Perform basic file operations from the command line
- Launch a text editor from the command line
- Enter ipython at the command line
- Start a jupyter notebook from the command line
- Get help using `man`
\<!-- - Manage a process with job control -->
\<!-- - Write a simple regular expression -->
\<!-- - Use `grep`/`sed`/`awk`/`cut`/`paste` to process/clean a text file -->
\<!-- - Perform “survival” edits using vi -->

# Shells

A shell is a computer program that allows you to type in text and run commands. It is often referred to as the "command line" or the 'terminal" although some would argue that these words have slightly different meanings. 

For the most part, you use the command line by typing in text and the computer responds by printing out a line (or several) lines of text. In this 
use case, the text from your keyboard is the input and the text to the monitor is the output. Nearly all Linux programs work by taking in text from 
one input, doing something to it or with it, and delivering text to the output. 

One of the particularly powerful features is the ability to redirect inputs and outputs. The input to a program can come from your keyboard, but it may also come from a text file, a webpage, the result of a calculation, a variable stored in memory or the result of another program.

The output from a program can also be redirected. Instead of printing the results to the monitor, the output can be redirected to a text file or another program.

In this way, commands can be chained together so that the output of one passes to the input of the next. Instead of entering commands with the keyboard, they can be saved in a text file for repeated execution and modification.  While this can be very, very powerful, it also gives command scripting a reputation for being cryptic and confusing. 

One particular place this is useful is in the file `~/.bashrc` or, on a Mac, `~/.bash_profile.`. These are text files that contain bash commands 
that are exectued automatically whenever you open a terminal window. They are a useful place to put commands that customize your shell to your personal preferences.

In this class, we will focus on python programming, so we will not spend much time on bash scripting. You may wish to investigate it more on your own.

Let's take a moment to look at our shell. The shell is just a program that runs on the operating system. When we open a new 
terminal window, we see a mostly blank page. On my system, the only thing displayed is:

`
land@nitro ~ $
`

This is known as the command prompt. Let's look at the pieces of it. The first part is my username, `land` 
the `@` indicates that I'm working on a computer named `nitro`. Mostly in this course, we will be woring on our own computers, 
so you will see your username@computername nearly all the time. Later, we will be working on cloud-based computers, such as 
Amazon Web Services (AWS). When that happens, we will no longer be working on our own computer, but rather a remote computer 
somewhere in the cloud. When we do that, our prompt will change to the username and computer name; something like `ubuntu@192.168.0.1`.

After the computer name is the `~` character. In Linux, `~` is shorthand for "the home directory of the current user."  We will use this abbreviation a lot, particularly for `~/.bashrc` (or `~/.bash_profile`)

After the `~` is a character, usually `$`. The dollar sign indicates that the terminal is ready to accept your input from the keyboard. 

There may be other information displayed as part of the prompt, such as the name of a virtual environment, or the name of a branch in a git 
repo. Text may also be color-coded to indicated various conditions. These options can be adjsuted in the `~/.bashrc` file.

Let's do a few basic things to get familiar with our shell. First, we can ask our shell to identify itself by typing:

`code

echo $0

`

`echo` is a command that tells the computer to repeat any input. For example `echo Hello World` will just print "Hello World". By itself, this doesn't do much, but when combined with input/output redirection, it can be handy.

  Note: most commands are case sensitive. `echo` will work, but `ECHO` may not.


In the command `echo $0`, the dollar sign tells echo to get its input from an environment variable, the environment variable named `0`. This is just the name of the shell program. On my computer, this returns `bash`. There are other shell programs such as 


- sh (Bourne Shell)
- ksh (Korn Shell)
- **bash** (Bourne-again shell)
- csh (C shell)
- tcsh
- zsh


Linux generally uses bash, Mac has recently switched to zsh as default. You may, if you like, switch between them, but they all pretty much work the same and for the purposes of this course, it makes no difference.

The [original computing terminal](https://en.wikipedia.org/wiki/Computer_terminal) was a teletypewriter (TTY). Commands were typed and zapped over to the room-sized computer mainframe. [UNIX](https://en.wikipedia.org/wiki/History_of_Unix) was developed in this environment, so many commands retain the terminology of teletypewriters and tape drives.

For an interesting book on the history of computing see: [A People's History of Computing in the United States](https://www.hup.harvard.edu/catalog.php?isbn=9780674970977)

A few other basic shell commands which you may find useful:


- `history` will show you the most recent commands you have entered
- `clear` will clear the screen
- `env` will show a list of environment variables, which are accessed with the `$`. We have already seen `$0` (shell program). Others include $USER (the name of the current user), `$HOME` (the user's home directory) and $PATH (a list of directories where the computer will look for programs to run.) Later in the course, we may use the environment variables to store values that we need to access frequently, but don't want to type. We will not need to interact with most of these directly.
- `sudo` is short for `super user do`. It allows you to run a command as a super-user. Sometimes this is necessary when installing programs or making adjustments to protected files. Be careful! `sudo` gives you unlimited power over you system, including the ability to delete critical files, so you it carefully.

## Keyboard shortcuts

Although it might be difficult at first, it really is faster and more efficient to use the keyboard instead of the mouse. The shell provides a couple of handy features to help make this easier:
- Use the up arrow key to recall the last command you typed (or hit up several times to scroll back through the history of recent commands). When you find the one you want, just hit "enter." 
- Use the `tab` key to auto-complete the names of files and directories. For example, to change to a directory with a long name, such as `galvanize_dsi_work_directory`, just start by typing `cd ga` and then hit the tab key. If `ga` is your directory is the only one that start with `ga` it will automatically fill in the rest for you. If there are more than one directories that start with `ga`, it will beep. If you hit tab again, it will show a list of all the possible directories. Then you can just type the next few letters until the name is resolved.
- to abandon a command you have started but decided not to finish, hit `\<ctrl> - c`.
- If there is output on the screen that has not finished, hit `\<ctrl> - c` to stop it and return to a command prompt (`$`)
- To repeat a command you have used previously, type `\<ctrl> - r` and then start typing the command. It will auto-complete from there.

## Directories

The organizing princple of Linux is "everything is a file." All files are stored in directories and directories are organized in a tree structure.
At the base of the tree is a directory called "root", which is symboized by `/`. All other directories are subdirectories of this directory.

When you start up a terminal window, it will take you to your home directory. As mentioned before, the shorthand for this directory is `~` which is equivalent to `$HOME`. To see where your home directory is located in the tree:

`
echo ~
`

or

`
echo $HOME
`

To see which directory you are currently in (which is not necessarily your home directory), type `pwd` which is short ofr "print working directory"

This is also available as an environment variable as:

`
echo $PWD
`

or
`
$PWD
`


As a general rule of thumb, you should keep all of your work in your HOME directory, or subdirectores of HOME. The other branches of the tree, including the root directory and its subdirectories, are for files and programs the computer needs. It is best to let the comptuer manage these most of the time.

Your HOME directory contains sub-directories such as:
- Downloads
- Pictures
- Music
- Videos
- Documents

`Documents` is a good place to keep all of your work, including all of the material for this course.

### Listing Contents

Very often, you will need to see the contents of a directory. The command for this is `ls` which is short for 'list`. 

Keep this in mind:

- `ls` by itself will not show "hidden" directories or files. A hidden directory or file is one whose name starts with "`.`"
- `ls -a` will show *all* the contents, including hidden files and directories.
- `ls -l` will display in a list format, which can be easier to read if there are more than a dozen or so entries.
- There are a number of options for `ls` to change the output style
- unless otherwise specified, `ls` will show the contents of the current directory. You can use it to examine other directories (without changing into them) such as `ls ..` (parent directory), `ls ~` (home directory) or `ls child/child/child`.


### Changing Directories

One of the most frequent tasks at the command line is changing directories. The command is `cd` which is short for "change directory".

- `cd` \<enter> will take you directly to your home directory.
- `cd ~` will also take you to your home directory
- `..` is short for "the parent directory of the current directory. So `cd ..` will take you 'up' one level.
- `.` is short for "the current directory." `cd .` doesn't do anything - it just takes you to where you already are.
- `cd \<directory name>` will take you to the child directory of the current directory. (Don't forget to use \<tab> to auto-complete!)

You can string these together. For example `cd ~/Documents` will take you to the 'Documents' subdirectory of HOME, regardless of where you were before.

If you're in a child directory (e.g. `~/Documents/child_1`) you can use `cd ../child_2` to go back one directory and then into the other child directory.

`cd ../../..` will take you up three levels. `cd child_1/child_2/child_3`  will take you three levels down.

### Making Directories

The command to make a new directory is `mkdir`.  Note that this will make a new directory, but will not move you into it. After doing `mkdir` you'll need to `cd` into it.

As before, you can string directories together such as `mkdir ~/Documents/work' or `mkdir ../child_2`

Protip:
  You can have spaces in directory names and file names, but it is better not to. You may need to use quotation marks around these names and it can make \<tab> auto-complete more difficult.  A good practice is to use the underscore `_` in directory and file names instead of spaces.


### Copying and Renaming Directories

Directories can be copied using the `cp` command. (Short for "copy"). This takes two arguments: first the current name of the directory, second the new name of the directory:

 `cp current_directory new_directory`.

 To rename a directory, use `mv` (short for "move"), with the same two arguments: current_name, new_name.


### Deleting Directories

Like files, directories can be deleted with the command `rm` (short for "remove"). However, linux will prevent you from accidentally removing a directory, so you must use `rm -rf \<directory name>`


## Files

As mentioned before, pretty much everything in Linux is a file. Our job, as programmers, is to write code into files. So we'll be spending a lot of time making and editing files.

All files have the following attributes:

- A directory where they are located.
- A filename. (remeber to avoid using spaces)
- An user who owns the file
- A group who owns the file
- A set of permissions for the user, group and everybody else
- contents of the file

In addition, many files will have a file extension and associated programs that work with the file.

In this course, we won't have to worry much about file ownership or permissions. (Although we will a little bit when we start to use AWS.) To see the owner and group of a file,
use `ls -l \<file_name>`. This will produce output such as:


`
-rw-rw-r-- 1 user group 0 Jun 16 14:01 my_file
`
The first character (in this case, "-") indicates that this a file (rather than "d" for directory.)

The next nine characters indicate permission. These are arranged in three groups of three characters.

The first group shows Read/Write/Execute permissions for the owner of the file. A "-" indicates that the permission is not granted. An 'r', 'w' or 'x' indicates that the permission is granted.
The second group of three characters shows the read/write/execute permissions for the group that owns the file.
The third group show the permissions for everyone who is neither the owner, nor in the group.

Next is the name of the user who owns the file. This is usually the person who created the file.
After that is the name of the user group who owns the file.

The date and time indicates the last time the files was modified or 'touched.'

Finally is the final name.

Two commands that are useful for modifying ownership and permissions are:

- `chown` for "change owner" 
- `chmod` for "change mode"

### Creating Files

There are several ways to create files. In this course, we will primarily be using a text editor (VS Code) to create and edit files, but linux also gives us some 
utilities at the command line to work with files.

- `touch \<filename>` will create a new, empty file if it does not already exist. If the file does exist, it will set the "last modified date and time" to the current time.
This can be helpful if you are sorting or filtering files by when they were last used.

As mentioned before, `echo` will just cause the computer to repeat any input you give it. If you don't add an output, it will output to the terminal window. But we can 
*redirect* the output into a file. 


  `echo "Hello World" > hello_world.txt`


Creates a new text file with the contents "Hello World".  The single forwards arrow (`>`)  redirects the output such that, if the file already existed, it will replace all the contents of that file with the new text.

Another option is to use the double forward arrow (`>>`). This will add the echoed text to the end of the existing file, without altering the existing content.

To include a new line character (`\n`) in the echo, you need to specify the `-e `option.

`echo -e "\nHello Again" >> hello_world.txt`

Another option is to create a text file from the output of a command. For example the `history` command shows a list of recent commands typed at the terminal.
If you don't want to see these on the screen, you can redirect the output into a file:

`history > history.txt`

These shell commands can be quick and handy, but for more advanced file editing, we will use a text editor. In this class, VS Code is the preferred text editor.

You should be able to open a text file for editing using:

`code \<file_name>`

To open a directory for editing in VS code, remember that the `.` signifies "the current directory."

`code .`

### Viewing the Contents of a File

There are several quick commands to see the contents of a file.

- `cat \<filename>` will print the full contents to the screen
- `head \<filename>` will show the first ten lines
- `tail \<filename>` will show the last ten lines
- `more \<filename>` will show the file one screen at a time. Press \<space> to advance to the next screen, or `\<ctrl> - c` to abort.
- Pardoxically, `less \<filename>` does pretty much the same thing as `more` but has some additional options

As before, you can redirect the output, so that `cat \<filename> > new_file.txt` will create a new file with the contents of \<filename>.

Note that `filename` is the input to `cat`. Although this input generally comes from the keyboard, it could be redirected from another source, such as the output of a different file or calculation.

There are many other useful functions to sort, filter and analyze text from an input to an output. We won't go into those now, but I will mention one. Suppose you want to review your `history` 
to see the last time you used some command, for example `mkdir`. One option would be to "pipe" the output of `history` to the `grep` command. `grep` looks for any line that contains a piece of text 
and returns only that line.  The vertical line (`|`) is known as a "pipe"

`history | grep mkdir`

To reiterate: in general, we will be using VS Code to view the contents of a file, especially if we want to make edits. But for very short examples, these commands are handy.

### Copying and renaming files

Like directories, files can be copied using the `cp` command with two arguments, source and destination.

`cp \<filename> \<new_file>`

We can also move a file:

`mv \<filename> \<new_filename>`

Note that this can be used to move or copy a file to a differnt directory:

`
mv my_file ../../child_1/child_2/new_file
`

### Deleting Files

Files can be deleted with `rm` (short for "remove")

`
rm \<filename>
`

## File Types

There are many different file types, most of which are indicated by an extension, which is a few letters after the ".' in the filename.
The file extension serves as a hint to the operating system about what type of progam should be used to open the file.

Some file type you are probably familiar with:

- .txt: text file
- .pdf: A Portable Document Format (PDF) file
- .html or .htm: Hypertext markup language, for example, a webpage
- .csv: Comma Separated Variables, a spreadsheet (usually of numbers), in plain text



Because this course is primarily focused on python programming, the main file types we will be using are:

- .py: A python file, or a "script". These are plain text files that can be edited with any text editor. VS Code is preferred.
- .ipynb: A jupyter notebook file (or ipython notebook file). These are similar to .py files, but contain additional tags so that they are visible in a web browser


An additional file type we will be using is:

- .md:  A Markdown file. You can think of markdown as a simplified word processor. It uses tags to format plain text. Like any plain text file, these are edited in VS Code.

We will be using Markdown files to document our projects. All projects should include a markdown file called `README.md` which serves as the introduction to the project.
Markdown files can include basic formatting, bulleted lists, embedded images and links.


## The `man` command

Linux provides many, many more commands than those listed here, and all of the commands listed above can take a variety of options. We won't go into those here. 
You can explore them by using the command `man`. This command prints out the instruction manual for any command.

For example, `man ls` will tell you what the `ls` command does and describe all of the optional arguments.

# Getting Started in Python

As mentioned before, this class is largely a *python programming* class. We will be spending the vast majority of our time in python. Now that we're familiar with 
our operating system, we need to get into python and start programming as quickly as possible.

There are several different options for python programming. Once you have python installed, all you need is terminal window. This is fine for very, very simple 
calculations, but for anything more than a few lines of code, you're going to need to save and edit code.

In this class, we will be programming in python in two environments, ipython and jupyter-notebook. There is a third approach which uses python to run scripts at the command line.
We will use this a bit later in the course. For now, we will focus on our two main environments:

- VS Code and ipython or terminal
- Jupyter Notebooks

**Many students fall into the trap of only using one of these environments. To complete this course you will need to be proficient in both.**

# iPython and VS Code

To get started programming using the ipython/VS Code approach, follow these steps:

- Open a terminal window
- Use `mkdir` if necessary to create a directory to save your work. 
- `cd` into this directory
- Type `code .` to open VS Code
- Create a new, blank file in VS Code using `\<ctrl> - n`
- Type some code. (for example `print('Hello World')`)
- Save the file with a `.py` extension. (for example, `example_1.py`) Remeber to use keyboard shortcuts!
- Leave VS Code open and return to the terminal window
- In the terminal window, type `ipython`

At this point, you should see something like this:

```
land@nitro unix (master) $ ipython
Python 3.7.6 (default, Jan  8 2020, 19:59:22) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.12.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]:      
```

Notice that the prompt has changed from a `$` to `In [1]:`. This indicates that we are no longer working with the shell, but rather inside an interactive python environment.

- Run the file using the command `run example_1.py` (Remember to use \<tab> to auto-complete the file name.)

You should now see the output `Hello World`, indicating that your script ran, followed by a new line for input: `In [2]:`.

**If this didn't work, seek help immediately**

To further develop your code, you can type commands directly at the ipython prompt, or into the .py file in VS Code. 

To re-run the code, remember to save the file in VS Code, return to ipython and repeat the `run` command (using up arrow key to recall the previous command)

When you are done working in ipython, just type `exit` at the prompt to return to the terminal window.


# Jupyter Notebook

The second programming environment we will be using is a browser-based interactive tool called Jupyer Notebook. 

To launch Jupyter Notebook, use the following steps:

- Open a terminal window
- Use `mkdir` if necessary to create a directory to save your work. 
- `cd` into this directory
- Type `jupyter notebook`
- This will open a webbrowser with a page called 'Jupyter' that displays the files in your directory.
- Click on the `new` button at the right to create a new Python 3 notebook. This will open a new page in the browser
- In the first cell, type some python code (e.g. `print('Hello World`))
- Hit \<ctrl>-\<enter> to execute the cell
- You should see the output from this line of code below the cell
- You may then add additonal lines of code in the cells below

To quit a session with jupyter notebook, return to the terminal window and hit \<ctrl>-c twice.

**If this didn't work, seek help immediately**

## Congratulations, you have now written python code in two different environments!

Remember: To complete this course, you will need to be proficient in both techniques. Don't fall into the trap of only using one or the other.


## An Alias for Jupyter Notebook

Because we are going to be using jupyter notebook frequently in this course, and to promote use of the keyboard, rather than the mouse, 
you may find it useful to create an alias to launch jupyter notebook. I like to use 'jup' as short for 'jupyter notebook'

First, check to see if this command is already in use by trying to run `jup` at the command line.

```
Command 'jup' not found, but can be installed with:

sudo apt install jup

```

Next, add an alias to your bash profile:
- On Linux:

`echo -e "\nalias jup='jupyter-notebook'" >> ~/.bashrc`

- On Mac:
`echo -e "\nalias jup='jupyter-notebook'" >> ~/.bash_profile`

We can check that this was added sucessfully as the last line in our profile settings with any of the following commands:

- `cat ~/.bashrc`
- `cat ~/.bashrc | grep jup`
- `grep jup ~/.bashrc`
- `more ~/.bashrc`
- `less ~/.bashrc`

Alternatively, we could open the file in VS Code and examine it there using `code ~/.bashrc`

Bear in mind: just because we have written the alias command into our ~/.bashrc file does not mean that the alias has been created. 
~/.bashrc is run automatically whenever a new terminal window is opened, or it can be run at any time with the command `source ~/.bashrc`.
Only after it has been sourced wil the `jup` alias work for us.

Another alias you might find useful:
`echo -e '\nalias goog="xdg-open https://google.com &"' >> ~/.bashrc`

Or, on a Mac:

`echo -e '\nalias goog="open https://google.com &"' >> ~/.bash_profile`

All data scientists use google a lot. Now you can open it just by typing "goog".


# Python and REPL

There is a third approach to running python which we will use less often, which is to run a script from the command line as follows:

- Open a terminal window
- Use `code .` to open VS Code
- Create a python script and save with a `.py` extension
- return to the terminal window and type `python \<filename>`

Python will then run the script and return the results in the terminal window. The disadvantage of this approach is that, after it is done, 
it exits python and returns to the shell prompt. It does not retain the values of variables or the ability to keep programming after the script 
is done.

We will be using "REPL" to write our programs. REPL stands for "Read-Evaluate-Print-Loop" and basically means that we can write, run, re-write and 
re-run our scipts over and over again as we develop them. After each step, all the variables stay in memory so that we can continue to inspect and 
use them. Running scipts from the command line using python, rather than *interactive* python makes this more difficult.

## A Note on Text Editors

In this class, we will primarily be using VS Code to edit text files. In some environments, such as working on a remote system, VS Code might not 
be installed. In this case, you can use VIM or nano, two old-school text editors that are always available. 


<!-- 


# Processes

A process is a program or task running on a computer.

A single process consists of:

- One or more threads
- Program text
- Memory for stack and heap
- File descriptors
- Environment
- Owner and privilege

To view running processes and their details, type `ps`

`
ps
`

By default, `ps` only shows processes started by you (that is, the userid associated with you, and not processes started by other users or the `root` user), and started in the same terminal that you just typed `ps` into.

To show all processes started by all users in all terminals, typ `ps waux`

`
ps waux
` -->


# Command-line Options

Most commands can take options.

Usually

- single-character options are preceded by `-` and can be combined
- full-word options are preceded by `--`
  Usually.

Examples:

- `python --version`
- `ls -l`
- `ls -la`

See `man` _command_ for more details.


## Managing processes

- `ps` (display running processes)
  - `ps waux` (display all processes from all users)
- `kill` (terminate a process)
  - If you have a process running in your terminal, `\<Ctrl>-C` should kill it. If that fails, you'll have to use `kill`.
- `\<bash command> &` (run process in background. [more info](https://bashitout.com/2013/05/18/Ampersands-on-the-command-line.html))
  - If you have a process running in your terminal, `\<Ctrl>-Z` pauses the process and sends it into the background. It does NOT kill that process.
- `jobs` (show background processes running in the current shell session; each process has a _job number_. [more info](http://tldp.org/LDP/abs/html/x9644.html))
  - `bg \<job number>` (resume a suspended job and run it in the background)
  - `fg \<job number>` (send a background job into the foreground)

### example: killing a process

To kill a misbehaving (or frozen) process, type `kill \<PID>` (where `\<PID>` is the process id listed in `ps` above).

Sometimes you may have the use the `-9` option of the `kill` command, which you can think of as a "hard shutdown" of a process. `kill -9 \<PID>`

Try the following in your terminal (not using the notebook). `$` represents the shell prompt, don't type `$`

`
$ sleep 100 &
$ jobs
$ ps
$ kill \<the PID for sleep>
$
`


## Downloading from the web with `wget` and `curl`

`
ls
`

The default command to retrieve content from web servers is `curl -o` on Mac OS X.

`
curl -o bee2.jpg https://upload.wikimedia.org/wikipedia/commons/7/77/Thomas_Bresson_-_Hym%C3%A9nopt%C3%A8re_sur_une_fleur_de_pissenlit_%28by%29.jpg
`

`
ls
`

To many Linux user, `wget` is the go-to tool for downloading; however it is not on Mac OS X by default. If you really like the original `wget` on Mac OS X, try install with `brew`

`
brew install wget
`

`
wget https://upload.wikimedia.org/wikipedia/commons/4/42/Apis_mellifera_flying2.jpg
`

`
ls
`

`
open Apis_mellifera_flying2.jpg
xdg-open Apis_mellifera_flying2.jpg
`

# [Regular Expressions](https://en.wikipedia.org/wiki/Regular_expression)

The `grep` command (and many languages) use regular expressions to match files.

Most characters match themselves. Some don't.

- `.` matches anything other than a newline
- `*` match zero or more of previous atom
- `+` match one or more of previous atom
- `|` match either previous or next item
- `[abc0-9]` match any of characters within
- `\` escape previous character
- `\(\)` for grouping (use egrep to use without `\`)

[Learn regular expressions](https://regexone.com/)

[Play regex golf](https://alf.nu/RegexGolf)

# Environment Variables

List with `env`

Set with `VAR=foo`, or `export VAR=foo` when run from a script (e.g., your `.bash_profile`)

# Basic vi/vim

Two main modes

- Insert mode (typing stuff inserts it in file)
- Command mode (each key has meaning)

The _escape_ key brings you to command mode; _i_ enters insert mode

Helpful commands

- `i` (enter insert mode)
- `a` (enter insert mode after this character)
- `dd` (delete a line)
- `100G` (go to line 100)
- `:wq` (save and exit)
- `:q!` (exit without saving)

# How does my shell know where all these commands / programs are?

When you type a command, your shell looks for the executable file corresponding to that command. How does bash know where that file is?

For example, when you type `ls`, your shell runs the executable file `ls` in your `/bin` folder.

`
which ls
`

`
ls /bin/
`

`
which grep
`
