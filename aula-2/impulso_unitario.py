import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-10, 10, 1)
nLen = len(n)

meuVetor = np.zeros((nLen, 1), dtype=np.int16)
meuVetor[n == 0] = 1

with open(r'impulsoUnitario.pcm', 'wb') as f:
    for d in meuVetor:
        f.write(d)

plt.stem(n, meuVetor)
plt.grid()
plt.show()