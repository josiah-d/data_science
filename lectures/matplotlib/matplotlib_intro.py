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

# + {"hideCode": false, "hidePrompt": false, "cell_type": "markdown"}
# # Matplotlib
# ## Learning Objectives
#
# 1. Name and recognize the two interfaces to `matplotlib`
# 2. Be able to use both interfaces to generate charts
# 3. Understand the connection between `matplotlib` and `seaborn`/`pandas`
# 4. Make plots with multiple datasets, and figures
# 5. Know the recommended functional form for writing your own plotting functions

# + {"hideCode": false, "hidePrompt": false}
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
# %matplotlib inline
plt.style.use('ggplot')

# + {"hideCode": false, "hidePrompt": false, "cell_type": "markdown"}
# # Plotting in Python
#
# There are many libraries for doing plotting in Python. Some you may encounter
# * Plotly
# * Bokeh
# * [Seaborn](https://seaborn.pydata.org)
# * **Matplotlib**
# * **Pandas**
# * ggplot (port of R package of same name)
#
# All of these aim to solve the same problem: allowing you to visualize your data.

# + {"hideCode": false, "hidePrompt": false, "cell_type": "markdown"}
# # Appreciating the challenges
#
# A good plotting library should:
#
# * Be easy to use.
# * Allow plotting of all kinds of data.
# * Support arbitrarily fine-grained control.
# * Support a variety of backends to make graphs in various formats.

# + {"hideCode": false, "hidePrompt": false, "cell_type": "markdown"}
# # Matplotlib
#
# While everyone has different opinions about what library is best, everybody knows and has used matplotlib. This makes it the de-facto choice for plotting in python.
#
# ## How does it work?
#
# In an effort to make easy things easy, and hard things possible, matplotlib has a number of different levels at which it can be accessed. They are:
#
# | Level | Control | Complexity |
# |-------|---------|------------|
# | plt | minimal, fast interface for plots, annotations | low |
# | OO interface w/ pyplot | fine-grained control over figure, axes, etc. | medium |
# | pure OO interface | Embed plots in GUI applicatione e.g. | too high |

# + {"hideCode": false, "hidePrompt": false, "cell_type": "markdown"}
# # plt examples
# -

# Here are some numbers to plot.

# + {"hideCode": false, "hidePrompt": false}
x_data = np.arange(0.1, 4, .2)
y_data_1 = np.sin(x_data)
y_data_2 = np.cos(x_data)
y_data_3 = np.exp(x_data)/100
# -

x_data

y_data_1

# `plt.scatter(x, y)` takes an array of horizontal coordinates `x` and an array of vertical coordinates `y` and draws a dot at each specified point in the Cartesian plane.

# + {"hideCode": false, "hidePrompt": false}
plt.scatter(x_data, y_data_1)
plt.title("look at me")
plt.xlabel('x axis')
plt.ylabel('vert')

#plt.show() # uncomment this line if you didn't start the notebook with %matplotlib inline
# -

# Some properties under your control are, for example, color, size, and marker style.
#
# #### [scatter() documentation](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.scatter.html)

plt.scatter(x_data, y_data_1, 
            color='b',
            s=300, 
            marker='*')
plt.title("so pretty")
plt.xlabel('x axis')
plt.ylabel('vert')

# `plt.plot(x,y)` draws a line between each point instead of just drawing points.

plt.plot(x_data, y_data_1)
plt.title("look at me")
plt.xlabel('x axis')
plt.ylabel('vert')

# You can change the color, line thickness, line style (solid, dashed, etc.) and you can even choose to draw the points as well.
#
# #### [plot() documentation](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html)
# #### [Line property documentation](https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D)

plt.plot(x_data, y_data_1, 
         color='k', 
         linestyle='--',
         linewidth=2,
         marker='^', 
         markersize=8)
plt.title("look at me")
plt.xlabel('x axis')
plt.ylabel('vert')

# You can draw multiple plots on the same axes simply by calling the plotting functions multiple times. You can also add labels to each plot and a legend. And you can add text at arbitrary locations with `plt.text()` (and yes, [Latex](https://matplotlib.org/users/usetex.html) is supported!)

# +
plt.scatter(x_data, y_data_1, 
            color='r', label='sin')

plt.scatter(x_data, y_data_2, 
            color='b', marker='*', s=200, label='cos')

