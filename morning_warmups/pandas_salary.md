## Warmup: Pandas Practice

**Include your code and answers in** `pandas_salary.py`.

Load `data/salary_data.csv` into a pandas dataframe and answer the following
questions.

1. Rename the columns as `['Name', 'Job', 'Department', 'Salary', 'Date']`

2. Check the data types in each column using `df.info()`.

   Which column has the wrong data type? Use `apply` on the column
   to replace it with the right type.

3. List the top 5 job titles with the highest average salaries.

4. Find the number of people who have the word `POLICE` in their
   `Job`.

   **Read about** `.str.contains()` [**here**](http://stackoverflow.com/questions/11350770/pandas-dataframe-select-by-partial-string).

5. For the people who have the word `POLICE` in their `Job`,
   what percentage of them are `POLICE OFFICER`?

   **This is achievable in one line of code.**

6. How many people joined between 13th July, 2000 and 13th August, 2000?

   Set the `Date` column as the index. Sort the dataframe by the index.
   Select rows of a particular time window,
   e.g. `df.loc['2000-07-13' : '2000-08-13']`.

   Pandas has a comprehensive suite of functions for time series data. Read
   more [here](http://nbviewer.ipython.org/github/changhiskhan/talks/blob/master/pydata2012/pandas_timeseries.ipynb)

