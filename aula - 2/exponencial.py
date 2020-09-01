import numpy as np
import matplotlib.pyplot as plt
import math

t = np.arange(0, 30, 1)

a = 0.5

exp = np.exp2(t)

plt.grid()
plt.stem(t,exp,use_line_collection=True)
plt.show()