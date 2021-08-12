## Warmup: Parentheses

**Include your code and answers in** `parentheses.py`.

You are tasked with determining whether a string of parenthesis is correctly balanced.  Write a function that takes as input a single string that may contain any ASCII character and determines at that moment whether or not the associated parenthesis (`[`, `]`, `(`, `)`,`{`,`}`) are correctly closed.  Return true or false accordingly.

**Bonus**

See if you can make it handle quotation marks (single and double) in the same way. This might be tricky because quotation marks don't have a left and right, so you might not be able to match them in the same way.

__All open parenthesis should be closed in the same order that they were opened__

So ")Text(" should return false, even thought it has the correct number of left and right parenthesis, because they are not opened and closed in the correct order


You can use the following print statements to check your work:

```
    print(f'''{check_parens('(a(b))()()')} should be True''')
    print(f'''{check_parens('a(b())')} should be True''' ) 
    print(f'''{check_parens(')a(b))')} should be False''' )
    print(f'''{check_parens('(a(b){c}')} should be False ''') 
    print(f'''{check_parens('(a(b)c})')} should be False ''' ) 
    print(f'''{check_parens('[(a(b){c})]')} should be True''' ) 
    print(f'''{check_parens('(a(b)]{c}')} should be False''')
    print(f'''{check_parens(')b(')} should be False''' )
    print(f'''{check_parens('(a[b)c]')} should be False''' ) 
```


### Bonus Tests

```
    text_1 = '''("A",['b']) '''

    print(f'''{check_parens(text_1)} should be True''')

    text_2 = '''('A",["b']) '''

    print(f'''{check_parens(text_2)} should be False''')
```