import numpy as np
import matplotlib
import matplotlib.pyplot as plt


# Read data
data = np.loadtxt('linear-regression-one-variable-sample-data.txt', delimiter=',')
X = data[0]
Y = data[1]

# Plot data
plt.plot(X, Y, 'rx', markersize=10)
plt.ylabel('Y')
plt.xlabel('X')
matplotlib.pyplot.show()
