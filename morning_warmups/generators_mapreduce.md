This warmup goes over python concepts that are important for understanding Map Reduce.

## 1. Python generators

1. Using generators, implement a prime number sequence.  I should be able to do the following (indefinitely):

    ```python
    In [10]: next(g)
    Out[10]: 2
    
    In [11]: next(g)
    Out[11]: 3
    
    In [12]: next(g)
    Out[12]: 5
    
    In [13]: next(g)
    Out[13]: 7
    
    In [14]: next(g)
    Out[14]: 11
    
    In [15]: next(g)
    Out[15]: 13
    
    ...
    ```

    For reference, here's a generator which gets all the numbers that have a 5 in them (as any digit).
    
    ```python
    def five_generator():
        i = 0
        while True:
            if '5' in str(i):
                yield i
            i += 1
    ```
    
    Each time you use the `next` method, the function will continue until it gets to the next yield statement and return that value.


## 2. Map and Reduce

It's generally not very pythonic to use the `map` and `reduce` functions. In standard python, we would use list comprehensions. However, when our data gets big, these will be important! So let's practice using them.

1. Using map, write some code which gets the first character of every word in a phrase:

    So if you start with `San Francisco is fun!` you should get `['S', 'F', 'I', 'F']`.
    
    Now write a function which creates the acronym. e.g. for the above example it should be `SFIF`. Use your above code as well as the `reduce` function. Don't use the `join` method.
    
    ```python
    In [11]: acronym('San Francisco is fun!')
    Out[11]: 'SFIF'
    ```
