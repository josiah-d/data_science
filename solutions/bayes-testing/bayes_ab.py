import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
plt.style.use('ggplot')


def plot_with_fill(ax, x, y, label):
    lines = ax.plot(x, y, label=label, lw=2)
    ax.fill_between(x, 0, y, alpha=0.2, color=lines[0].get_c())
    ax.legend(loc='best')


def get_pdf(x, site):
    ''' The function will return the pdf for a given beta distribution

    Parameters
    -----------
    x : Array of x values
    site : Array cooresponding to the site in question

    Returns
    --------
    numpy array
    '''
    alpha = sum(site)
    beta = len(site) - alpha
    return stats.beta(a=alpha, b=beta).pdf(x)


def expected_profit_difference(hits, expect_a, expect_b):
    ''' Returns the expected profit from switching from A to B

    Parameters
    -----------
    hits : int number of clicks you expect your site to recieve
    expect_a : Expected value of Site A
    expect_b : Expected value of Site B

    Returns
    --------
    profit : float
    '''
    return expect_b * 1.05 * hits - expect_a * 1.00 * hits


if __name__ == '__main__':
    ''' Question 1 '''
    site_a = np.loadtxt('data/siteA.txt')
    site_b = np.loadtxt('data/siteB.txt')

    # Create x range
    x = np.arange(0, 1.001, 0.001)

    ''' Question 2 '''
    y_prior = stats.uniform().pdf(x)

    fig, ax = plt.subplots(figsize=(10, 5))
    plot_with_fill(ax, x, y_prior, 'Prior')

    ax.set_xlabel('Click Through Rate')
    plt.savefig('Question_2.png')
    plt.close()

    ''' Question 3 '''
    y_prior = stats.beta(a=1, b=1).pdf(x)
    fig, ax = plt.subplots(figsize=(10, 5))
    plot_with_fill(ax, x, y_prior, 'Prior with Beta Distribution')
    ax.set_xlabel('Click Through Rate')
    plt.savefig('Question_3.png')
    plt.close()

    ''' Question 4 '''
    y_50a = get_pdf(x, site_a[:50])

    ''' Question 5 '''
    fig, ax = plt.subplots(figsize=(10, 5))
    plot_with_fill(ax, x, y_prior, 'Prior')
    plot_with_fill(ax, x, y_50a, 'Posterior After 50 Views')
    ax.set_title('Site A')
    ax.set_xlabel('Click Through Rate')
    plt.savefig('Question_5.png')
    plt.close()

    ''' Question 6 '''
    # Let's do this all in one step to make graphing this more managable
    views = [50, 100, 200, 400, 800]

    # Create our y_a for each view count in views
    y_a = [get_pdf(x, site_a[:view]) for view in views]

    # Create the labels for passing to the plot_with_fill function
    labels = ['Posterior After {} Views'.format(view) for view in views]

    # Now let's actually plot all these at once
    fig, ax = plt.subplots(figsize=(10, 5))
    plot_with_fill(ax, x, y_prior, 'Prior')
    for y, label in zip(y_a, labels):
        plot_with_fill(ax, x, y, label)
    ax.set_title('Site A')
    ax.set_xlabel('Click Through Rate')
    ax.set_xlim([0, 0.4])
    plt.savefig('Question_6.png')
    plt.close()

    ''' Question 7 '''
    # First we want to determine y_a and y_b after 800 views
    y_a = get_pdf(x, site_a[:800])
    y_b = get_pdf(x, site_b[:800])

    # Let's plot each
    fig, ax = plt.subplots(figsize=(10, 5))
    plot_with_fill(ax, x, y_prior, 'Prior')
    plot_with_fill(ax, x, y_a, 'A Posterior After 800 Views')
    plot_with_fill(ax, x, y_b, 'B Posterior After 800 Views')

    # Now let's zoom in on just the portion of the graph we are concerned with
    ax.set_xlim(0, 0.3)
    ax.set_title('Site A Vs. Site B')
    ax.set_xlabel('Click Through Rate')
    plt.savefig('Question_7.png')
    plt.close()

    ''' Question 8 '''
    # First let's take 10000 draws for each like so...
    a_sample = np.random.beta(a=sum(site_a), b=800-sum(site_a), size=10000)
    b_sample = np.random.beta(a=sum(site_b), b=800-sum(site_b), size=10000)

    # Now let's get the percentage of the time that the draw from Site B
    # is larger than the draw from Site A
    prob = (b_sample > a_sample).mean() * 100
    print('There is a {:.2f}% probability that Site B is better than Site A\n'.format(prob))

    ''' Question 9 '''
    # We first need to calculate the lower bound using stats.beta.ppf function
    lower_a = stats.beta(a=sum(site_a), b=800-sum(site_a)).ppf(0.025)
    # Let's now do the same for the upper bound
    upper_a = stats.beta(a=sum(site_a), b=800-sum(site_a)).ppf(0.975)
    print("A's 95% HDI is {:.5f} to {:.5f}".format(lower_a, upper_a))

    # Let's now do the same for Site B
    lower_b = stats.beta(a=sum(site_b), b=800-sum(site_b)).ppf(0.025)
    upper_b = stats.beta(a=sum(site_b), b=800-sum(site_b)).ppf(0.975)
    print("B's 95% HDI is {:.5f} to {:.5f}\n".format(lower_b, upper_b))

    ''' Question 10 '''
    # Now let's get the percentage of the time that the draw from Site B is
    # larger than the draw from Site A using the samples we defined earlier
    prob = (b_sample > a_sample + 0.02).mean() * 100
    print('There is a {:.2f}% probability that Site B is 2% better than Site A\n'.format(prob))

    # Now let's take a look at the histogram of the difference b/w B and A + 2%
    site_diff = b_sample - (a_sample + 0.02)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.hist(site_diff, bins=100);
    plt.savefig('Question_10.png')
    plt.close()

    ''' Question 11 '''
    # Let's first look at the difference between Site A and B
    print('Frequentist Comparison of Site A and B')
    t, p = stats.ttest_ind(site_a, site_b)
    if p < 0.05:
        print("We can reject null hypothesis. P-value: {}\n".format(p))
    else:
        print("We cannot reject null hypothesis. P-value: {}\n".format(p))

    # Now let's look whether B is 2% better than A
    print('Is Site B 2% better than Site A?')
    t, p = stats.ttest_ind(site_a + 0.02, site_b)
    if p < 0.05:
        print("We can reject null hypothesis. P-value: {}\n".format(p))
    else:
        print("We cannot reject null hypothesis. P-value: {}\n".format(p))

    ''' Question 12 '''
    # Let's first find the expected values of each site
    expect_a = a_sample.mean()
    expect_b = b_sample.mean()

    # Using the expected_profit_difference function let's look at a wide range
    # of possible hits
    hits = [10000 * 10**p for p in range(6)]
    diffs = [expected_profit_difference(hit, expect_a, expect_b)
             for hit in hits]
    for hit, diff in zip(hits, diffs):
        print("Expected difference of ${:.2f} for {} hits".format(diff, hit))
