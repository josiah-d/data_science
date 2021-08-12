## 1. Create a Random Variable

Say you're giving a probability mass function in the form of a dictionary like this:

```python
{'A': 0.5, 'B': 0.1, 'C': 0.4}
```

I would like to get a random variable which is `A` 50% of the time, `B` 10% of the time and `C` 40% of the time. Write a function to do this. The only random function you can use is a uniform random distribution (use the `random` function from the `random` module).

In ipython, type `from random import random` to get the function and type `random?` to see what it does.

Now complete this function:

```python
def random_variable(pmf):
    '''
    INPUT: dictionary
    OUTPUT: one of the keys of the dictionary

    Return one of the keys of the dictionary according to the given probabilities. You may assume the probabilities sum to 1.
    '''
```

Test that your code works correctly with the following code:

```python
from collections import Counter
results = Counter()
n_obs = 10000
for i in range(n_obs):
    results[random_variable({'A': 0.5, 'B': 0.1, 'C': 0.4})] += 1
for outcome, count in results.items():
    print(outcome, count / n_obs)
```

## 2. Python modules

Say you have a file called `src.py` with these contents:

```python
def print_hello(name):
    print(f"Hello, {name}!")

print_hello("Jeff")
```

1. Before actually creating this file and running any code, determine what you think will happen if you run the following code in the command line.

    ```python
    from src import print_hello
    print_hello("Tammy")
    ```

2. Create the `src.py` file and run the above code. Is this what you expected?

3. Modify the `src.py` so that you only get one "Hello" from running the above code. Make sure that if I run `python src.py` on the command line I will still get the same result as before!
