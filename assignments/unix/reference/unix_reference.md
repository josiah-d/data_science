# Introduction to Unix

## Background

Unix is a multitasking, multiuser computer operating system. Today, most
computers are either built on top of a Unix / Unix-like operating system or Microsoft
Windows. There are a number of differences between them, but the key
difference is that Unix is open-source, which means that anybody and everybody
has access to the source code (this isn't true for Windows).

There are a number of different distributions of Unix. Two of the
most popular are Mac OS and Linux. While different distributions of Unix will
have programs that are unique to that distribution, the majority
of the programs in each Unix distribution will be the same. Today we're going
to be working with some of the programs that are common across all
distributions.

## Generalization
All Unix shells implement the following paradigms:

**wildcard matching**  
`doc*` matches `doc` and `document` but not `dodo`  

**piping**  
`ls -l | grep key | less`  
_List files in the current directory (`ls`), retain only the lines of output containing the string "key" (`grep`), and view the result in a scrolling page (`less`)_.

A pipeline is a sequence of processes chained together by their standard streams, so that the output of one process (stdout) becomes the input (stdin) to the next.

**command substitution**  
`nano fgrep -l unix *.md`  
_Search for all the markdown files containing the string 'unix' using fgrep and then edit any that are found using the nano editor._

Command substitution allows a command to be run and its output pasted back on the command line as arguments to another command.

**variables**
```#!/bin/sh
message="hello world"
echo $message
```

**here documents**

    $ tr a-z A-Z <<END_TEXT
    >   capitalize this text
    >   END_TEXT
    CAPITALIZE THIS TEXT
_Text is passed to the `tr` command (transliterating lower to uppercase) using a here document._

A here document uses I/O redirection to feed a command list to an interactive program.

**control structures for condition-testing and iteration**
```
if [ $a -gt 0 ]; then
      echo "${a} is greater than zero"
else
      echo "${a} is less than or equal to zero"
fi
```

As an aside, this is equivalent to the following in Python:
```
if a > 0:
      print("{value} is greater than zero".format(value=a))
else:
      print("{value} is less than or equal to zero".format(value=a))
```

Now that you have a taste for what Unix can do, let's go back to basics.

## Basic Commands

One thing to note before actually getting to Unix commands is that
these _commands_ are the programs referred to in the background
section. Technically speaking, each one of these commands is actually a small
little program that somebody has built.

### Navigation

In terms of navigation, the following three commands are going to be your
bread and butter:

* `pwd` - Stands for `print working directory`; this will write the full
  pathname of the current working directory to the terminal
* `cd` - Stands for `change directory`; this will allow you to navigate between
  different folders/directories in your directory structure
* `ls` - Stands for `list`; this will list the files in the current working
  directory

Let's walk through these in a little more detail.

1.) `pwd` is fairly straightforward, but in talking about pathnames it's
important to talk about the Unix filesystem tree and to make the
distinction between absolute and relative pathnames. In a Unix-based
operating system, files are organized in a tree-like pattern. The top
directory in a filesystem is called the *root directory*, which contains
files as well as subdirectories, which contain more files and
subdirectories, and so on. 

Note that the terms directory and subdirectory are synonymous with the term folder.

When discussing the pathname of a file or subdirectory, we need to note
whether it is an absolute path or a relative path:

* An **absolute pathname** begins with the root directory and follows
  the filesystem tree, branch by branch, from a designated starting point. These
  will always begin with a forward slash `/` (meaning start from the root of the system)
  or a tilde forward slash `~/` (meaning start from your home directory).

* A **relative pathname** begins with the current working directory
  and follows the filesystem tree, branch by branch, from the current
  working directory. These will not begin with a forward slash `/`.
  Relative paths may start with the name of a file or folder (e.g.
  `galvanize/ds-day-1`) or with one or two dots. `./` means the current
  directory, and `../` means the directory *above* the current directory,
  also known as the *parent* directory.

The distinction between relative and absolute paths is a *vitally important*
concept that you *must* understand completely. Ask as many questions as it takes for this to make sense.

2.) `cd` allows you to change from one directory to another by simply placing
the name of the directory you want to go to after the `cd` command. `cd`
accepts a relative pathname or an absolute pathname, but if you pass it a
relative pathname, then that pathname has to be accessible via the current
working directory.

Assuming that my username is `elliot` and the repo for today is located at the path
`/Users/elliot/galvanize/ds-day-1`, then I can change to it using any of the following absolute paths:

```bash
cd ~/galvanize/ds-day-1
cd ~elliot/galvanize/ds-day-1
cd /Users/elliot/galvanize/ds-day-1
```

Note that `~/` is short for "my home directory" and `~elliot/` means "`elliot`'s home directory";
therefore, if my username is `elliot`, then `~/` and `~elliot/` mean exactly the same thing.

If I am already in my home directory (`/Users/elliot`), I also can use a relative path. Here are two examples of relative paths to the same place:

```bash
cd ./galvanize/ds-day-1
cd galvanize/ds-day-1
```

Some special ways of using the `cd` command involve the following:

```bash
cd ~  # Change to your home directory.
cd    # Another way to change to your home directory.
cd .. # Change directory to the directory above the current directory.
```

