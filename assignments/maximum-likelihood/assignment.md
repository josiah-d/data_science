# Maximum Likelihood

## Introduction

In this exercise we're going to explore the concept of maximum likelihood estimation (MLE).

Maximum likelihood estimation is the gold standard methodology for estimating some true parameter from a data set.  For example:

  - We have a coin of unknown fairness, and we want to flip the coin a bunch of times and use the results to figure out the fairness of the coin (first example).
  - We have a chunk of matter that is undergoing radioactive decay (the atoms in the material spontaneously self-destruct at some rate), and we would like to figure out the rate of decay (second example).
  
We will start by using MLE to figure choose between a finite number of possibilities (the truth is one of these ten things, which one of the possibilities is most likely), and will then generalize the method to choosing between an infinite number of possibilities.

## Basic

### Part 1: Coin Flips

Let's start with the most mundane (but instructive) example, *flipping coins*!

1\. Write a function `flip_coin` that returns an array of zeros and ones representing a sequence of `n` flips of a coin of fairness `p`.

```python
def flip_coin(n, p) -> np.array:
    """Flip a coin of fairness p, n times.
    
    Parameters
    ----------
    n: int
      The number of times to flip the coin.

    p: float, between zero and one.
      The probability the coin flips heads.

    Returns
    -------
    flips: np.array of ints
      The results of the coin flips, where 0 is a tail and 1 is a head.
    """
    pass
```

The likelihood function is a measure of how reasonable a given value of `p` is given some observed data.  It is defined as the probability of observing sequence of coin flips <img src="https://render.githubusercontent.com/render/math?math=\{f_1, f_2, \ldots, f_k\}">, given some value of `p`:

<p align=center>
<img src="images/likelihood-definition.png" alt="Definition of Likelihood Function">
</p>

Since we're doing coin flips, the probabilities in question are:

<p align=center>
<img src="images/p-coin-flip-definition.png" alt="Definition of Coin Flip Probabilities">
</p>

2\. Write a function `coin_log_likelihood` that returns the *logarithm* of the likelihood of `p` given a sequence of coin flips.

```python
def coin_log_likelihood(p, flips):
    """Return the log-likelihood of a parameter p given a sequence of coin flips.
    """
```

Let's suppose we flip a coin from a bag of coins of unknown origin ten times, and we get the following results:

```
H, T, T, T, H, H, T, T, T, T
```

3\. Create a numpy array `flip_data` representing this sequence of coin flips.

4\. Suppose the are *two* coins in the bag, and we are provided with the knowledge that:

<p align=center>
<img src="images/coin-ps.png" alt="Coin Flip Probabilities">
</p>

Use your function to compute the *log-likelihood* of each of these coins given the sequence of coin flips.  Which coin is more likely the one you chose and flipped?  Does this align with your intuition?

5\. Make a bar chart of these two log-likelihoods.  Here's how the resulting chart should look.

<p align=center>
<img src="images/two-coin-likelihood.png" alt="Example of Two Coin Likelihood Function">
</p>

Note that since probabilities are less than one, the log-likelihood is always *negative*, so the bars extending downwards, while weird, is correct.

6\. Wrap your plotting code in a function so that you can continue to use it.

```python
def plot_coin_likelihood(ax, ps, data):
```

7\. Make a plot of the likelihood for each *truncated* sequence of flips.  That is:

```
First plot for: H
Second plot for: H, T
Third plot for: H, T, T
Fourth plot for: H, T, T, T,
...
Tenth plot for: H, T, T, T, H, H, T, T, T, T
```

You'll find the function you wrote earlier useful.  The result should look like:

<p align=center>
<img src="images/two-coin-likelihoods.png" alt="Example of Two Coin Likelihood Functions">
</p>

8\. Spend some time discussing how the likelihood of each possibility evolves as we flip the coin more and more.  Does the evolution make sense to you?

9\. Repeat the experiment for a wider set of possible probabilities:
    
```python
probabilities = np.linspace(0, 1, num=11)
```

Now let's generalize the above ideas to an *infinite* set of probabilities, i.e. let's find the maximum likelihood out of *all* the possible probabilities:

```
0 < p < 1
```

10\. Write a function `plot_coin_likelihood_continuous` that is much like your previous `plot_coin_likelihood` function, but draws a **line** plot (i.e. the graph of a function) over the entire range of probabilities.  You won't need to pass in an array of probabilities to this one:

