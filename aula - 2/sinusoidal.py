import numpy as np
import matplotlib.pyplot as plt

meuVetor = []
n = np.arange(-20, 20, 1)


f = 100
Fs = 8000

sen = np.sin(2 * np.pi * n * (f / Fs))


plt.stem(n, sen)
plt.grid()
plt.show()