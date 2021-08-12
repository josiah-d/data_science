import numpy as np

# Find the state of land use in 2009 and 2014,
# assuming that the transition probabilities for 5-year
# intervals are given by the matrix A and remain
# practically the same over the time considered.

stoch_mat = np.array([[0.7, 0.1, 0], [0.2, 0.9, 0.2], [0.1, 0, 0.8]])
# array([[ 0.7,  0.1,  0. ],
#        [ 0.2,  0.9,  0.2],
#        [ 0.1,  0. ,  0.8]])

use_2004 = np.array([0.25, 0.2, 0.55])
use_2009 = stoch_mat.dot(use_2004)
use_2014 = stoch_mat.dot(use_2009)

# we do it this way because we want to multiply one row from the stochastic
# matrix by the current usage vector to get a new vector of the form
# [new_C, new_I, new_R]

# use_2004 array([ 0.25,  0.2 ,  0.55])
# use_2009 array([ 0.195,  0.34 ,  0.465])
# use_2014 array([ 0.1705,  0.438 ,  0.3915])
