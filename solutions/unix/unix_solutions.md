## Examing the file

* What do the beginning and end of the file look like?

```bash
head file
tail file
```

* Examine the first couple of pages of the file.

```bash
less file
```

* Advanced: if you want to look at just the lines 636100 to 636120 how would you do it?

```bash
cat file | sed -n '636100,636120 p'
```

## Exploratory analysis

* The tag `<contributor>` identifies a contributor. How many are there?

```bash
cat file | fgrep '<contributor>' | wc -l
```

* How many contributors are identified by the tag username?

```bash
cat file | fgrep '<username>' | wc -l
```

* Who are the most common contributors by username?

```bash
cat file | sed -n '/<username>/p' | sed -E 's/<username>|<\/username>//g' | sort | uniq -c | sort -rn | head
```

* How many are bots?

```bash
cat file | sed -n '/<username>/p' | sed -E 's/<username>|<\/username>//g' | sort | uniq | fgrep -E '[B|b][O|o][T|t]' | wc -l
```

* Advanced:   What are the other contributors -- i.e., those entries which have a `<contributor>` tag but not a nested `<username>` tag?  Hint: use `sed` or `perl`.  How many of these contributors are there?  Do they explain all of the missing contributors?

```bash
# Something like this gets all the contributor tags and puts
# them on one line each

cat enwiki-latest-pages-articles1.xml-p000000010p000030302 | sed -n '/<contributor>/,/<\/contributor>/p' | awk 'BEGIN {ORS=""} /<\/contributor>/ {ORS="\n"; print $0} !/<\/contributor>/ {ORS="" ; print $0} END {print "\n"}'

# Then you can see which don't have <username> tags by piping this to a grep command

... | fgrep -E -v '<username>'

# and use

... | wc -l

# to see that the number of contributors <username> + the
# number with <ip> adds up to the total number
```
