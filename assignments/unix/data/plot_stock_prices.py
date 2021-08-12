import sys
import matplotlib.pyplot as plt

vals = [float(line.split(',')[7]) for line in sys.stdin]

plt.plot(vals)
plt.title('Stock Price Data')
plt.ylabel('Adjusted Closing Price')
plt.xlabel('Trading Day')
plt.show()
