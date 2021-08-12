# The Central Limit Theorem and its Associated Confidence Intervals

## Basic
## Part 1: Simulation Experiments

The Central Limit Theorem states that the mean of a sufficiently large number of samples of independent random variables, will be approximately normally distributed (with the quality of the approximation improving with larger samples).

Since the CLT applies to (almost) all distributions, its application is ubiquitous in statistics. In the first section we will build some simulation chops by exploring the CLT.

1. As we explore the CLT we will be plotting means of samples drawn from several different distributions.  In order to do this efficiently we need to pass the Scipy distribution objects ([docs here](http://docs.scipy.org/doc/scipy-0.17.1/reference/stats.html)) and their parameters to the following plotting function. This function generates draws from a distribution by calling the `.rvs()` method.

You can use this code to generate data from at least the **Poisson, Binomial, Exponential, Geometric, and Uniform** distributions. The example of generating data from `Binomial` distribution is provided.

**Your task is to create examples of utilizing the `make_draws()` function to generate data from `Poisson`, `Exponential`, `Geometric` and `Uniform` distributions.** Note that the `dict` will be different for different distributions.



  ```python
  import scipy.stats as stats

  def make_draws(dist, params, size=200):
      """
      Draw a sample from a specified distribution
      with given parameters and return these in an array.

      Parameters
      ----------

      dist: scipy.stats distribution object:
        Distribution object from scipy.stats, must have a .rvs method

      params: dict:
        Parameters needed to define the distribution dist.
      For example, if dist = scipy.stats.binom, then params could be

            {'n': 100, 'p': 0.25}

      size: int:
        The number of values to draw

      Returns
      -------
      sample: np.array, shape (size, )
        An i.i.d sample from the specified distribution.
      """
      return dist(**params).rvs(size)

  # Generate draws from the Binomial Distribution, using Scipy's binom object.
  binomial_samp = make_draws(stats.binom, {'n': 100, 'p':0.25}, size=200)
  ```

Implementation Notes:
    This may be the first time you've seen the `**` construction.  The `**params` notation unpacks the `params` dictionary and passes the items in the dict as keyword arguments into the `dist` function.  If this is unfamiliar, check out the [docs](https://docs.python.org/2/tutorial/controlflow.html#unpacking-argument-lists) and/or [stackoverflow](http://stackoverflow.com/questions/1179223/in-python-when-passing-arguments-what-does-before-an-argument-do).

2. Now that you are comfortable drawing samples from various distributions, let's explore some behavior of samples.  Implement a `plot_means` function that takes the same parameters as `make_draws()` but adds two extra parameters:

  - `ax`: pyplot.Axis object.  The axis to draw a plot on.
  - `repeat`: int.  The number of samples of size `size` to draw.

The `plot_means` function should draw `repeat` number of samples of size `size`, and compute the means of each of those samples.  Then it should draw a histogram of the resulting sample means on the supplied `ax`.


You can refer to the following code snippet for the central logic of `plot_means()` function
```python
  samples = np.zeros((repeat, size))
  # a placeholder for all sampled data
  for idx in range(repeat):
      samples[idx,:] = make_draws(dist, params, size=size)
      # assign each row a sample
  sample_means = np.mean(samples, axis=1)
  # obtain the sample mean for each sample (each row)
  ax.hist(sample_means, bins=25)
  # plot the sample means on the given axis
```

3. Call `plot_means()` with at least each of the following distributions:
   - Binomial
   - Poisson
   - Exponential
   - Geometric
   - Uniform

   Try out different parameter settings for each of the distributions, as well
   as varying the `size` and `repeat` choices. Initial choices for the `size` 
   and `repeat` might be 200 and 5000. If the distribution of means resembles 
   a normal distribution regardless of the distribution you have specified, 
   you have some evidence for the central limit theorem! (Failure to observe this phenomenon means 
   because of the asymmetry and skew of the distribution of the data being
   sampled more samples are needed before the CLT effect will begin to emerge!)

4. What do you observe if you change the sample `size` to 10 instead of 200,
   keeping `repeat` constant at 5000? Explain your observation on a high
   level. Should the CLT apply when your sample `size` is small with a large
   value for `repeat`?  Hint: this is best answered by distinguishing
   between the role of the `size` and the `repeat` variable.

5. Instead of taking the mean of the samples, take the maximum of each of the
   samples and plot the histograms again. Do they resemble the normal
   distribution? Do all sample statistics follow a normal distribution?  In
   your answer clarify the sample statistics to which the CLT applies.

<br>

## Advanced
### Part 2: Population Inference and Confidence Intervals

The central limit theorem has great utility for making statistical inferences about sample means, since it gives an almost complete description of their properties.  In particular, the most popular type of confidence interval is derived from an understanding of the central limit theorem.


1. Suppose Google sampled 200 of its employees and measured how long they are gone for lunch. Load the data `data/lunch_hour.txt` into a numpy array or pandas DataFrame and compute the mean lunch hour of the sample.

2. Viewing the lunch hour data as an i.i.d sample from the lunch hours of ALL Google employees, the sample mean is a random variable, and we have a single draw from it.  What is the distribution of this sample mean random variable, and how do you know?

3. Compute the [standard error](http://en.wikipedia.org/wiki/Standard_error) of the sample mean. Based on the standard error and the sample mean, compute the [95% confidence interval](https://en.wikipedia.org/wiki/Confidence_interval#Basic_steps) for the population mean lunch break length.

4. Interpret what the 95% confidence interval implies about the lunch hours of Google employees in general.

5. If the sample size were smaller, how would that affect the 95% CI? Explain your answer.  Suppose the sample size was 10, does your assumption from `2.` still hold? Explain your answer.
