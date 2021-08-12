A box contains a 4-sided die, a 6-sided die, an 8-sided die,
a 12-sided die, and a 20-sided die. A die is selected at random, and the
rest are destroyed.

We would like to determine which die I have selected, given only information of what I roll.

1. What is the prior?

    *You should use a uniform prior. Each of the five dice has a 20% chance of being picked.*

2. What is the likelihood function? You should assume that the dice are fair dice.

    ```
    likelihood(data|die) = 0      if data > die
                           1/die  if data <= die
    ```

    *Here `die` is the max value of the die (4, 6, 8, 12 or 20). The data is what was rolled. Note that there is no way to roll a number higher than the value of the die. If the value is possible, all values are equally likely, so it depends on the size of the die.*

3. Say I roll an 8. After one bayesian update, what is the probability that I chose each of the dice?

    ```
    likelihood(8|4)  = 0
    likelihood(8|6)  = 0
    likelihood(8|8)  = 1/8
    likelihood(8|12) = 1/12
    likelihood(8|20) = 1/20
    ```

    ```
    P(8) = 1/5*0 + 1/5*0 + 1/5*1/8 + 1/5*1/12 + 1/5*1/20
         = 31/600
         = 0.0517
    ```

    ```
    posterior(4)  =    1/5*0 / P(8) = 0
    posterior(6)  =    1/5*0 / P(8) = 0
    posterior(8)  =  1/5*1/8 / P(8) = 15/31 = 0.484
    posterior(12) = 1/5*1/12 / P(8) = 10/31 = 0.323
    posterior(20) = 1/5*1/20 / P(8) =  6/31 = 0.194
    ```

4. Comment on the difference in the posteriors if I had rolled the die 50 times instead of 1.

    *The posterior would be a lot more certain. Depending on what you rolled, one of the values would be a lot larger than the others would be 0 or close to 0.*

5. Which one of these two sets of data gives you a more certain posterior and why?
`[1, 1, 1, 3, 1, 2]` or `[10, 10, 10, 10, 8, 8]`

    *The second one would give you a more certain posterior since the first two dice are eliminated as possibilities.*

6. Say that I modify my prior by my belief that bigger dice are more likely to be drawn from the box. This is my prior distribution:

    ```
    4-sided die: 8%
    6-sided die: 12%
    8-sided die: 16%
    12-sided die: 24%
    20-sided die: 40%
    ```

    What are my posteriors for each die after rolling the 8?

    First need to recalculate the probability of rolling an 8:

    ```
    P(8) = 0.08*0 + 0.12*0 + 0.16*1/8 + 0.24*1/12 + 0.40*1/20
         = 3/50
         = 0.06
    ```

    ```
    posterior(4)  =    0.08*0 / P(8) = 0
    posterior(6)  =    0.12*0 / P(8) = 0
    posterior(8)  =  0.16*1/8 / P(8) = 1/3 = 0.333
    posterior(12) = 0.24*1/12 / P(8) = 1/3 = 0.333
    posterior(20) = 0.40*1/20 / P(8) = 1/3 = 0.333
    ```

    Which die do we think is most likely? Is this different than what you got with the previous prior?

    *This gives us that the last 3 dice are equally likely. This is different from the uniform prior which gave the 8-sided die as the most likely candidate.*

7. Say you keep the same prior and you roll the die 50 times and get values 1-8 every time. What would you expect of the posterior? How different do you think it would be if you'd used the uniform prior?

    *The posterior would be really certain that it was the 8-sided die at this point. You wouldn't see much difference from the uniform prior since the data washes out the prior.*
