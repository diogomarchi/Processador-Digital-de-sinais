import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz


with open("wn.pcm", 'rb') as f:
    buf = f.read()
    x = np.frombuffer(buf, dtype='int16')
    data_len = len(x)


with open("passaBaixa.pcm", 'rb') as f:
    buf = f.read()
    w = np.frombuffer(buf, dtype='int16')
    data_len = len(w)

#mi
numero = 10*np.exp(-6)

#sistema desconhecido
sd = [0.6, 0.5, 0.4, 0.3, 0.2]

#saida desejada
d = np.convolve(x, sd)

#filtragem
y = np.convolve(x, w, 'same')

#estimacao do erro
e = d - y

#adaptacao do vetor de erro
for i in range(w):
    w[i+1] = w[i] + 2 *numero* e[i] * x[i]

# amostra de 100 ms
t = np.arange(0, len(x)/6000, 1 / sample_rate)

###############
#   plot
plt.subplot(2, 1, 1)
plt.plot(t, w[: len(t)], "k-", "ko", "k-", label="passa baixa")
plt.plot(t, e[: len(t)], label="erro")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

plt.show()
