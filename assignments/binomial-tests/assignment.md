# Binomial Tests

## Introduction

In this assignment, we will explore the simplest kind of statistical test, tests where the distribution of data under a null hypothesis is binomial.  More sophisticated tests, like the z-tests (which use the normal distribution) and the t-tests (which use a generalization of the normal distribution called the t-distribution) can be viewed as elaborations on the themes set down here.

## Basic

### Part 1: Binomially Distributed Data

Recall the binomial distribution describes data generated when we observe a binary outcome (one of two things can happen) a fixed number of times, and the probability that one or another thing happens for each individual outcome does not change.

In each of the following situations, the resulting data *may be* binomially distributed.

  - If it is binomially distributed, give the parameters of the binomial distribution.
  - If it is not binomially distributed, describe why not.  If you can, give the correct distribution (if not, don't worry too much about it).

1. A large bucket contains 1256 six sided dice.  You dump all of them onto the ground (without losing any) and count how many 4's you see.

2. A large bucket contains 1256 dice with varying numbers of sides (some have four sides, some have six, some have 8, some have 10, some have 12, and some have 20).  You dump them all onto the ground (without losing any) and count how many 4's you see.

3.  A magic the gathering deck (like a deck of cards) is made up of two types of cards: lands, and playables.  You have a forty card deck that contains the typical 17 lands.  You shuffle your deck, then draw the top card and see if it is a land.  You repeat this process 100 times, and count how often there is a land on top.

4.  A magic the gathering deck is made up of two types of cards: lands, and playables.  You have a forty card deck that contains the typical 17 lands.  You shuffle your deck, draw a hand of 7 cards, and count the number of lands.

#### The following two I'm gonna tell you up front: these ARE binomially distributed!  Convince yourself this is true, and compute the appropriate values of the parameters.

5. A large bucket contains 1256 six sided dice.  You dump all of them onto the ground, but this time you lose a random number of dice; there is a 10% chance you will lose any individual die.  You, again, count the number of 4's. 

6.  A magic the gathering deck is made up of two types of cards: lands, and playables.  Although 17 lands is typical in a 40 card deck, it is sometimes correct to play 16 or 18 lands.  Say when you construct a deck, 80% of them contain 17 lands, 10% contain 16, and 10% contain 18.  You build a magic the gathering deck, shuffle it, and then look at the top card and see if it is a land.  You then repeat this process 100 times (including rebuilding the deck), and count how many times there was a land on top.


### Part 2: Binomial Hypothesis Tests

In each of the following situations, a decision can be made by using a hypothesis test based on the binomial distribution.  For each scenario:

  - State the null and alternate hypothesis.
  - State the distribution of the count under the null hypothesis (which, in every scenario, is a binomial distribution).
  - Plot the null binomial distribution, and shade the region to the right of the count you actually observed.
  - Calculate the p-value associated with the stated null and alternate hypothesis.
  - Decide whether to reject the null hypothesis.

1. Muriel still insists she can tell if you poured milk into tea before or after the hot water.  To prove her point, she goes to goodwill and purchases ALL of their mugs, 137 in total.  It take all day, but you manage to randomly make cups of tea milk or water first in all the mugs, without telling her how many there are of each, and test her on all of them.  She gets 72 correct.  Do you believe her now?

2. You are working on your heelflips (a skateboarding trick).  Your goal is to land them more than 50% of the time (as in, the true rate you land them is over one half.  Of course, in any given sample, you may learn more or less than that ideal).   You attempt 122 heelflips in a day, and land 72 of them.  Do you believe you are as good as you want to be?

3. Buses are seemingly always late, like 90% of them.  Thoroughly dismayed with the state of public transportation, you spend all day collecting data and being just generally upset.  Out of 53 total bus arrivals in a given day at your local bus stop, 49 of them were late.  Is the situation really that bad, 90% of them?

4. You'd like to think that you are improving at programming, but most of your programs don't run at first.  Your instructors insist that this is normal, but it's discouraging, so you would like to have some measure of improvement.  At the beginning, none of your programs ran the first time, but this week you wrote 6 programs, and one of them ran the first time!  Can you confidently clam that more than 5% of your programs run the first time, you'd feel pretty good about that.

## Advanced

## Part 3: Varying the Sample Size

In this final section, we will see how one of the examples above changes as we vary the sample size.

1. Let's suppose that Muriel finds more (or less) mugs at the goodwill.  Write a function to encapsulate your work in problem 1 above.  It should take as parameters the number of mugs, and the number she got correct, and return a p-value under the null hypothesis that she is guessing randomly.

    ```python
    def binomial_test(n_mugs, n_correct, p_null=0.5):
    ```

2. Use your function to replicate your conclusion from above.

3. Suppose the *truth* is that Muriel gets 52% of the mugs correct.  Vary the number of mugs total between 1 and 250, and in each case assume that the number Muriel gets correct is `0.52 * n_mugs` (which isn't an integer, but do something sensible to make it one).  Plot the p-value of a binomial test on this data as the number of mugs used varies.

4. How many mugs would we need to achieve a p-value of `< 0.2`, of `< 0.1`, of `< 0.05`?
