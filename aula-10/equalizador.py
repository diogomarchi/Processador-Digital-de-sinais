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
fcPB = 600
fcPA = 3000
bw = 200
bwn = bw / fs
fcPB = fcPB / fs
fcPA = fcPA / fs

M = 4 / bwn

#create vector PA
hA = gera_coef(M, fcPA)
hA = - hA
hA[int(M/2)] += 1

#create vector PB
hB = gera_coef(M, fcPB)

# filtro Passa faixa
hPF2 = gera_coef(M, fcPA)        # passa baixa

hPF1 = gera_coef(M, fcPB)        # passa alta
hPF1 = -hPF1
hPF1[int(M/2)] += 1
hPF = np.convolve(hPF1, hPF2)

# ganhos
g_pb = 0.7
g_pf = 0.6
g_pa = 0.5
with open("coefPassaFaixaEq", 'w') as f:
    for d in hPF:
        f.write(str(d.astype(np.float16))+",\n")

with open("coefPassaBaixaEq", 'w') as f:
    for d in hB:
        f.write(str(d.astype(np.float16))+",\n")

with open("coefPassaAltaEq", 'w') as f:
    for d in hA:
        f.write(str(d.astype(np.float16))+",\n")

with open("sweep_20_3600.pcm", 'rb') as f:
    buf = f.read()
    data_i = np.frombuffer(buf, dtype='int16')
    data_len = len(data_i)

    # replica do arquivo lido para salvar o resultado
    data_pb = g_pb * np.convolve(hB, data_i, 'same')
    data_pf = g_pf * np.convolve(hPF, data_i, 'same')
    data_pa = g_pa * np.convolve(hA, data_i, 'same')

    data_o = data_pb + data_pa + data_pf

    data_o = data_o.astype(dtype='int16')


# amostra de 100 ms
t = np.arange(0, data_len/fs, 1 / fs)

###############
#   plot
plt.subplot(2, 1, 1)
plt.plot(t, data_i[: len(t)], "k-", label="Input")
plt.plot(t, data_o[: len(t)], label="Output")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")


print("calculating freqz")
[w1, h1] = freqz(hA, worN=fs, fs=1)
[w2, h2] = freqz(hB, worN=fs, fs=1)
[w3, h3] = freqz(hPF, worN=fs, fs=1)

print("printing freqz")
plt.subplot(2, 1, 2)
plt.plot(w1, abs(h1), label="PA")
plt.plot(w2, abs(h2), label="PB")
plt.plot(w3, abs(h3), label="PF")
plt.legend()
plt.xlabel("Freq")
plt.ylabel("Amplitude")

with open("equalizador.pcm", 'wb') as f:
    for d in data_o:
        f.write(d)

plt.grid()
plt.show()