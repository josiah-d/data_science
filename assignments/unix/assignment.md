# Unix

## Introduction

In this exercise, you will learn how to use Unix commands to perform exploratory data analysis (EDA) from the command line.  This is an invaluable skill which will help you find problems in data sets and clean data more quickly.  Often, with a little cleverness, you can answer questions about your data without needing to resort to `Python`, `R`, and other heavier tools.

Unix is particularly adroit at handling text files because there are many commands which can operate on this format.  By extension, CSV files are also easy to manipulate.

## Basic

### Part 1: Set up a directory for DSI

> This is your first basic assignment. A basic assignment can usually be done individually in a quick fashion.

In this assignment. Create the following directory structure for the DSI program in the commandline. Your solution to this assignment will be put in the `/dsi_lax3/assignments/unix/unix_sol.md` file. Keeping a consistent and organized file structure is beneficial in the long run.

#### Clone a git repo

For example, you can clone the `lectures` directory by the following command. Make sure you only `clone` it, rather than `fork` it.

```shell
git clone https://github.com/GalvanizeDataScience/lectures
cd lectures # now you are in the lectures folder.
```

If you have limited disk space, like running linux on a virtual machine, you can refer to this [link](https://github.com/GalvanizeDataScience/lectures/blob/main/README.md) to only clone contents of depth level 1.


```shell
└── dsi_galvanize
    ├── assignments
    │   ├── readme.md
    │   └── unix
    │       └── unix_sol.md
    ├── capstones
    │   ├── capstone1
    │   ├── capstone2
    │   ├── capstone3
    │   └── readme.md
    ├── lectures
    │   └── readme.md
    ├── requirements.txt
    └── resources
        └── readme.md

```

## Advanced

### Part 2: Introduction to Unix Command Line Interface

> This is your first advanced assignment. An advanced assignment combines various skills you learned in the lecture and usually requires some thinking. Feel free to discuss with your classmates or DSR to solve the problems.

> You will be using some new commands in the steps below. Read the manual for these new commands: `less`, `grep`, and `sort`. You can access the manual using the `man` command. E.g. run `man less` to read the manual for the `less` command. (Tip: To exit `man`, press 'q' on your keyboard.)


1.  Use `cd` to navigate into the `unix/data/` sub-directory. You should see two files: `2015_sp100.csv` and `plot_stock_prices.py`.

2.  Use `less` to peek at the file (`2015_sp100.csv`). It contains daily stock prices for stocks in the [S&P 100 Index](https://en.wikipedia.org/wiki/S%26P_100) for the year 2015. Notice the lines of the file are in random order.

3.  Use `grep` to print all the lines having prices for Google (symbol: GOOG). Use *bash file redirection* to store these GOOG lines into a file named `2015_goog.csv`.

4.  Use `sort` to sort the lines in `2015_goog.csv`. Use *bash file redirection* to store the sorted lines into a new file named `2015_goog_sorted.csv`.

5. The Python script `plot_stock_prices.py` knows how to plot stock price data files. Run that script, and use *bash file redirection* to input the file `2015_goog_sorted.csv` into the script's *stdin*.

6. Combine steps 3, 4, and 5 above into one command using *bash pipes*.

## Extra Credit

> This is your first `extra credit` assignment. In `extra credit` assignment, you are expected to use a lot of googling, trying-and-error. You will meet tasks that you may not know how to do it in the first place. Please do not feel frustrated but feel excited. **You are not expected to solve the extra-credit problem during the assignment time slot of the day.**

> Most questions you meet as a data scientist will be fresh and new. Treat instructors and DSR as senior data scientist and try to communicate with them to help you overcome the diffculties.

###  Part 3: Wikipedia data


Let's analyze some Wikipedia data using Unix tools.  But first some advice:  you will be working with a large file, so commands will take a while to run.  Consequently, test your scripts and commands on a small subset of the file so that you can get them working quickly.  When you working in an environment, like `bash` or regular expressions, where debugging tools are scarce, you should build up your code in small steps, testing each step along the way.  Document anything clever to make future maintenance easier.


#### Getting started

Start by downloading the data using the command line. If the linked file was removed by Wikimedia. Go to [Wikimedia dump page](https://dumps.wikimedia.org/enwiki/latest/) and download one file with name pattern `https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles1.xml-****.bz2`. The rest of the exercise remains the same.

```bash
wget https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles1.xml-p1p41242.bz2
```


1.  What does the `wget` command do?  Could you also use `curl`?
2.  What type of file is `enwiki-latest-pages-articles1.xml-****.bz2`?  How can you figure out the a file's type? Often files come in different (compressed) archive formats. `tar` and `gzip` are common.  Unpack the file.
3.   How big is it?  How many lines does it have?  What type of file is the uncompressed version of the file?
4.  Would it be a good idea to load this file into an editor?


#### Examining the file

Loading large files into an editor is a bad idea because it is time consuming and can crash your editor if you run out of memory.  Fortunately, Unix provides tools which work on arbitrarily large text files, including CSV.

5.  What do the beginning and end of the file look like?  What commands did you use?
6.   Examine the first couple pages of the file.  What do you notice about the structure?
7.   Optional:   if you want to look at just lines 636100 to 636120 how would you do it?  (Hint: use `head` and `tail` and the option `-n`.)


#### Exploratory analysis

Let's answer some basic questions about contributors.

8.   The tag `<contributor>` ... `</contributor>` identifies a contributor.  How many are there?
9.  How many users are identified by the tag `<username>`?
10.   Who are the most common contributors by username? Hint: you will need to connect several commands via pipes. You may need `uniq -c` to do the counting.
11.   How many unique bots are there? You can think the following regular expression matches a bot. Hint: Use `grep -E` instead of `grep`. What does it do?
```
'[B|b][O|o][T|t]'
```
