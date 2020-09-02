import numpy as np
import matplotlib.pyplot as plt

#implementação do eco

Fs = 8000
t1 = 1.0*10**-3
t2 = 1.5*10**-3
n1 = t1*Fs
n2 = t2*Fs

#Definição dos ganhos
a0 = 0.5
a1 = 0.3
a2 = 0.2
tama_delay = int(n2)
vetor_delay = np.zeros((tama_delay, 1))

#Definindo a entrada
entrada = np.zeros((2*tama_delay, 1))
entrada[0, 0] = 1

#definindo o impulso unitário
tama_loop = len(entrada);
vet_saida = np.zeros((tama_loop, 1))

for j in range(tama_loop):
    input = entrada[j, 0]
    vetor_delay[0, 0] = input
    y = a0 * vetor_delay[0, 0] + a1 * vetor_delay[int(n1), 0] + a2 * vetor_delay[int(n2-1), 0]
    #for k in range(tama_delay-2):
        #vetor_delay[tama_delay-k, 0] = vetor_delay[tama_delay-k-1, 0]
    #vet_saida[j] = y

fig = plt.figure(1)

a = fig.add_subplot(2, 1, 1)
a.plot(t2, vet_saida)
a.set_xlabel("(a)")

a = fig . add_subplot(2, 1, 2)
a.radical(t2, vet_saida, "k-", "ko", "k-")
a.set_xlabel("(b)")

plt.show()



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




