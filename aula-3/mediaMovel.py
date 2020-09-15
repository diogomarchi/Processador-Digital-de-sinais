import numpy as np
import matplotlib.pyplot as plt

sample_rate = 8000
k = 8
media_buf = np.zeros(k)

with open("sweep_20_3600.pcm", 'rb') as f:
    buf = f.read()                              ##le arquivo
    data_i = np.frombuffer(buf, dtype='int16')  #coloca arquivo lido no vetor
    data_len = len(data_i)                      #pega o tamanho do vetor

    data_o = np.zeros_like(data_i)              #cria um vetor zerado fo tamanho da entradaa

    for i in range(data_len):                   #for de posicao do vetor para fazer a media
        media_buf[0] = data_i[i]                #primeira posicao do vetor media, coloca a posicao atual do vetor de entrada
        m = np.sum(media_buf)/k         #soma tudo e divide pelo tamanho
        data_o[i] = m                           #coloca a media na posição do vetor
        buf = media_buf[0:k-1]          #desloca
        media_buf[1:k] = buf            #descloca

# amostra de 100 ms
t = np.arange(0, 0.1, 1 / sample_rate)

###############
#   plot
plt.stem(t, data_i[: len(t)], "k-", "ko", "k-", label="Input")
plt.plot(t, data_o[: len(t)], label="Output")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()


file_name = "media_"+str(k)+"_resultado_sweep.pcm"
with open(file_name, 'wb') as f:
    for d in data_o:
        f.write(d)