import numpy as np
import matplotlib.pyplot as plt

#implementação do eco

Fs = 8000
Ts = 1 / Fs;
t1 = 1.0*10**-1
t2 = 1.5*10**-1
L = 1 * Fs
n1 = t1*Fs
n2 = t2*Fs

#Definição dos ganhos
a0 = 0.5
a1 = 0.3
a2 = 0.2

#Definindo a entrada

with open('C:/Users/Diogo/Documents/FACULDADE-MATERIAS/Processador-Digital-de-sinais/aula-1/teste_audio.pcm', 'rb') as f:
    buf = f.read()                              #le arquivo
    data_i = np.frombuffer(buf, dtype='int16')  #coloca na variavel, o arquivo lido(buffer)
    data_len = len(data_i)                      #pega o tamanho do vetor

    entrada = np.zeros_like(data_i)             #cria vetor de entrada

    for i in range(data_len):                   #for para vetor pegar os dados
        entrada[i] = data_i[i]                  #atribui valor ao vetor
    f.close()                                   #fecha arquivo


tama_loop = len(entrada);                       #tamanho do vetor de entrada
vet_saida = np.zeros((tama_loop, 1))            #cria vetor de saida do tamanho do vetor de entrada
vetor_amostra = np.zeros((int(L), 1))           #cria vetor de amostra com o tamanho especificado(8000)

for j in range(tama_loop):
            vetor_amostra[0] = entrada[j];                           #primeira posicao do vetor de amostra recebe o valor da posicao de entrada
            y = a0 * vetor_amostra[0] + a1 * vetor_amostra[int(n1-1)] + a2 * vetor_amostra[int(n2-1)]  #faz as repetições
            vet_saida[j] = y                                         #colocando as repetições no vetor de saida
        
            vetor_amostra[1:int(n2)] = vetor_amostra[0:int(n2)-1]    #deslocamento

plt.stem(vet_saida)                                          #plota o vetor de saida
plt.title('delay teste')
plt.show()

with open('saidaEco.pcm', 'wb') as f:
    for d in vet_saida:
        f.write(d.astype(np.int16))












