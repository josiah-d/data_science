# starter code
import numpy as np
from sklearn.decomposition import NMF
import matplotlib.pyplot as plt

nut_vals=np.array([[130, 110,  25, 100,  45],
                   [  0,   0,  40, 330,  80],
                   [260, 450, 220, 300, 460],
                   [ 34,  30,   6,   0,   8],
                   [  2,   2,   4,   0,   6],
                   [  8,  15, 190,   4, 220]])
# your code below
err = []
comps = [1, 2, 3, 4]
for i in comps:
    model = NMF(n_components=i, init='random', random_state=0)
    W = model.fit_transform(nut_vals)
    H = model.components_
    re = model.reconstruction_err_
    print("{0} components, reconstruction error {1:0.2f}".format(i, re))
    err.append(re)

plt.plot(comps, err)
plt.show()