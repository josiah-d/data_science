from scipy import stats
import numpy as np
import matplotlib.pyplot as plt


def make_draws(dist, params, size=200):
    """Return array of samples from dist with given params.

    Draw samples of random variables from a specified distribution, dist, with
    given parameters, params, return these in an array.

    Parameters
    ----------
    dist: Scipy.stats distribution object
        Distribution with a .rvs method

    params: dict
        Parameters to define the distribution dist.
                e.g. if dist = scipy.stats.binom then params could be:
                {'n': 100, 'p': 0.25}

    size: int, optional (default=200)
        The number of random variables to draw.

    Returns
    -------
    Numpy array: Sample of random variables
    """
    return dist(**params).rvs(size)


def plot_bootstrapped_statistics(dist, params, stat_function=np.mean, size=200, repeats=5000):
    """Plot distribtuion of sample means for repeated draws from distribution.

    Draw samples of specified size from Scipy.stats distribution and calculate
    the sample mean.  Repeat this a specified number of times to build out a
    sampling distribution of the sample mean.  Plot the results.

    Parameters
    ----------
    dist: Scipy.stats distribution object
            Accepts: scipy.stats: .uniform, .poisson, .binom, .expon, .geom

    params: dict
        Parameters to define the distribution dist.
            e.g. if dist = scipy.stats.binom then params could be:
            {'n': 100, 'p': 0.25}

    stat_function: function
        Statistic to be calculated on bootrapped samples, e.g., np.max or np.mean

    size: int, optional (default=200)
        Number of examples to draw.

    repeats: int, optional (default=5000)
        Number of sample means to calculate.

    Returns
    -------
    ax: Matplotlib axis object
    """
    dist_instance = dist(**params)

    bootstrapped_statistics = []
    for _ in range(repeats):
        values = dist_instance.rvs(size)
        bootstrapped_statistics.append(stat_function(values))

    d_label = {
        stats.uniform: ['Uniform', 'Mean of randomly drawn values from a uniform'],
        stats.poisson: ['Poisson', 'Mean events happening in an interval'],
        stats.binom: ['Binomial', 'Mean number of successes'],
        stats.expon: ['Exponential', 'Mean of waiting time before an event'],
        stats.geom: ['Geometric', 'Mean trials until first success']
        }

    dist_name, xlabel = d_label[dist]
    title_str = 'Mean of {0} samples with size {1} drawn from {2} distribution'
    title_str = title_str.format(repeats, size, dist_name)

    fig, ax = plt.subplots(figsize=(7, 6))

    ax.hist(bootstrapped_statistics, bins=30)
    ax.set_xlabel(xlabel)
    ax.set_ylabel('Counts')
    ax.set_title(title_str, fontsize=14)
    
    return ax


def sample_sd(arr):
    """Sample Standard Deviation.

    ddof=1 means Delta Degrees of Freedom, changes denom. to N-1.

    Parameters
    ----------
    arr: Numpy array
        Array of data.

    Returns
    -------
    float
    """
    return np.std(arr, ddof=1)


def standard_error(arr):
    """Compute standard errror of arr.

    Parameters
    ----------
    arr: Numpy array

    Returns
    -------
    float
    """
    return sample_sd(arr) / np.sqrt(len(arr))


def bootstrap(arr, iterations=10000):
    """Create a series of bootstrapped samples of an input array.

    Parameters
    ----------
    arr: Numpy array
        1-d numeric data

    iterations: int, optional (default=10000)
        Number of bootstrapped samples to create.

    Returns
    -------
    boot_samples: list of arrays
        A list of length iterations, each element is array of size of input arr
    """
    if type(arr) != np.ndarray:
        arr = np.array(arr)

    if len(arr.shape) < 2:
        arr = arr[:, np.newaxis]
        # [:, np.newaxis] increases the dimension of arr from 1 to 2

    nrows = arr.shape[0]
    boot_samples = []
    for _ in range(iterations):
        row_inds = np.random.randint(nrows, size=nrows)
        # because of the [:, np.newaxis] above 
        # the following will is a 1-d numeric data with the same size as the input arr
        boot_sample = arr[row_inds, :]
        boot_samples.append(boot_sample)

    return boot_samples


def bootstrap_confidence_interval(sample, stat_function=np.mean, iterations=1000, ci=95):
    """Calculate the CI of chosen sample statistic using bootstrap sampling.

    CI = confidence interval

    Parameters
    ----------
    sample: Numpy array
        1-d numeric data

    stat_function: function, optional (default=np.mean)
        Function for calculating as sample statistic on data

    iterations: int, optional (default=1000)
        Number of bootstrap samples to create

    ci: int, optional (default=95)
        Percent of distribution encompassed by CI, 0<ci<100

    Returns
    -------
    tuple: lower_ci(float), upper_ci(float), bootstrap_samples_statistic(array)
        Lower and upper bounds of CI, sample stat from each bootstrap sample
    """
    boostrap_samples = bootstrap(sample, iterations=iterations)
    bootstrap_samples_stat = list(map(stat_function, boostrap_samples))
    low_bound = (100. - ci) / 2
    high_bound = 100. - low_bound
    lower_ci, upper_ci = np.percentile(bootstrap_samples_stat,
                                       [low_bound, high_bound])
    return lower_ci, upper_ci, bootstrap_samples_stat


def pearson_correlation(arr):
    """Calculate the Pearson Correlation in a two-dimensional data set.

    Optionally return a P-value of the significance of the correlation.

    Parameters
    ----------
    arr: Numpy array
        Numeric array of size N x 2

    p_val: boolean, optional (default=False)
        Return P-value if True

    Returns
    -------
    corr_coeff: float
        The Pearson Correlation Coefficient

    p_val: float
        P-value of significance of the correlation.
    """
    col1 = arr[:, 0]
    col2 = arr[:, 1]
    corr_coeff, pval = stats.stats.pearsonr(col1, col2)
    return corr_coeff, pval
