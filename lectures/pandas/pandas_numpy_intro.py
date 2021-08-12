# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.1.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Pandas 
#
# ## Objectives
#
# * Create `Series` and `DataFrame`s from Python data types. 
# * Create `DataFrame`s from on disk data.
# * Index and Slice `pandas` objects.
# * Aggregate data in `DataFrame`s.
# * Join multiple `DataFrame`s.

# ## What is Pandas?
# A Python library providing data structures and data analysis tools. The name comes from "panel data"; think about it as a way to visualize and sift through tables of data, similar to R or (heaven forfend) Excel.
#
# * They are built on top of NumPy NdArrays
# * http://pandas.pydata.org/pandas-docs/stable/comparison_with_sql.html
#
#
#
# ## Benefits
#
# * Efficient storage and processing of data.
# * Includes many built in functions for data transformation, aggregations, and plotting.
# * Great for exploratory work.
#
# ## Not so greats
#
# * Does not scale terribly well to large datasets.
#
# ## Documentation:
#
# * http://pandas.pydata.org/pandas-docs/stable/index.html

# +
#By convention import pandas like:
import pandas as pd
#By convention import numpy like:
import numpy as np
#Make sure you have both lines when using matplotlib in Jupyter notebook
import matplotlib.pyplot as plt
#For fake data.
from numpy.random import randn
np.random.seed(123)

# %matplotlib inline
plt.style.use('ggplot')

# +
# np.random.seed(123)
# np.random.randn(3,4) # np.random.randn(3,4).round(2)
# -

# # Pandas is built on Numpy
# * Numpy is one of the fundamental packages for scientific computing in Python.
#
#
# ## Numpy Arrays
# * Or NdArrays (n-dimensional array)
# * They are like lists in Python however they allow faster computation
#     1. They are stored as one contiguous block of memory, rather than being spread out across multiple locations like a list. 
#     2. Each item in a numpy array is of the same data type (i.e. all integers, all floats, etc.), rather than a conglomerate of any number of data types (as a list is). We call this idea homogeneity, as opposed to the possible heterogeneity of Python lists.
#
#
# Just how much faster are they? Let's take the numbers from 0 to 1 million, and sum those numbers, timing it with both a list and a numpy array.
#

# +
numpy_array = np.arange(0, 1e6)
python_list = list(range(int(1e6)))

print("python list")
time = %timeit -n 100 -r 1 -o sum(python_list) # -r how many times to repeat the timer (default 3)
print (time.all_runs[0]/time.loops )

print("\n" + "numpy array")
time = %timeit -n 100  -r 1 -o np.sum(numpy_array)
print (time.all_runs[0]/time.loops)

print("\n" + "numpy array -- standard library sum")
time = %timeit -n 100  -r 1 -o sum(numpy_array)
print(time.all_runs[0]/time.loops)
# -

# ## Numpy NdArrays
#
# * have types
# * Each array is of one type

# +
ints = np.array(range(3))
chars = np.array(list('ABC'))
strings = np.array(['A','BC',"DEF"])

print(ints.dtype, chars.dtype, strings.dtype)
# -

chars

strings

ints

ints*0.3

(ints*0.3).dtype

# ## Creating and using NdArrays

my_lst_ndarray = np.array([1, 2, 3, 4, 5])
my_tuple_ndarray = np.array((1, 2, 3, 4, 5), np.int32) 

print(my_lst_ndarray.dtype)
print(my_tuple_ndarray.dtype)

print(my_lst_ndarray.shape)
print(my_tuple_ndarray.shape)

# +
# np.array?
# -

# ## 2D arrays

nd_arr = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10],[11, 12, 13, 14, 15]])
nd_arr

# ## Access info in the array
# * Individual data
# * Slices of data

nd_arr[1,1]

nd_arr[0:2,0:2]

nd_arr.shape

nd_arr.sum()

# +
# nd_arr.sum?
# -

nd_arr.sum(axis=1)

nd_arr.sum(axis=0)

nd_arr.max()

# ## Broadcasting

a = np.array([10, -10]) 
b = np.array([1, -1])
c = np.array([0.5, 4, 1])

a

b

a + b

c

a + c

# +
a = np.array([[10], [-10]]) 
b = np.array([[1, 2], [-1, -2]]) 

print("a = \n{}\n".format(a))
print("b = \n{}\n".format(b))
print("a + b = \n{}".format(a + b))

# elements will "duplicate, expand, and fill up" 
# to make the dimensions compatible for element-wise operations

# +
print("a = \n{}\n".format(a))

print("a + 4 = \n{}\n".format(a + 4))

print("a*3 = \n{}".format(a*3))
# -

a.shape

a = np.array([[10, 0, -10, 0],[-10, 0, -10, 0]]) 
b = np.array([[2,2],[-1,0]]) 
print ("the shape of a is {}, the shape of b is {}\n".format(a.shape, b.shape))
print("a = \n{}\n".format(a))
print("b = \n{}".format(b))
# a+b