3.) `ls` allows you to list the files in the current directory or any
directory placed after the `ls` command. Similar to the `cd` command,
`ls` accepts a relative pathname or an absolute pathname, but if you pass
it a relative pathname, then that pathname has to be accessible via the
current working directory.

Assuming that I am in the `~/galvanize/ds-day-1` folder, I can
issue the following commands to see what's here:

```bash
ls     # List the files and directories in galvanize/ds-day-1
ls -l  # The -l is a dash followed by a lowercase L. Shows details.
tree   # Show a directory tree of what's here.
```

Note: if you're on a Mac with Homebrew and the `tree` command isn't installed, `brew install tree` will install it for you.

### Creating and Removing files

In terms of creating and removing files, the following commands are used:

* `touch` - create a file/change the timestamp on an already existent file
* `rm` - remove/delete a file

1.) In its default usage, `touch` is a command that will open and close a file
while leaving its contents unchanged. The end result is that it changes
the access timestamp associated with the file. However, if we `touch` a non-existent filename, an empty file with that name will be created.

```bash
touch existing_file     # Update the timestamp of existing_file
touch nonexistent_file  # Create nonexistent_file (paradoxical?)
```

2.) `rm` is a command that allows us to delete files by simply placing the
name of the file(s) to delete after the `rm` command.

```bash
rm file1.txt  # Delete file1.txt
rm file2.txt file3.txt  # Delete both file2.txt and file3.txt
```

**Note**: The results of the `rm` command are permanent, so **be careful**
when using it.

### Creating and Removing Directories

In terms of creating and removing directories, the following commands are used:

* `mkdir` - create a directory
* `rmdir` - remove a Directory

1.) `mkdir` allows us to create a new directory(s) simply by placing the name of our newly created directory(s) right after the `mkdir` command:

```bash
mkdir new_dir1 # Create new directory called new_dir1 in the current directory
mkdir new_dir2 new_dir3 # Create new directories called new_dir2 and new_dir3
                        # in the current directory.
```

2.) `rmdir` allows us to delete an **empty** directory by placing the name of
the directory to delete right after the `rmdir` command:

```bash
rmdir empty_dir # Delete the empty directory called empty_dir
```

If the directory we want to delete is not empty, and **we are sure**
that we want to delete it, then we can add a **recursive** option to the
`rm` command from above:

```bash
rm -r nonempty_dir # Delete nonempty_dir and all of its contents.
```

### Moving files and Directories

The two commands that we use to move files and directories around are:

* `cp` - copy files and directories
* `mv` - move and rename files and directories

1.) `cp` allows us to copy a file or directory from one location to another.
It takes two arguments - the name of the file or directory to copy, and
the name of the file or directory to copy it to (i.e. from location and
to location). If we are copying a directory, we have to add the `-r`
recursive option to the `cp` command.

```bash
cp foo.txt bar.txt       # Make a copy of foo.txt called bar.txt
cp foo.txt spam/         # Copy foo.txt into the spam directory.
cp foo.txt spam/bar.txt  # Copy foo.txt to spam/ as bar.txt

cp -r dir1 dir2  # Copy dir1 and all its concents into dir2.  
```

2.) `mv` allows us to move and rename a file or directory (getting rid of the original). Similar to the `cp` command, it takes two arguments - the name of the file or directory to move or rename, and the name of the file or directory to move it or rename it to.

```bash
mv file1.txt file2.txt  # Move the contents of file1.txt to file2.txt. This
                        # effectively just renames file1.txt to file2.txt.
mv dir1 dir2  # Renames dir1 to dir2 if dir2 doesn't exit, and otherwise
              # moves dir1 into dir2.
```

**Note**: `mv` will overwrite files if they already exist. If `file2.txt` had
already existed in the above, then it would have been overwritten with the
contents of `file1.txt`.

## Keyboard Shortcuts

Becoming efficient at navigating around your terminal can save you loads of
time. Below, we'll walk through some commands that can help increase your
efficiency right from the command line.

### Using The Up/Down/Right/Left Arrows and Tab

* To revisit commands from your history, you can typically press the up arrow, where pressing it multiple times allows you to cycle through all your previous commands. You can also use your down arrow to cycle through commands, too.

* To navigate single characters in a line, you can typically use your left
and right arrows. Holding down your META key (typically `alt` on mac; try `alt` or `ctrl` on Windows) will allow you to navigate through whole words at a time.

* Tab completion is a thing in most unix shells. What this means is that
you can type the beginning couple of letters of a file or directory and
hit tab to complete it (so long as the file/directory name is unique,
otherwise it will complete up to the point that it can).

### Control-key Commands

Note here that `^h` is the same as `ctrl-h` on a mac, and the equivalent
on a Windows system (try `ctrl` or `alt`).  

```bash
^u # Erases input from current location to beginning of line.
^k # Erases input from the current location to the end of the line.
^a # Jump to beginning of line.
^e # Jump to end of line.  
^z # Suspend a program that may be running and gives you another shell prompt.
^c # Kill a program that may be running.
^l # Clear the entire screen (works like typing 'clear' ).
```
