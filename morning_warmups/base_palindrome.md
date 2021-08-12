## Python Algorithm

Write a function that takes a number in base 10 and finds the smallest base, 2 or greater, in which that number is a palindrome.

For example:

```python
palindrome_base(52)         # Should return 3 as 52 base 3 is 1221
palindrome_base(1933401)    # Should return 35
```

In case you don't know the algorithm to change from base 10 into another here it is:

1. Divide the number by the new base.
2. The remainder from this operation is the next number in the new base.
3. Take the quotient from the operation and make it the next one you divide by. Repeat from step 1.
4. When the quotient is smaller than the base you it is the last number in the new base.
