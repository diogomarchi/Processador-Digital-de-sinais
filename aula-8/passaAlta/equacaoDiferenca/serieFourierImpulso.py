import numpy as np
import matplotlib.pyplot as plt

def i(t):
    if t == 0:
        i = 1
    else:
        i = 0
    return i

b = np.arange(-3,4,1)
a = []
for n in range(-3, 4, 1):
    a.append(i(n+1) + i(n) + i(n-1))

plt.stem(b, a)
plt.show()
