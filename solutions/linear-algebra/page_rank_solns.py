import numpy as np
from matplotlib import pyplot as plt


LETTERS = "ABCDE"

# Refer to the diagram in the sprint. Rows are ABCD
trans_mat = np.array([[0, 1, 0, 0, 0],
                      [.5, 0, .5, 0, 0],
                      [1./3, 1./3, 0, 0, 1./3],
                      [1, 0, 0, 0, 0],
                      [0, 1./3, 1./3, 1./3, 0]])

# Equal probability to be at each page
states = np.repeat(1. / len(trans_mat), len(trans_mat))

# Taking one step and getting the probability to be at each state
states.dot(trans_mat)

# Plotting the probability of each page for first 10 steps
fig, ax = plt.subplots(1, figsize=(15, 5))
states = np.repeat(1. / len(trans_mat), len(trans_mat))

for i in range(1, 11):
    ax = plt.subplot(2, 5, i)
    ax.bar(range(5), states)
    ax.set_xticks(np.arange(5) + .5)
    ax.set_xticklabels([ch for ch in LETTERS])
    ax.set_ylim(0, .6)
    ax.set_title("Step " + str(i))
    states = states.dot(trans_mat)

fig.subplots_adjust(hspace=.5)
plt.show()

print('Matrix multiplication solution:', states)
# Eigenvalue solution
print('Eigen values: ', np.linalg.eig(trans_mat.T)[1][:, 0] / np.sum(np.linalg.eig(trans_mat.T)[1][:, 0]))

# B is the most probable
