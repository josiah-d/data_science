*This assumes you've done:* `from bayes import Bayes`

1. Encode both priors as dictionaries.

    ```python
    uniform_prior = {4: 0.2, 6: 0.2, 8: 0.2, 12: 0.2, 20: 0.2}
    unbalanced_prior = {4: 0.08, 6: 0.12, 8: 0.16, 12: 0.24, 20: 0.4}
    ```

2. Implement the likelihood function. It should take the data (in this case a number 1-20) and the die number (4, 6, 8, 12 or 20).

    ```python
    def likelihood(data, val):
        if data > val:
            return 0
        return 1. / val
    ```

3. First, let's examine the case where we only roll the die once. Say we roll a single 8.

    * What are the posteriors if we started with the uniform prior?
    
        ```python
        bayes = Bayes(uniform_prior.copy(), likelihood)
        bayes.update(8)
        bayes.print_distribution()
        ```

        Results:

        ```
        4:0.0
        6:0.0
        8:0.483870967742
        12:0.322580645161
        20:0.193548387097
        ```
    
    * What are the posteriors if we started with the unbalanced prior?
    
        ```python
        bayes = Bayes(unbalanced_prior.copy(), likelihood)
        bayes.update(8)
        bayes.print_distribution()
        ```

        Results:

        ```
        4:0.0
        6:0.0
        8:0.333333333333
        12:0.333333333333
        20:0.333333333333
        ```
    
    * How different were these two posteriors?
    
        *The prior weights higher numbers first, so even though you saw an 8, the 8-sided die is not more likely in the unbalanced case.*

4. Let's say you get all this data:

    ```
    [8,2,1,2,5,8,2,4,3,7,6,5,1,6,2,5,8,8,5,3,4,2,4,3,8,
     8,7,8,8,8,5,5,1,3,8,7,8,5,2,5,1,4,1,2,1,3,1,3,1,5]
    ```

    * What are the posteriors if we started with the uniform prior?

        ```python
        data = [8,2,1,2,5,8,2,4,3,7,6,5,1,6,2,5,8,8,5,3,4,2,4,3,8,
                8,7,8,8,8,5,5,1,3,8,7,8,5,2,5,1,4,1,2,1,3,1,3,1,5]
        bayes = Bayes(uniform_prior.copy(), likelihood)
        for datapoint in data:
            bayes.update(datapoint)
        bayes.print_distribution()
        ```

        Results:

        ```
        4:0.0
        6:0.0
        8:0.999999998432
        12:1.56832854302e-09
        20:1.26765059824e-20
        ```

        It's *incredibly* likely that it's the 8-sided die.
    
    * What are the posteriors if we started with the unbalanced prior?

        ```python
        data = [8,2,1,2,5,8,2,4,3,7,6,5,1,6,2,5,8,8,5,3,4,2,4,3,8,
                8,7,8,8,8,5,5,1,3,8,7,8,5,2,5,1,4,1,2,1,3,1,3,1,5]
        bayes = Bayes(unbalanced_prior.copy(), likelihood)
        for datapoint in data:
            bayes.update(datapoint)
        bayes.print_distribution()
        ```

        Results:

        ```
        4:0.0
        6:0.0
        8:0.999999997648
        12:2.35249281269e-09
        20:3.16912649312e-20
        ```

        It's still *incredibly* likely that it's the 8-sided die.
    
    * How different were these two posteriors?
        
        *The prior becomes essentially irrelevant as you collect more data.*

5. With the uniform prior, which of these two sets of data leads to a more certain posterior? `[1, 1, 1, 3, 1, 2]` or `[10, 10, 10, 10, 8, 8]`

    ```python
    data = [1, 1, 1, 3, 1, 2]
    bayes = Bayes(uniform_prior.copy(), likelihood)
    for datapoint in data:
        bayes.update(datapoint)
    bayes.print_distribution()
    ```

    Results:

    ```
    4:0.905098407035
    6:0.0794599424558
    8:0.0141421626099
    12:0.00124156160087
    20:5.79262980503e-05
    ```

    ```python
    data = [10, 10, 10, 10, 8, 8]
    bayes = Bayes(uniform_prior.copy(), likelihood)
    for datapoint in data:
        bayes.update(datapoint)
    bayes.print_distribution()
    ```

    Results:

    ```
    4:0.0
    6:0.0
    8:0.0
    12:0.955423749541
    20:0.0445762504586
    ```

    *You can see the second example is more certain of the result. It's 95.5% chance of being the 12-sided die. In the first example, it's 90.5% chance of being the 4-sided die. This is because rolling the 10 allows you to eliminate the first three dice.*
