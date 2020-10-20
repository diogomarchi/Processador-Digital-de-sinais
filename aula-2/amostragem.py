import numpy  as  np
import  matplotlib . pyplot  as  plt


# Sinal analogico
Dt = 1 / 64
t = np.arange(- 50 * Dt, 50 * Dt, Dt)

# Plota o sinal analógico xa
f  =  60
xa = np.cos(2 * np.pi * f * t)


# Sinal discreto
Fs = 1000
Ts = 1 / Fs
n = np.arange(- 50, 50, 1)
xd = np.cos(2 * np.pi * n * f / Fs )


# Plota
fig = plt.figure(1)

a = fig.add_subplot(2, 1, 1)
a.stem( t, xa)
a.set_xlabel("(a)")

a = fig.add_subplot(2, 1, 2)
plt.stem(t, xd)
a.set_xlabel("(b)")

plt.show ()