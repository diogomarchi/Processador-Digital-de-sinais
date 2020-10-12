import numpy as np
import matplotlib.pyplot as plt

def x(t):
    if t == 0:
        i = 1
    else:
        i = 0
    return i

b = np.arange(-3,4,1)
a = []
for n in range(-3, 4, 1):
    a.append(0.282*x(n) + 0.282*x(n-1) + 0.4361*a[n-1])

plt.stem(b, a)
plt.show()
