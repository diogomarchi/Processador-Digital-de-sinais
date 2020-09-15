import numpy as np
import matplotlib.pyplot as plt

vet = [1, 0.5, 0.25, 0.125]

x = [1, 1, 1, 1, 1, 1]
'''
with open("degrauUnitario.pcm", 'rb') as f:
    buf = f.read()                              ##le arquivo
    data_i = np.frombuffer(buf, dtype='int16')  #coloca arquivo lido no vetor
    data_len = len(data_i)                      #pega o tamanho do vetor

    data_o = np.zeros_like(data_i)              #cria um vetor zerado fo tamanho da entradaa

    #for i in range(data_len):                   #for de posicao do vetor para fazer a media
     #   media_buf[0] = data_i[i]                #primeira posicao do vetor media, coloca a posicao atual do vetor de entrada
'''
m = np.convolve(x, vet)


plt.stem(m)
plt.xlabel("n")
plt.ylabel("x[n]")
plt.show()
