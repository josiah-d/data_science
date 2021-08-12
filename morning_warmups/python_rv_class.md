## Warmup: Random Variable Class

Let's create a random variable class!  

1. Create a Random Variable class (`RandomVariable`) that represents a distribution of a possible set of outcomes. 
   It should have the following methods:
   
   - `sample()`: Makes a draw from the random variable and return an outcome.
     The various outcomes are drawn with the appropriate probabilities, and
     draws should be independent.
   - `all_outcomes()`: Return a set of all the possible outcomes.
   - `pmf(t)`: Evaluate the probability mass function of the random varaible at an outcome `t`.

2. The `RandomVariable` class should be instantiated with a dictionary mapping
the outcomes to thier probabilities. 

```python
from my_stats import PMF

die = {"1": 1/6, "2": 1/6, "3": 1/6, "4": 1/6, "5": 1/6, "6": 1/6 }

die_rv = RandomVariable(die)

# Your sequence of draws witl vary!
die_rv.sample() #=> "3"
die_rv.sample() #=> "2"
die_rv.sample() #=> "6"
die_rv.sample() #=> "3"

die_rv.all_outcomes() #=> {"1", "2", "3", "4", "5", "6"}

die_rv.pmf(2) #=> 0.16666666666666666
```
