import numpy as np
import matplotlib.pyplot as plt

sample_rate = 8000

n = np.arange(-10, 10, 1/sample_rate)
nLen = len(n)

meuVetor = np.zeros((nLen, 1), dtype=np.int16)
meuVetor[n > 0] = 1

with open(r'degrauUnitario.pcm', 'wb') as f:
    for d in meuVetor:
        f.write(d)

plt.stem(n, meuVetor)
plt.grid()
plt.show()