plt.plot(x_data, y_data_3, 
         color='k', linewidth=3, linestyle="--", label='growth')

plt.title("award-winning figure")
plt.xlabel('x axis')
plt.ylabel('vert')
plt.legend()

plt.text(0.7, -0.6, 
         "$\infty$ fun", 
         fontsize=19, 
         rotation=13)

plt.savefig('uhh.png') # saving a figure is easy!

# + {"hideCode": false, "hidePrompt": false, "cell_type": "markdown"}
# ## Weird
#
# `plt` was imported as a library, but it appears to be keeping track of some state that gets modified by each plotting function call, behavior that we'd usually associate with objects.
#
# In fact, `plt`, operates in a not-very-pythonic way. But wait, what is [pythonic](https://docs.python-guide.org/writing/style/#general-concepts)???
#
# If you think it's strange that we're working in Python, where "everything is an object", but there doesn't seem to be any objects required to make our image, join the club!

# + {"hideCode": false, "hidePrompt": false, "cell_type": "markdown"}
#
#
# # Behind the curtain
#
# ![Matplotlib diagram](http://matplotlib.org/_images/fig_map.png)
#
#

# + {"hideCode": false, "hidePrompt": false, "cell_type": "markdown"}
# # The OO interface

# + {"hideCode": false, "hidePrompt": false}
# create the figure object
fig = plt.figure() 

# create a single "axes" object
# inside this figure
# more about the "1,1,1" in a moment
ax = fig.add_subplot(1,1,1) 

# plot data on those axes
ax.plot(x_data, y_data_1)

# add a title
ax.set_title('some line')

# add axis labels
ax.set_xlabel('horizontal axis')
ax.set_ylabel('vertical axis')
# -

# In this example, the fact that state is maintained is less surprising.
#
# All the plot style keywords we saw above (color, linewidth, etc.) are the same in `ax.plot()` and `ax.scatter()`.

# + {"hideCode": false, "hidePrompt": false, "cell_type": "markdown"}
# Matplotlib provides a more compact function for initializing a figure & axes: `plt.subplots` (note: different from `plt.subplot`, sorry)

# + {"hideCode": false, "hidePrompt": false}
# this is a shorter way to create 
# a single blank figure & axes
fig, ax = plt.subplots()

ax.plot(x_data,y_data_1)

ax.set_title('some stuff')
ax.set_xlabel('horizontal axis')
ax.set_ylabel('vertical axis')

# let's add another plot on these axes
ax.scatter(x_data, y_data_3, color='b')

# + {"hideCode": false, "hidePrompt": false, "cell_type": "markdown"}
# Why all the reference to "subplots"? Matplotlib is aiming to be as general as possible here. A single figure could contain many axes, and matplotlib asks you to specify the positions of these axes according to a grid.
#
# If unspecified, `plt.subplots()` returns a 1 by 1 grid with a single axes object.
#
# `plt.subplots(n,m)` specifies a grid with `n` rows and `m` columns, with an axes object in each grid square. These axes objects are returned in a numpy array.

# + {"hideCode": false, "hidePrompt": false}
fig, axs = plt.subplots(2,4)

# + {"hideCode": false, "hidePrompt": false}
type(axs)

# + {"hideCode": false, "hidePrompt": false}
axs
# -

axs.shape

axs[0,2]

dum_ax = axs[0,2]

# So to plot on one of those axes, I can index into the array of axes objects, then call all the plotting methods I want

fig, axs = plt.subplots(2,4)
axs[0,2].plot(x_data,y_data_2)

# Ugly overlapping text can be fixed with `plt.tight_layout()`, and figure size can be controlled with the `figsize` keyword of `plt.subplots()`.

# +
fig, axs = plt.subplots(2,4, figsize=(10,4))

axs[0,2].plot(x_data,y_data_2)
axs[0,2].set_title('cool')

plt.tight_layout()
# -

# Note that I used `ax` to name a single axes object and `axs` to name an array of axes objects. This is a useful distinction.

# ### Iterating over axes in a subplot

# + {"hideCode": false, "hidePrompt": false, "cell_type": "markdown"}
# Making a big grid of axes and manually indexing into each one to make a plot sounds terrible. Let's loop over this collection of axes instead.
#
# We can't just type `for ax in axs`, however, because iterating over an `n` by `m` numpy array returns one _row_ at a time and NOT one _element_ at a time. So instead we use the `.flatten()` method to squish a numpy array into a one-dimensional array of its elements.
# -

