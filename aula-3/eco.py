import numpy as np
import matplotlib.pyplot as plt

#implementação do eco

Fs = 8000
t1 = 8.0*10**-3
t2 = 10.5*10**-3
n1 = t1*Fs
n2 = t2*Fs

#Definição dos ganhos
a0 = 0.5
a1 = 0.3
a2 = 0.2
tama_delay = int(n2)
vetor_delay = np.zeros((tama_delay, 1))

#Definindo a entrada

with open('C:/Users/Diogo/Documents/FACULDADE-MATERIAS/Processador-Digital-de-sinais/aula-1/teste_audio.pcm', 'rb') as f:
    buf = f.read()
    data_i = np.frombuffer(buf, dtype='int16')
    data_len = len(data_i)

    entrada = np.zeros_like(data_i)

    for i in range(data_len):
        entrada[i] = data_i[i]


tama_loop = len(entrada);
vet_saida = np.zeros((tama_loop, 1))

for j in range(tama_loop):
    input = entrada[j]
    vetor_delay[0, 0] = input
    y = a0 * vetor_delay[0, 0] + a1 * vetor_delay[int(n1-1), 0] + a2 * vetor_delay[int(n2-1), 0]
    vet_saida[j, 0] = y
    for k in range(tama_delay-2):
        vetor_delay[tama_delay-k-1, 0] = vetor_delay[tama_delay-k-2, 0]

plt.stem(vet_saida)
plt.title('delay teste')
plt.show()

with open('saidaEcoWalter.pcm', 'wb') as f:
    for d in vet_saida:
        f.write(d.astype(np.int16))

'''
if __name__ == "__main__":
    plt.close('all')
    print("Selecione uma das seguintes opções: ")
    option = input("'D': Degrau Unitario \n'I': Impulso Unitario \n'S': Sequencia Sinusoidal \n'E': Sequencia Exponencial\n\n")
    if option == 'D' : degrau_unitario()
    elif option == 'I': impulso_unitario()
    elif option == 'S': sinusoidal()
    elif option == 'E': exponencial()
    else:
        exit()
'''




