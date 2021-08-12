'''
Problems:
1. Make a scatter plot of sepal width vs sepal length
2. Compute the mean vector (column-wise) of the data matrix. The shape of the mean vector should be (1, 2)
   Plot the mean vector on the scatter plot in 1.
3. Write a function (euclidean_dist) to calculate the
   euclidean distance between two column vectors (not row vector).
   Your function should check if the vectors are column vectors
   and the shape of the two vectors are the same.
4. Write a function (cosine_sim) to calculate the cosine
   similarity_between two column vectors (not row vector).
5. Write a function that would loop through all the data
   points in a given matrix and calculate the given
   distance metric between each of the data point and the
   mean vector. A for loop is allowed here.
6. Plot histograms of the euclidean distances and
   cosine similarities.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Read into pandas dataframe
iris = pd.read_csv('data/iris.txt')
data = iris[['SepalWidth', 'SepalLength']].values


# 2. Plot scatter plot with mean vector
width = data[:, :1]
length = data[:, 1:]
print(length.shape)
print(width.shape)

fig, ax = plt.subplots()
ax.scatter(width, length, alpha=.5, edgecolor='none')
ax.set_xlabel('Sepal Width', fontsize=14)
ax.set_ylabel('Sepal Length', fontsize=14)

means = np.mean(data, axis=0, keepdims=True)
ax.scatter(means[:, :1], means[:, 1:], marker='x', s=300, c='r', alpha=.3, linewidths=5)
plt.show()


# 3. check centered data
print((data-means).shape)

# 4. Plot histogram of Euclidean distances

# Write functions to check if inputs are column vectors
# of the same size.
def is_column_vector(v):
    return len(v.shape) == 2 and v.shape[1] == 1

def is_same_shape(v1, v2):
   return v1.shape == v2.shape

def check_args(v1, v2):
    if not is_same_shape(v1, v2):
        raise ValueError("Inputs not the same size")
    if not is_column_vector(v1):
        raise ValueError("Not a column vector")

# Compute Euclidean distance function
def euclidean_distance(vec1, vec2):
    check_args(vec1, vec2)
    diff = (vec1 - vec2)
    return np.sqrt(diff.T.dot(diff))

def arr_loop(data, func, row_wise=True):
    if not row_wise:
        data = data.T
    means_row_vec = np.mean(data, axis=0, keepdims=True)
    result_arr = np.array([])
    for row_vec in data:
        col_vec = row_vec[:, np.newaxis]
        means_col_vec = means_row_vec.T
        dist = func(col_vec, means_col_vec)
        result_arr = np.append(result_arr, dist)
    return result_arr

dist_lst = arr_loop(data, euclidean_distance)

fig, ax = plt.subplots()
ax.hist(dist_lst, bins=20, edgecolor='none', density=1)
ax.set_ylabel('Probability Density', fontsize=14)
ax.set_xlabel('Euclidean Distance', fontsize=14)
plt.show()

# 5. Plot histogram of Cosine similarities
def cosine_similarity(vec1, vec2):
    check_args(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    norm_prod = norm1 * norm2

    return vec1.T.dot(vec2) / norm_prod

fig, ax = plt.subplots()
cos_lst = arr_loop(data, cosine_similarity)
ax.hist(cos_lst, bins=20, edgecolor='none', density=1)
plt.show()
