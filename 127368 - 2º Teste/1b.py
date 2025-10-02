# Claudino José Martins - 127368

import matplotlib.pyplot as plt
import numpy as np

GM = 4 * np.pi**2  
x0 = 1             
y0 = 0             
vx0 = 0            
vy0 = 2            
dt = 0.001         
anos = 3           
n = int(anos / dt)

x = np.zeros(n+1)
y = np.zeros(n+1)
vx = np.zeros(n+1)
vy = np.zeros(n+1)

x[0] = x0
y[0] = y0
vx[0] = vx0
vy[0] = vy0

for i in range(n):
    r = np.sqrt(x[i]**2 + y[i]**2)
    ax = -GM * x[i] / r**3
    ay = -GM * y[i] / r**3
    vx[i+1] = vx[i] + ax * dt
    vy[i+1] = vy[i] + ay * dt
    x[i+1] = x[i] + vx[i+1] * dt
    y[i+1] = y[i] + vy[i+1] * dt

G = GM
M = 1
m = 1

Ep = np.zeros(n+1)
Ec = np.zeros(n+1)
E_total = np.zeros(n+1)

for i in range(n+1):
    r = np.sqrt(x[i]**2 + y[i]**2)
    Ep[i] = -G * m * M / r
    Ec[i] = 0.5 * m * (vx[i]**2 + vy[i]**2)
    E_total[i] = Ep[i] + Ec[i]

plt.figure(figsize=(10,6))
plt.plot(np.arange(n+1)*dt, Ep, label="Energia Potencial")
plt.plot(np.arange(n+1)*dt, Ec, label="Energia Cinética")
plt.plot(np.arange(n+1)*dt, E_total, label="Energia Total")
plt.xlabel("Tempo (anos)")
plt.ylabel("Energia (UA^2/ANO^2)")
plt.title("Energias ao longo do tempo na órbita da Terra")
plt.legend()
plt.grid()
plt.show()

# Comentário dos resultados:

# O gráfico mostra que a Ep e a Ec variam, mas a energia total mantém-se praticamente constante. 
# Logo, verificamos a conservação da energia mecânica no movimento orbital da Terra em torno do Sol.