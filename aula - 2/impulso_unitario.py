import numpy as np
import matplotlib.pyplot as plt

meuVetor = []
n = np.arange(-10, 10, 1)
i = 0

for i in n:
    if i == 0:
        meuVetor.append(1)
    else:
        meuVetor.append(0)


# impulso
#sig_imp  =  np . zeros (( sample_rate , 1 ))
#sig_imp [ t  ==  0 ] =  1

plt.stem(n, meuVetor)
plt.grid()
plt.show()