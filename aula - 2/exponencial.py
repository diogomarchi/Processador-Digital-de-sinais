import numpy as np
import matplotlib.pyplot as plt
import math

t = np.arange(0, 30, 1)
#Aa^n
A = 1
a = 0.5

exp = A*a**t

plt.plot(t, exp, "o")
plt.grid()
plt.show()