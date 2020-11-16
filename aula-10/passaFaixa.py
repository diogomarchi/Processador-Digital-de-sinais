 # 'LOW-PASS WINDOWED-SINC FILTER
 #'This program filters 5000 samples with a 101 point windowed-sinc filter,
 #resulting in 4900 samples of filtered data.
 #
import numpy as np
from scipy.signal import freqz
import matplotlib.pyplot as plt

def gera_coef(M, fc):
    h = np.zeros(int(M))
    tam = len(h)
    for i in range(tam):
        if (i - M / 2) == 0:
            h[i] = 2 * np.pi * fc

        else:
            h[i] = np.sin(2 * np.pi * fc * (i - M / 2)) / (i - M / 2)

        h[i] = h[i] * (0.54 - 0.46 * np.cos(2 * np.pi * i / M))

    # normalize
    h = h / np.sum(h)

    return h

fs = 8000
fc1 = 400
fc2 = 800
bw = 200
bwn = bw / fs
fc1 = fc1 / fs
fc2 = fc2 / fs

M = 4 / bwn

#create vector PA
hA = gera_coef(M, fc1)
hA = - hA
hA[int(M/2)] += 1

#create vector PB
hB = gera_coef(M, fc2)


hFaixa = np.zeros(int(M))
#rejeita faixa
for i in (range(len(hFaixa))):
    hFaixa[i] = hA[i] + hB[i]

#inversao espectral para fazer passa faixa
hFaixa = - hFaixa
hFaixa[int(M/2)] = hFaixa[int(M/2)] + 1


with open("sweep_20_3600.pcm", 'rb') as f:
    buf = f.read()
    data_i = np.frombuffer(buf, dtype='int16')
    data_len = len(data_i)

    # replica do arquivo lido para salvar o resultado
    data_o = np.convolve(hFaixa, data_i)
    data_o = data_o.astype(dtype='int16')


# amostra de 100 ms
t = np.arange(0, data_len/fs, 1 / fs)

#   plot
plt.subplot(2, 1, 1)
plt.plot(t, data_i[: len(t)], "k-", "ko", label="Input")
plt.plot(t, data_o[: len(t)], label="Output")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

# amostra de 100 ms
t = np.arange(0, data_len/fs, 1 / fs)


[w, x] = freqz(hFaixa, worN=fs, fs=1)

plt.subplot(2, 1, 2)
plt.plot(w, abs(x), label="Passa faixa")
plt.legend()
plt.xlabel("Freq")
plt.ylabel("Amplitude")
plt.grid()
plt.show()


#salvando em arquivo
file_name = "passaFaixa.pcm"
with open(file_name, 'wb') as f:
    for d in data_o:
        f.write(d)