foo = np.random.randint(60, size=(4,3))

foo

for thing in foo:
    print(len(thing))

foo.flatten()

foo.shape

foo.flatten().shape

for thing in foo.flatten():
    print(thing**2)

axs.shape

axs

axs.flatten()

axs.flatten().shape

# +
fig, axs = plt.subplots(2,4, figsize=(10,4))

for i, ax in enumerate(axs.flatten()):
    ax.scatter(x_data,y_data_3)
    ax.set_title('Plot number {}'.format(i))

plt.tight_layout()
# -

type(axs.flatten())

# ## What about the lines being drawn? Are those objects, too?
# Yes. `ax.plot()` creates the line object and returns it as well as drawing it.

# +
fig, ax = plt.subplots()

plot1_stuff = ax.plot(x_data,y_data_1)

ax.set_title('some stuff')
ax.set_xlabel('horizontal axis')
ax.set_ylabel('vertical axis')

plot2_stuff = ax.scatter(x_data, y_data_3, color='b')
# -

plot1_stuff

type(plot1_stuff)

plot1_stuff[0]

line1 = plot1_stuff[0]

line1.get_c()

# +
# experiment here!

# + {"hideCode": false, "hidePrompt": false, "cell_type": "markdown"}
# # Mix 'n' Match
#
# Turns out, you can combine `plt` and object-oriented approach. Sound confusing? It is. You should avoid it if you can. 

# + {"hideCode": false, "hidePrompt": false}
fig = plt.figure()

ax1 = fig.add_subplot(1,2,1)
plt.title('sin(x) and cos(x)')

ax2 = fig.add_subplot(1,2,2)
plt.title('straight line')

ax1_stuff = ax1.plot(x_data, y_data_1, color='m', alpha=.25)

ax1.plot(x_data, y_data_2)

# ax1_stuff[0].set_alpha(.25) # alternative to using the alpha keyword when calling ax.plot

ax2.plot(x_data, x_data)

line = ax1_stuff[0]
line.set_alpha(.55)

fig.suptitle('wowoowowow', fontsize=44, y=1.1)
fig.tight_layout()

# + {"hideCode": false, "hidePrompt": false, "cell_type": "markdown"}
# # Why should we use the OO oriented approach?
#
# The "functional" `plt` interface is fine for simple plots.
#
# However, as soon as you want fine-grained control over each aspect of your figure (especially if it has more than one set of axes), you will find the OO interface vastly less frustrating. 

# + {"hideCode": false, "hidePrompt": false, "cell_type": "markdown"}
# # More about subplots
# -

# `plt.subplots(n, m)` creates an `n` by `m` grid with an axes object in each grid box.
#
# What if you want to add a single set of axes in an arbitrary location over your figure?
#
# `plt.add_subplot(p, q, i)` creates a single axes object at box `i` of a `p` by `q` grid. 
#
# This gives you a lot of control over possible figure layouts. Here's an example.

# + {"hideCode": false, "hidePrompt": false}
# start with a 2 by 2 grid
fig, axs = plt.subplots(2, 2)

# let's plot a different function in each box

y_funcs = [np.sin, np.cos, np.sqrt, lambda x: x]

for ax, y_func in zip(axs.flatten(), y_funcs):
    ax.scatter(x_data, y_func(x_data))
    
fig.suptitle('some curves');

# + {"hideCode": false, "hidePrompt": false}
# start with a 2 by 2 grid
fig, axs = plt.subplots(2, 2)

# let's plot a different function in each box

y_funcs = [np.sin, np.cos, np.sqrt, lambda x: x]
for ax, y_func in zip(axs.flatten(), y_funcs):
    ax.plot(x_data, y_func(x_data))
    
fig.suptitle('some curves')

# now let's add a small plot in the center
# imagine overlaying a 3 by 3 grid on the figure
# if call the upper left square #1, then the 
# center square would be #5
ax_center = fig.add_subplot(3, 3, 5)

ax_center.plot(x_data, np.log(x_data))

ax_center.set_title('what');
# -

fig.axes

plt.gcf()

# + {"hideCode": false, "hidePrompt": false}
ax_center.set_title('hoo yeah')
# -

fig

