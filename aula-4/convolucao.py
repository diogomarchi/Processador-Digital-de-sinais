import numpy as np
import matplotlib.pyplot as plt

h = [1, 0.5, 0.25, 0.125]
#h = [0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125]

x = [1, 1, 1, 1, 1, 1, 1, 1,1,1]
#x = [1, 0, 0, 0, 0, 0]

m = np.convolve(x, h)


plt.stem(m)
plt.xlabel("n")
plt.ylabel("x[n]")
plt.show()