```python
def plot_coin_likelihood_continuous(ax, data):
```

11\. Use your function to plot like likelihood function for the full sequence of flips.  You result should look something like this:

<p align=center>
<img src="images/coin-likelihood-continuous.png" alt="Likelihood For Full Sequence of Coin Flips">
</p>

This plot is the graph on the **log-likelihood function** for the coin flipping experiment.  The **principle of maximum likelihood** states that the best estimate of the true fairness of the coin in the **maximum** of this function.

12\. Write a function `maximum_coin_likelihood` that computes the maximum likelihood estimate of the coin fairness.  You'll need to use the `np.argmax` function (check out the numpy documentation to see what it does).

13\. Compute the maximum likelihood estimate of `p` for this sequence of coin flips.  Re-draw your plot of the likelihood function from before, but superimpose a vertical line at the maximum likelihood estimate.

14\. Make a plot of the complete likelihood function for each truncated sequence of coin flips, and superimpose the vertical line at the maximum likelihood estimate.

15\. Can you spot a pattern in the results for the various maximum likelihood estimates?  Do you have any conjectures for (a formula for) the maximum likelihood estimate of `p` in this situation?

∞\. **Wicked Bonus**: Prove your conjecture.

## Advanced

### Part 2: Poisson Rate Estimation

In this example we will give another example of maximum likelihood estimation, this time using data from a real life experiment (and an important one at that!).

In 1919 [Ernest Rutherford](https://en.wikipedia.org/wiki/Ernest_Rutherford) completed an important experiment on the radioactive decay of atoms.  In radioactive decay (actually a particular type of radioactive decay called α-decay), a (more or less) inert chunk of matter spontaneously emits an α-particle.  It's impossible to predict exactly when this decay will happen, but the process does have some regularities.  It is the structure of these regularities that was discovered by Rutherford in this experiment.

Rutherford observed a chunk of [radium](https://en.wikipedia.org/wiki/Radium) of a fixed and well measured mass for a fixed amount of time and then counted how many radioactive events he observed over that span of time.  He then repeated this experiment 2612 times, each time taking record of how many events he observed.

<p align=center>
<img src="images/rutherford-paper.png" alt="Image of Rutherford's Paper">
</p>

The following numpy array contains Rutherford's data.

```python
alpha_particle_counts = np.array([
    57, 203, 383, 525, 532, 408, 273, 139, 49, 27, 10, 4, 2, 0])
```

For example, there were 57 periods of time where no event was observed, 203 periods where exactly one was observed, 383 where exactly two, and so on.

1\. Make a histogram of Rutherford's data.  You should have one bar for each observed count (using `ax.hist` will almost certainly do the wrong thing here, so you should manually construct a bar chart).

2\. Do you have any conjectures for the distribution of this data.  Keep in mind that it is descrete data describing a count.

The Poisson distribution is the most well know distribution used to describe count data.

You can play around with the Poisson distribution by importing `scipy.stats.poisson`.  It has one parameter λ that describes the rate of occurrences of an event.

3\. The log-likelihood function of the Poisson distribution is

<p align=center>
<img src="images/poisson-log-likelihood.png" alt="Log-Likelihood of Poisson Distribution">
</p>

Where `k_i` are the observed counts in our data, `N` is the number of data points we have observed, and the constant does not depend of the parameter λ.  

Plot the log likelihood function of Rutherford's data for a grid of λ's in the range `[0, 12]` (you can assume the constant is zero, doing otherwise just moves the graph up and down).

4\. Calculate the maximum likelihood estimate of the rate of alpha decay λ from Rutherford's experiment.  Superimpose a vertical line at the maximum likelihood estimate of λ.

5\. Make note of what we just did: we fit a **distribution** to Rutherford's data.  To check the goodness of fit, we can plot both the fit distribution (a Poisson in this case) and the original data on the same plot.

Here's an example with some simulated data:

<p align=center>
<img src="images/simulated-data-and-model.png" alt="Poisson Fit with Simulated Data">
</p>

6\. The **law of small numbers** (non-canonical, yet clever, name) states that binomial distribution with a very large `N` and a very small `p` are very well approximated by Poisson distributions.

Given that a chunk of Radon is made of a very large number of individual Radon atoms, does the Law of Small Numbers explain your results in this section?

Reference: [Caltech Lesson on the Law Small Numbers](http://www.math.caltech.edu/~2016-17/2term/ma003/Notes/Lecture12.pdf)
