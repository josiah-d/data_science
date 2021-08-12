## Basic

The following steps will create the directory structures.

```
# go to the directory where you want to put the `lax_dsi` folder in.
mkdir dsi_lax3
cd dsi_lax3

# assignments directory
mkdir assignments
touch assignments/readme.md
mkdir assignments/unix
touch assignments/unix/unix_sol.md

# capstones directory
mkdir capstones
mkdir capstones/capstone1
mkdir capstones/capstone2
mkdir capstones/capstone3
touch capstones/readme.md

# lectures directory
mkdir lectures
touch lectures/readme.md

# resources directory
mkdir resources
touch resources/readme.md

# requirements.txt
touch requirements.txt
```

## Intermediate

1.
```
cd unix/data/
```
2.
```
less 2015_sp100.csv
```
3.
```
grep GOOG 2015_sp100.csv > 2015_goog.csv
```
4.
```
sort 2015_goog.csv > 2015_goog_sorted.csv
```
5.
```
python3 plot_stock_prices.py < 2015_goog_sorted.csv
```
6.
```
grep GOOG 2015_sp100.csv | sort | python3 plot_stock_prices.py
```

Check the `plot_stock_prices.py` file and learn how to read standard input in Python.

## Advanced

### **Getting started**

1.
wget download resources through internet. Yes, you can do the same with `curl`. For usage, check this [link](http://www.compciv.org/recipes/cli/downloading-with-curl/).

2.
Google. And you will find something like this link [Linux/Unix: How To Extract and Decompress a .bz2/.tbz2 File](https://www.cyberciti.biz/faq/linuxunix-how-to-extract-and-decompress-a-bz2-tbz2-file/)
```
bunzip2 -d enwiki-latest-pages-articles1.xml-p1p41242.bz2
```

3.
Check size
```
ls -althr
```
```
-rw-r--r-- 1 ubuntu ubuntu 845M Sep 21 14:34 enwiki-latest-pages-articles1.xml-p1p41242
```
Check number of lines
```
wc -l enwiki-latest-pages-articles1.xml-p1p41242
```
Depends on the actual file you use, the result may be different.
```
6296752 enwiki-latest-pages-articles1.xml-p1p41242
```
It is an [xml](https://en.wikipedia.org/wiki/XML#:~:text=Extensible%20Markup%20Language%20(XML)%20is,free%20open%20standards%E2%80%94define%20XML.) file.

4. No


### **Examining the file**

5.
```bash
head enwiki-latest-pages-articles1.xml-p1p41242
tail enwiki-latest-pages-articles1.xml-p1p41242
```

6. Answers may vary. You can say it looks like an html file with nested tags, etc.

* Examine the first couple of pages of the file.

7.

```
head -n 636120 enwiki-latest-pages-articles1.xml-p1p41242| tail -n 20
```

### **Exploratory analysis**


8.
`27448`
```bash
cat enwiki-latest-pages-articles1.xml-p1p41242 | grep -n '<contributor>' | wc -l
```

9.

`24272`

```bash
 cat enwiki-latest-pages-articles1.xml-p1p41242 | grep -n '<username>' | wc -l
```

10.

Google. You will find links like this [Sort and count number of occurrence of lines](https://unix.stackexchange.com/questions/170043/sort-and-count-number-of-occurrence-of-lines).

You may also need to understand the `-r` and `-n` options of `sort` command. `man sort` is your friend.

```bash
cat enwiki-latest-pages-articles1.xml-p1p41242 | grep '<username>' | sort | uniq -c | sort -rn | head
```
Think about that why we need two `sorts`. Try to decompose each step in the pipes to understand what's going on.

```
   1329         <username>Tom.Reding</username>
    929         <username>Citation bot</username>
    441         <username>MZMcBride</username>
    423         <username>1234qwer1234qwer4</username>
    421         <username>Graham87</username>
    333         <username>InternetArchiveBot</username>
    314         <username>FrescoBot</username>
    262         <username>ClueBot NG</username>
    212         <username>Xqbot</username>
    196         <username>AnomieBOT</username>
```
11.
`73`
```bash
cat enwiki-latest-pages-articles1.xml-p1p41242 | grep '<username>' | sort | uniq -c | sort -rn | grep -E '[B|b][O|o][T|t]' | wc -l
```