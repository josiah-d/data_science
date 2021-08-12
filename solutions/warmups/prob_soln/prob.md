### Probability Practice

1. Let's say we play a game where I keep flipping a coin until I get heads. If the first time I get heads is on the `n`th coin, then I pay you `2n-1` dollars. How much would you pay me to play this game?

    You should end up with a sequence that you need to find the closed form of. If you don't know how to do this, write some python code that sums the first 100.

    ``` W = Winnings. E(W) = sum_{n >= 1} (2n-1)/2^n  = 3 ```

2. Write a program to simulate the game and verify that your answer is correct.
    
    ``` python
    import numpy as np

    def coin():
        tails, num_flips = True, 0
        while tails:
            num_flips += 1
            if np.random.binomial(1, 0.5):
                tails = False
        return num_flips

    def main():
        flips_required = np.array([coin() for _ in range(10000)])
        winnings = 2*flips_required - 1
        avg_winnings = np.mean(winnings)
        print(avg_winnings)

    if __name__ == '__main__':
        main()
    ```
    
    Alternatively, you could use the [geometric distribution](https://en.wikipedia.org/wiki/Geometric_distribution), which generates the number of Bernoulli trials needed until the first success. This approach allows you to stick to `numpy` arrays, which are much speedier than `for` loops. 

    ```python
        import numpy as np

        def main():
            flips_required = np.random.geometric(p=0.5, size=10000)
            winnings = 2*flips_required - 1
            avg_winnings = np.mean(winnings)
            print(avg_winnings)

        if __name__ == '__main__':
            main()
    ```