# Now do 
a + b

# + {"code_folding": []}
# it's not clear how it should fill up in this case... so it can't/doesn't
# -

# ----------------------------------------------------
#
# # Pandas Series
# * are (one dimensional) np.ndarray vectors **with an index**
# * They are built upon NdArrays

series = pd.Series([5775,373,7,42,np.nan,33])
print("series is \n{}\n".format(series))
print("the shape of the series is {}".format(series.shape))

world_series = pd.Series(["cubs","royals","giants","sox","giants","cards","giants","...",None])
world_series

# ## Pandas Series are very powerful when dealing with dates

# +
# pd.date_range?

# +
#Datetime index
dt_index = pd.date_range('2015-1-1', '2015-11-1', freq='m')

np.random.seed(999)
dt_series = pd.Series(randn(10), 
                      index = dt_index)
dt_series
# -

# ## Series methods

round(dt_series.mean(), 2)

# # Index
# Notice how each series has an index (in this case a relatively meaningless default index).
#
# Pandas can make great use of informative indexes. Indexes work similarly to a dictionary key, allowing fast lookups of the data associated with the index.
#
# Indexes can also be exploited for fast group-bys, merges, time-series operations and lots more.
#
# When you're really in the zone with pandas, you'll be thinking a lot about indexes.

# +
np.random.seed(999)

indexed_series = pd.Series(randn(5), 
                           index = ['California', 'Alabama', 
                                    'Indiana', 'Montana', 
                                    'Kentucky'])
alt_indexed_series = pd.Series(randn(5),
                               index = ['Washington', 'Alabama', 
                                        'Montana', 'Indiana', 
                                        'New York'])
print("indexed_series = \n{}\n".format(indexed_series))
print("alt_indexed_series = \n{}".format(alt_indexed_series))
# -

#Pandas uses the index by default to align series for arithmetic!
indexed_series + alt_indexed_series

# # Pandas `DataFrame`s
# * are a set of Pandas Series **that share the same index** 
#

pd.DataFrame(
    [[1, 2, 3], [4, 5, 6]], 
    columns=['a', 'b', 'c'], 
    index=['foo', 'bar'])

np.random.seed(888)
df = pd.DataFrame(randn(10, 5), 
                  index=dt_index,
                  columns=[x for x in 'abcde'])
df

# ## To select just one column, use brackets
#

df['a']

# You can also use the "dot notation" for selecting a column

df.a

# Note that this will fail if your column has the same name as a dataframe method, so you may wish to avoid this notation.

# +
# df.
# -

# ## To select one row, use .loc[]

df.loc['2015-10-31']

# ## A column of a dataframe is a series:

col = df['d']
type(col)

# ## So is a row

row = df.loc['2015-01-31']
type(row)

# ### The columns all have the same index:

col.index   

# ### What's the index for the rows?

row.index

df.index

df.columns

# ## Selecting multiple columns

df[['a','b']]

# ## Column operations
# Just like numpy, operations are broadcast to every element of a column

df['a'] + df['b']

# ## Adding a new column
# It's just like setting by key in a dictionary

df['h'] = abs(df['a'])**df['b']

df

# ## Advanced selection
#

# ### .loc 
# select by row label (index), and column label

df.loc['2015-05-31':'2015-08-31', 'c':'e'] #Ranges by label.

df.loc['2015-05-31':'2015-08-31', 'c':'e'] = 2.7

df

# ### .iloc
# select by __positional__ index

df.iloc[2:4,2:5] #Ranges by number.

# ### .ix (deprecated)
# select by either label or position index
# (deprecated because it led to too much ambiguity)

df.ix[2:-3,2:5] # Figures out what you probably want

df.ix['2015-05-31':'2015-08-31', 'c':'e']

# # DO NOT USE .ix 
# It is here so you can recognize it and scold others for using it.
#   
#   
# --------------------------------------------------------------------------------------------     
#         
#       
#       
# # Multiple Indices

# Start with a df with a single date index

np.random.seed(777)
dt_index = pd.date_range('2015-1-1', '2017-7-1', freq='m')
df = pd.DataFrame(randn(30,5), index=dt_index)
df

# Let's add new column of states

df['state'] = ['Alabama', 'Alaska' , 'Arizona'] * 10
df.head()

# `reset_index` shifts the index to a column, then gives the rows a boring old positional index

df = df.reset_index()

df

# `set_index` sets columns to indices

df = df.set_index(['state', 'index'])
df.head()

df.loc['Alabama'].head()

# +
# df.loc['2015-01-31'] #Doesn't work.
# -

df.loc[('Alabama', '2015-01-31')] #Can do this.

# # Loading data from a file

df = pd.read_csv('data/winequality-red.csv', delimiter=';')

df.head()  #Display the first x rows (default is 5)

df.shape

df.columns

df.info()

df.describe()

df.tail()

# # Filtering (i.e., row selecting or boolean indexing)

df['chlorides']

df['chlorides'] <= 0.08 

