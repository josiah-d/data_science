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

# Alternative approach that uses a geometric distribution and avoids a for loop.

# import numpy as np

# def main():
#     flips_required = np.random.geometric(p=0.5, size=10000)
#     winnings = 2*flips_required - 1
#     avg_winnings = np.mean(winnings)
#     print(avg_winnings)

# if __name__ == '__main__':
#     main()