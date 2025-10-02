# Claudino José Martins - 127368

import matplotlib.pyplot as plt
import numpy as np

vi = 0 # velocidade inicial do corpo m/s
dt = 0.01 #n passos
vt = 24.5 #velocidade terminal
g = -9.8 #aceleração gravítica

T = np.arange(0,100, dt)
v = np.zeros(T.size)
y = np.zeros(T.size)

v[0] = 0
y[0] = 30

y1 = 30 + 0*T + 0.5*g*T**2 #Valor Teorico

floor = np.zeros(T.size)

#Metodo de Euler
for i in range(0, T.size-1):
    if T[i] == 10:
        vt = 5.0
    D = -g/(vt**2)  
    v[i+1] = v[i] + (g-D*v[i]*abs(v[i]))*dt # velocidade no instante
    y[i+1] = y[i] + v[i] * dt # posiçao no instante
    if y[i+1]>0 and y[i+1]<0.5:
        print(i+1)

#268 é o ultimo valor printado ou seja o valor de t mais proximo do momento y=0
print("Velocidade: ", abs(v[268]))
# Velocidade: 19.37827734930491
print("Posição da Bola: ", T[268])
# Posição da Bola: 2.68

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.set_xlabel('tempo (s)')
ax.set_ylabel('Y (m)')
ax.plot(T, floor, label="Y = 0")
ax.plot(T, y, label="Metodo de Euler")
#ax.plot(T, y1, label="Exato")

plt.legend()
plt.show()