# + {"hideCode": false, "hidePrompt": false, "cell_type": "markdown"}
# # What about pandas?
# -

# Pandas has its own convenient methods for hooking into matplotlib.

# + {"hideCode": false, "hidePrompt": false}
import pandas as pd

# + {"hideCode": false, "hidePrompt": false}
df = pd.DataFrame({'x':x_data, \
                   'sinx':np.sin(x_data),\
                   'cosx':np.cos(x_data),\
                   'rand':np.random.rand(len(x_data))})
df = df.set_index('x')
df.head()

# + {"hideCode": false, "hidePrompt": false}
# df.plot?

# + {"hideCode": false, "hidePrompt": false}
df['cosx'].head()

# + {"hideCode": false, "hidePrompt": false}
df['cosx'].plot();

# + {"hideCode": false, "hidePrompt": false, "cell_type": "markdown"}
# Calling the plot method on a pandas series returns a familiar matplotlib axes object, which we can continue to modify.

# + {"hideCode": false, "hidePrompt": false}
ax1 = df['cosx'].plot()
ax1.set_title('sin(x) & cos(x)');
# -

# We can also pass an axes object to the `.plot()` method, meaning we have full control over where the plot ends up.

ax1 = df['cosx'].plot()
ax1.set_title('sin(x) & cos(x)')
df['sinx'].plot(ax=ax1);

# Quite useful in subplots.

# + {"hideCode": false, "hidePrompt": false}
fig, ax_list = plt.subplots(3,1, figsize=(10,10))

cols = df.columns
for ax, col in zip(ax_list.flatten(), cols):
    df[col].plot(ax=ax)
    ax.legend()
    
top_ax = ax_list[0]
top_ax.set_ylim(bottom=-2, top=2);

# + {"hideCode": false, "hidePrompt": false}
ax_list.flatten().shape

# + {"hideCode": false, "hidePrompt": false, "cell_type": "markdown"}
# ## Cool pandas plotting methods

# + {"hideCode": false, "hidePrompt": false}
df = pd.read_csv('data/winequality-red.csv', sep=';')

# + {"hideCode": false, "hidePrompt": false}
df.head()

# + {"hideCode": false, "hidePrompt": false}
df['alcohol'].hist(figsize=(8,6), bins=20);

# + {"hideCode": false, "hidePrompt": false}
df.hist(figsize=(12,12), bins=20);

# + {"hideCode": false, "hidePrompt": false, "cell_type": "markdown"}
# There's a lot going on behind the scenes in that one command. Here's how we would write it the long way:

# + {"hideCode": false, "hidePrompt": false}
fig, axes = plt.subplots(4,3, figsize=(12,12))
for cell_ax, col in zip(axes.flatten(), df.columns):
    df[col].hist(ax=cell_ax)
    cell_ax.set_title(col)
fig.tight_layout() 

# + {"hideCode": false, "hidePrompt": false}
axes

# + {"hideCode": false, "hidePrompt": false}
df.plot.scatter('pH', 'alcohol');

# -

df.head()

df['quality'].value_counts()

# + {"hideCode": false, "hidePrompt": false}
mask = (df['quality'] == 5)

# + {"hideCode": false, "hidePrompt": false}
mask.head()

# + {"hideCode": false, "hidePrompt": false}
(~mask).head()

# + {"hideCode": false, "hidePrompt": false}
df[mask].head()
# -

df[~mask].head()

# + {"hideCode": false, "hidePrompt": false}
ax = df[mask].plot.scatter('pH', 'alcohol', color='b', alpha=0.1)
df[~mask].plot.scatter('pH', 'alcohol', color='r', alpha=0.1, ax=ax);

# + {"hideCode": false, "hidePrompt": false}
pd.plotting.scatter_matrix(df.iloc[:,:5], figsize=(12,12));

# + {"hideCode": false, "hidePrompt": false}
pd.plotting.scatter_matrix(df, figsize=(12,12));


# + {"hideCode": false, "hidePrompt": false, "cell_type": "markdown"}
# # Writing plotting functions

# + {"hideCode": false, "hidePrompt": false, "cell_type": "markdown"}
# ## Quick tip: passing arbitrary numbers of arguments & keyword arguments

# + {"hideCode": false, "hidePrompt": false}
def our_own(*args, **kwargs):
    print(args)
    print(kwargs)
