import numpy as np
# Se o código estiver em um arquivo chamado plot_zplane.py
from zPlane import zplane
b = np.array([1, 1.5, 2])
a = np.array([1, 0, 0])
zeros = np.roots(b)
print(zeros)
zplane (b, a)