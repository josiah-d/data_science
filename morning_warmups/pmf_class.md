## Discrete Probability Class

You are going to build a class that represents discrete probability distributions.

1. Create a module called `my_stats`.

2. Write a generic `PMF` class, that represents a probability mass function. It will need to store:
  * values
  * associated probabilities

3. Initialize each PMF with a dictionary representing a mapping from value => probability. If the PMF is initialized without an argument use a reasonable default value.

4. You should allow querying of your PMF by value and return a probability. Write a `prob()` method that takes an input value as an argument, and returns the probability of getting that value.

5. Also allow for the case of updating a value after a PMF object has already been created. Create a `set()` method on your class that takes a key => value pair to update.

6. The last thing your PMF class should do is print its distribution. Create a method `print_pmf()` that outputs the distribution as a list of tuples.

**Note: The PMF should always be normalized, i.e. the sum of the probabilities should be 1.**

### Example Class Usage

```python
from my_stats import PMF

die = PMF({"1": 1./6, "2": 1./6, "3": 1./6, "4": 1./6, "5": 1./6, "6": 1./6 })

die.prob("3") #=> 0.166

die.print_pmf() #=> [("1", 0.166), ("2", 0.166), ("3", 0.166), ("4", 0.166), ("5", 0.166), ("6", 0.166)]

# weight the die, be sure to renormalize, so that the probability of the updated side
# and the probabilties of all the other sides sum to 1
die.set(("2", 1/2))

die.print_pmf() #=> [("1", 0.1), ("2", 0.5), ("3", 0.1), ("4", 0.1), ("5", 0.1), ("6", 0.1)]
```

