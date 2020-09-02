import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-20, 20, 1)


f = 100
Fs = 8000

sen = np.sin(2 * np.pi * n * (f / Fs))

with open(r'sinusoidal.pcm', 'wb') as f:
    for d in sen:
        f.write(d.astype(np.int16))


plt.stem(n, sen)
plt.grid()
plt.show()