our_own(1,2,3, one=1, two=2)

# + {"hideCode": false, "hidePrompt": false, "cell_type": "markdown"}
# ## another quick reminder: unpacking
# [more on unpacking](https://www.python.org/dev/peps/pep-0448/)

# + {"hideCode": false, "hidePrompt": false}
data = (x_data, y_data_1)
plt.plot(*data)


# + {"hideCode": false, "hidePrompt": false}
def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph

    Parameters
    ----------
    ax : Axes
        The axes to draw to

    data1 : array
       The x data

    data2 : array
       The y data

    param_dict : dict
       Dictionary of kwargs to pass to ax.plot

    Returns
    -------
    out : list
        list of artists added
    """
    out = ax.plot(data1, data2, **param_dict)
    return out


# + {"hideCode": false, "hidePrompt": false}
fig, ax = plt.subplots()
out = my_plotter(ax, x_data, y_data_1, {'linewidth':3, 'linestyle':'-.'})

# + {"hideCode": false, "hidePrompt": false}
ax

# + {"hideCode": false, "hidePrompt": false}
out

# + {"hideCode": false, "hidePrompt": false, "cell_type": "markdown"}
# # Example:
# Let's write a function that draws some data, and some horizontal
# lines representing the 25th and 75th percentile.
#
# We'll call it iqr_plot.
#
# ## I do: 
# a function for drawing a horizontal line at some point.
#
# ## We do: 
# write the iqr_plot function.
#
# ## You do: 
# make a 2 by 2 grid of plots using this function.
#

# + {"hideCode": false, "hidePrompt": false}
# plt.hlines?
# -

## I do
fig, ax = plt.subplots()
ax.scatter(x_data, y_data_1)
ax.hlines(0.4, 0, 4);


# + {"hideCode": false, "hidePrompt": false}
## I do
def my_hline(ax, x_data, y_level):
    """
    Plots a horizontal line through the data at y = y_level
    
    Parameters:
        ax (axes object): axes to plot on
        x_data (numpy array): horizontal coordinates of data
        y_level (float): vertical coordinate of the line
        
    Returns:
        out (list): list of artists added        
    """
    ax.hlines(y_level, x_data.min(), x_data.max())


# +
fig, ax = plt.subplots()

ax.scatter(x_data, y_data_1)

my_hline(ax, x_data, 0.44)


# + {"hideCode": false, "hidePrompt": false}
def my_hline2(ax, x_data, y_level):
    out = ax.plot([x_data.min(), x_data.max()], \
                  [y_level, y_level],\
                  color='k',\
                  linestyle=':',\
                  linewidth=5)
    return out


# +
fig, ax = plt.subplots()

ax.scatter(x_data, y_data_1)

my_hline2(ax, x_data, 0.44)
# -

np.percentile(y_data_1, [25,75])

foo, bar = np.percentile(y_data_1, [25,75])

foo

bar


# + {"hideCode": false, "hidePrompt": false}
def iqr_plot(ax, x_data, y_data):
    q25, q75 = np.percentile(y_data, [25,75])
    
    out1 = ax.scatter(x_data, y_data)
    
    out2 = my_hline2(ax, x_data, q25)
    out3 = my_hline2(ax, x_data, q75)
    return [out1] + out2 +out3


# +
fig, ax = plt.subplots()

stuff = iqr_plot(ax, x_data, y_data_1)
# -

stuff

# YOU Do!
# make a 2 by 2 grid of plots using this function `iqr_function`.

# +
#
# -

# ### Different dimensions

np.random.seed(888)
y_4 = np.random.randint(100, size=101)

x_data

x_data.shape

y_4

# + {"tags": ["raises-exception"]}
plt.scatter(x_data, y_4)
# -

y_4 = list(range(20))

len(y_4)

plt.scatter(x_data, y_4)

y_4[11] = None

plt.scatter(x_data, y_4)

# +
# # start with a 2 by 2 grid
# fig, axs = plt.subplots(2, 2)

# # let's plot a different function in each box
# y_funcs = [np.sin, np.cos, np.sqrt, lambda x: x]
# for ax, y_func in zip(axs.flatten(), y_funcs):
#     iqr_function(ax, x_data, y_func(x_data))
#     ax.scatter(x_data, y_func(x_data), alpha=0.2)

# fig.suptitle('some curves')
