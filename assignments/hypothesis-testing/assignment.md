# Hypothesis Testing

## Basic

### Part 1: Analyzing Click Through Rate

We will use hypothesis testing to analyze **Click Through Rate (CTR)** on the New York Times website. CTR is defined as the number of clicks a user makes per impression that is made upon the user (impression means view, so how the frequency that the user clicks on something they have seen).

We are going to determine if there is statistically significant
difference between the mean CTR for the following groups:

```
1. Signed in users v.s. Not signed in users
2. Male v.s. Female
3. Each of 7 age groups against each other (7 choose 2 = 21 tests)
```

1. Load `data/nyt1.csv` in a pandas dataframe called `nyt_ctr_df`.

   Use `nyt_ctr_df.info()` to make sure the data types are valid and there are no null values.  This data has been cleaned for you, but generally it is good practice to check for those.

2. Make a new column `CTR` using the `Impressions` and the `Clicks` columns.
    - hint: check the definition of `CTR`, it is a ratio.

3. Are there any `nan`'s now?  If so, did you just create them?  If so, what should you do? (i.e., watch out for rows with zero impressions).

   - hint: How would you handle rows with `0` impression?

4. Plot the distribution of each column in the dataframe. Do that using `nyt_ctr_df.hist()`.

   Check out the arguments you can use with the function
   [here](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.hist.html).

   - hint: Set the `figsize=(12,5)` to make sure the graph is readable.

5. Make 2 dataframes - one a dataframe of 'users who are signed in' called `ctr_signed_in` and a second of 'users who are not signed in' called `ctr_not_signed_in`. Plot the distributions of the columns in each of the dataframes in a way that they can be easily compared. By visually inspecting the two sets of distributions, describe the differences between users who are signed in and not signed in?

6. Use a Welch's t-test to determine if the mean CTR between the signed-in users and the non-signed-in users is statistically different. Explain how you arrive at your conclusion.

The Welch's t-test, unlike Student's t-test, does *not* assume the two populations (in this case the signed in and non-signed in users) from which the samples are drawn have the same variance. By specifying the `equal_var` argument to be `False`, `ttest_ind` becomes Welch's t-test effectively.

   ```python
   scipy.stats.ttest_ind(a, b, equal_var=False)
   ```

7. On the other hand, the Welch's t-test *does* assume that the two populations are normally distributed!  Does this seem reasonable in this situation?

None: If your answer is *no*, and you are concerned with the consequences of this, you may want to investigate the concept of a non-parametric test, as they make no such strong distributional assumptions.

8. Determine if the mean CTR between male users (1) and female users (0) is statistically different. Use only the rows where the users are signed in (the only case where the gender indicator is meaningful).  

Note: In this data set, the binary encoding of gender is: `Male: 1, Female: 0`

9. Calculate a new column called `AgeGroup`, which bins Age into the following buckets

   `'(7, 18]', (18, 24]', '(24, 34]', '(34, 44]', '(44, 54]', '(54, 64]', '(64, 1000]'`

   Again, Use only the rows where the users are signed in. The non-signed in users all have age 0, which indicates the data is not available.

   - hint: Use pandas' [cut](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.cut.html) function to bucket the ages. Below is an example to split students' scores into groups.

   ```python
   df["score_group"] = pd.cut(df["score"], [60,70,80,90,100], include_lowest = True)
   ```

10. Determine the pairs of age groups where the difference in mean CTR is statistically significant. Collect the p-values and the difference of the means for each pair.  Store these results in a `DataFrame`.

   Rank (in descending order) the difference in mean CTR for the pairs that are statistically significant. Comment on the trend you observe for groups `(64, 1000]`, `(54, 64]` and `(7, 18]`.

   Rank (in ascending order) the difference in mean CTR for the pairs that are _statistically insignificant_. State the 3 groups that are the least different in mean CTR and provide an explanation for why you think this is true.

11. How much do you trust the stories you just told youself.  Imagine that you observed the *exact opposite* situation than you actually did.  Could you come up with a story to justify *that*?

**It's easy to tell yourself stories that justify what you think you have observed.  Be careful about taking them as evidence.**

## Advanced

### Part 2: A / B Testing Landing Pages

Designers at Etsy have created a **new landing page** in an attempt to improve sign-up rate for local meetups.

The impact of a change is often measured using *lift*. Say the historic sign-up rate for the **old landing page** is 10%.  An improvement in the sign-up rate to only 10.1%, while just a .1% absolute improvement, is a multiplicitive change of lift in conversion of 1%, this is a *lift* of 1%.

If the lift statistically significant, the new landing page would be considered a success (that's just how management works at Etsy apparantly).  The product manager will not consider implementing the new page if the lift is not staistically significantly greater than or equal to 1%.

Your task is to determine if the new landing page provides a 1% or more lift to the sign-up rate. You are also given the understanding that there is a very different user base on weekends and an important amount of the revenue comes from those weekend users.

<br>

1. Design an experiment in order to decide if the new page has a 1% lift in sign-up rate as compared to the old page?  Describe in detail the data collection scheme you would use for the experiment. Justify why the data will be collected that way.

Remember that we want to be sure the change is atually *caused* by the switch to the new landing page.
   
2. Why is it useful to report the change in conversion in terms of lift instead of absolute difference in conversion?

3. State your null hypothesis and alternative hypothesis. Is your alternative hypothesis set up for a one-tailed or two-tailed test? Explain your choice.

4. You ran a pilot experiment according to ``Question 1`` for ~1 day (Tuesday). The collected data is in ``data/experiment.csv``. Import the data into a pandas dataframe. Check the data for duplicates and clean the data as appropriate. 

5. Calculate a p-value for a 1% lift from using the new page compare to the old page. We've supplied a `z-test` function that can test for a given amount of lift:

    ```
    H0: ctr_old - ctr_new < lift
    HA: ctr_old - ctr_new >= lift
    ```

The `effect_size` argument will be useful, since we are not looking to see that one click through rate is simply *different* than another, we want to know that they are different *by a certain ammount*.

To import this function (assuming you are running python from the directory containing this `assignemnt.py` file) you should use:

    ```python
    from src.z_test import z_test
    ```

What assumptions are you making when you use such a z-test. Interpret the p-value and explain your decision whether to recommend adopting the new page or not.

6. Assume your test was insignificant. Given the setting of the experiment and the context of the problem, why might you be hesitant to make the conclusion to not use the new landing page. What would you do instead? 
   
7. Why might it be a problem if you keep evaluating the p-value as more data comes in and stop when the p-value is significant?

If it's unclear what the issue with this is, see [this](http://www.evanmiller.org/how-not-to-run-an-ab-test.html) article.

8. One perennial problem for A/B testing is when to stop your test. We will cover a more in-depth treatment of calculating statistical power of your experiment. One semi-quantitative way to assess if your conclusion is going to change if you have had run the experiment longer is to plot the progression of the p-value as a time series. If the p-value is consistent upon the collection of more data over an extended period of time, then you are more confident that your conclusion would stay the same even if the experiment had run on longer.  

   - See Airbnb's talk on this technique [here](http://nerds.airbnb.com/experiments-airbnb/)
   and [here](http://nerds.airbnb.com/experiments-at-airbnb/).
   
   Plot the time series of the p-values using hourly intervals, such that the p-value at the second hour would be evaluating data up to second hour and at the third hour would be evaluating the data up to the third hour. Describe the insights you gain from the plot.