mask = df['chlorides'] <= 0.08 

mask

type(mask)

# You can use a boolean series to "mask" a dataframe / series, returning only those rows where the mask is `True`

df[mask]

# Okay, this is cool. What if I wanted a slightly more complicated query...
df[(df['chlorides'] >= 0.04) & (df['chlorides'] < 0.08)]

df2 = df[(df['chlorides'] >= 0.04) & (df['chlorides'] < 0.08)][['pH','fixed acidity']]

df2.head()

df2.sort_values('pH').reset_index().head()

df2.sort_values('pH').reset_index(drop=True).head()

# # Groupby

df.head()

g = df.groupby('quality') # Note that this returns back to us a groupby object. It doesn't actually 
                      # return to us anything useful until we perform some aggregation on it. 
g

g.max()['density']

# +
# Note we can also group by multilple columns by passing them in in a list. It will group by 
# the first column passed in first, and then the second after that (i.e., it will group by 
# the second within the group by of the first). 
df2 = df.groupby(['pH', 'quality']).count()['chlorides']

df2.head(20)
# -

# # Remove columns

# +
# add a computed column

df['pct_free_sulf'] = df['free sulfur dioxide'] / df['total sulfur dioxide']
# -

df.head()

# +
# Dropping a row

# +
# df.drop('pct_free_sulf')
# -

df.drop('pct_free_sulf', axis = 1).head()

df.columns

# # Managing Missing Values
# * http://pandas.pydata.org/pandas-docs/stable/missing_data.html

miss_val_df = pd.DataFrame(
    [[1, 2, 3], [4, np.nan, 6]], 
    columns=['a', 'b', 'c'], 
    index=['foo', 'bar'])
miss_val_df

miss_val_df.fillna(0)

miss_val_df

# IF YOU WANT THE CHANGE TO HAPPEN INPLACE YOU MUST SPECIFY:
miss_val_df.fillna(0,inplace=True)
miss_val_df

# + {"code_folding": []}
## DROP ROW
# -

miss_val_df['b']['foo'] = np.nan

miss_val_df

miss_val_df.dropna()

# # Merge 
# * http://pandas.pydata.org/pandas-docs/stable/merging.html
#
# We can join DataFrames in a similar way that we join tables to SQL.  In fact, left, right, outer, and inner joins work the same way here.

# +
merge1 = pd.DataFrame(
    [[1, 2, 3], [4, 3, 6]], 
    columns=['a', 'b', 'c'])

merge2 = pd.DataFrame(
    [[1, 2, 3], [4, 3, 6]], 
    columns=['z', 'b', 'y'])

print("merge1 = \n{}\n\nmerge2=\n{}\n".format(merge1, merge2))
# -

merged_df = merge1.merge(merge2, how='outer')

merged_df

# # Concatenating
# * adding *rows*
# * see also: df.append()

df1 = pd.DataFrame(
    {'Col1': range(5), 'Col2': range(5), 'Col3': range(5)})
df2 = pd.DataFrame(
    {'Col1': range(5), 'Col2': range(5), 'Col4': range(5)},
    index=range(5, 10))

df1

df2

#Vertically
pd.concat([df1, df2], axis=0, sort=False)

pd.concat([df1, df2], join='outer', axis=1)

# # Categorical data

df = pd.read_csv('data/playgolf.csv', delimiter=',' )
df.head()

# df.value_counts() gets you the frequencies

df['Outlook'].value_counts()

# Using apply will get you the value counts for multiple columns at once

df[['Outlook','Result']].apply(lambda x: x.value_counts())

# Contingency Tables for looking at bivariate relationships between two categorical variables

pd.crosstab(df['Outlook'], df['Result'])

# Often we want the row percentages

pd.crosstab(df['Outlook'], df['Result']).apply(lambda r: r/r.sum(), axis=1)

# Or the column percentages

pd.crosstab(df['Outlook'], df['Result']).apply(lambda c: c/c.sum(), axis=0)

# # Plotting DataFrames

df = pd.read_csv('data/playgolf.csv', delimiter=',' )
df.head()

df.hist(['Temperature','Humidity'],bins=5);

df[['Temperature','Humidity']].plot(kind='box');

df.plot('Temperature', 'Humidity', kind='scatter');

groups=df.groupby('Outlook')
for name, group in groups:
    print(name)

# +
fig, ax = plt.subplots(figsize = (8,6))

ax.margins(0.05)
for name, group in groups:
    ax.plot(group.Temperature, group.Humidity,\
            marker='o', linestyle='', ms=12, label=name)
ax.legend(numpoints=1, loc='lower right')

plt.show()
# -

df.head()

df['Outlook'].value_counts()

df['Windy'].value_counts()

g = df.groupby(['Outlook', 'Windy'])

g.max()

g.agg(max) # ? type(g.agg(max))

df_th = g.agg(max)[['Temperature','Humidity']]
df_th

df_th.unstack()

df_th.unstack()['Temperature']

df_th.reset_index()

df
