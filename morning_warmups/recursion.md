# Recursion

A recursive function is a function that calls itself. For example, 

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

This returns the [factorial](https://en.wikipedia.org/wiki/Factorial) of a number n, also written as n!, which is the 
product of all integers up to and including n (that is, 1*2*3*...*n).

0! = 1 by definition.

Every recursive function has:
- a _recursive step_ where the function itself is called
- a _base case_, a stopping point, where the function returns a value without calling itself

## Exercise: write the following functions recursively

- `fibonacci(n)`, which take an integer n and returns the 
nth value of the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number): 
    - F(1) = 0, F(2) = 1, and F(n) = F(n-1) + F(n-2)
- `sum_digits(n)`, which takes an integer n and 
returns the sum of the digits of n 
    - for example `sum_digits(4502)` should return 11, since
that's 4+5+0+2
- `recursive_sum(lst)`, which takes a list of numbers and returns their sum
- `recursive_max(lst)`, which takes a list of numbers and returns the maximum value
