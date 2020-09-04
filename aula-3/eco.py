import numpy as np
import matplotlib.pyplot as plt

#implementação do eco

Fs = 8000
Ts = 1 / Fs;
t1 = 1.0*10**-3
t2 = 1.5*10**-3
L = 0.1 * Fs
n1 = t1*Fs
n2 = t2*Fs

#Definição dos ganhos
a0 = 0.5
a1 = 0.3
a2 = 0.2

#Definindo a entrada

with open('C:/Users/Diogo/Documents/FACULDADE-MATERIAS/Processador-Digital-de-sinais/aula-1/alo.pcm', 'rb') as f:
    buf = f.read()
    data_i = np.frombuffer(buf, dtype='int16')
    data_len = len(data_i)

    entrada = np.zeros_like(data_i)

    for i in range(data_len):
        entrada[i] = data_i[i]
    #f.close(buf)


tama_loop = len(entrada);
vet_saida = np.zeros((tama_loop, 1))
vetor_amostra = np.zeros((int(L), 1))

for j in range(tama_loop):
    vetor_amostra[0] = entrada[j];
    y = a0 * vetor_amostra[0] + a1 * vetor_amostra[int(n1-1)] + a2 * vetor_amostra[int(n2-1)]
    vet_saida[j] = y

    for k in range(int(L)):
        vetor_amostra[int(L)-k-1] = vetor_amostra[int(L)-k-2]

plt.stem(vet_saida)
plt.title('delay teste')
plt.show()

with open('saidaEco.pcm', 'wb') as f:
    for d in vet_saida:
        f.write(d)












