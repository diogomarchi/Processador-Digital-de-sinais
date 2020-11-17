 # 'LOW-PASS WINDOWED-SINC FILTER
 #'This program filters 5000 samples with a 101 point windowed-sinc filter,
 #resulting in 4900 samples of filtered data.
 #
import numpy as np
from scipy.signal import freqz
import matplotlib.pyplot as plt

fs = 8000
fc = 400
bw = 200
bwn = bw / fs
fcn = fc / fs

M = 4 / bwn

#create vector
h = np.zeros(int(M))
tam = len(h)

#Calculate the low-pass filter kernel via Eq. 16-4
for i in range(tam):
    if (i - M/2) == 0:
         h[i] = 2*np.pi*fcn

    else:
         h[i] = np.sin(2*np.pi*fcn * (i-M/2)) / (i-M/2)

    h[i] = h[i] * (0.54 - 0.46*np.cos(2*np.pi*i/M))

#Normalize the low-pass filter kernel for
soma = 0
for i in range(tam): #'unity gain at DC
    soma = soma + h[i]

#garantindo que os valores estao entre 0 e 1
for i in range(tam):
    h[i] = h[i] / soma

with open("sweep_20_3600.pcm", 'rb') as f:
    buf = f.read()
    data_i = np.frombuffer(buf, dtype='int16')
    data_len = len(data_i)

    # replica do arquivo lido para salvar o resultado
    data_o = np.convolve(h, data_i, 'same')
    data_o = data_o.astype(dtype='int16')


[w, x] = freqz(h, worN=fs, fs=1)

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

plt.subplot(2, 1, 2)
plt.plot(w, 20 * np.log10(abs(x)), label="resposta em frequencia")
plt.legend()

plt.show()


#salvando em arquivo
file_name = "passaBaixaCoef.dat"
with open(file_name, 'w') as f:
    for d in h:
        f.write(str(d.astype(np.float16))+",\n")

with open("passaBaixaPCM.pcm", 'wb') as f:
    for d in data_o:
        f.write(d)


