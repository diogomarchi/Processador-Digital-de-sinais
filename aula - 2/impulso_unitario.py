import numpy as np
import matplotlib.pyplot as plt

meuVetor = []
n = np.arange(0, 20, 1)
i = 0

for i in n:
    if i > 0:
        meuVetor.append(0)
    else:
        meuVetor.append(1)

plt.plot(n, meuVetor, "o")
plt.grid()
plt.show()