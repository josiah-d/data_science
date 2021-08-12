import matplotlib.pyplot as plt
import numpy as np

x_data = np.arange(0, 4, .011)
y_data = np.sin(x_data)

plt.plot(x_data, y_data)
plt.title('using plt')

plt.show()
