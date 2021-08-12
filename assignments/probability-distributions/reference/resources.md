## Quick Review of Distributions

The following is a short review of common distributions and their parameters.


```
Discrete:

    - Bernoulli
        * One instance of a success or failure in a trial with a fixed probability of success.
	* Parameters: p, probability of success in a trial.

    - Binomial
        * Number of successes out of a known number of trials, each with a fixed probability of success.
	* Parameters: p, probability of success, n, number of trials.

    - Poisson
        * Count of the number of events occuring in a fixed interval of time (or volume of space), where each event occurs at a fixed rate.
        * Parameters: lambda: rate of event occurance.

    - Geometric
        * Number of trials until the first success in a (potentially infinite) sequence of bernoulli trials.
	* Parameters: p, probability of success in a trial.

Continuous:

    - Exponential
        * Time (or space) between two subsequent poisson distributed events.
	* Parameters: lambda: rate of event occurance.

    - Uniform
        * All values are equally likely.
        * Parameters: a, b: endpoints of interval supporting the distribution.

    - Gaussian a.k.a Normal
        * Distribution shaped like a bell curve with very quickly decaying tails.  Commonly occuring due to the Central Limit Theorem.
	* Parameters: mu, expectation, sigma, standard deviation.

```

# Resources

There's a lot in today's material, but it's far from comprehensive.  
Here is a cheat sheet to assist with some core parts of today's lecture:

* [A smaller cheatsheet](http://www.cs.elte.hu/~mesti/valszam/kepletek.pdf)

And here's a great statistics book:

* [All of Statistics](https://www.springer.com/us/book/9780387402727)
