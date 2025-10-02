# Claudino José Martins - 127368

import numpy as np
import matplotlib.pyplot as plt

GM = 4 * np.pi**2  
x0 = 1             
y0 = 0             
vx0 = 0            
vy0 = 2
dt = 0.001         

anos = 3
n = int(anos / dt)

t = np.zeros(n+1)
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

plt.figure(figsize=(8, 8))
plt.plot(x, y, label="Trajetória da Terra")
plt.scatter(0, 0, color="orange", label="Sol", s=100)
plt.xlabel("x (UA)")
plt.ylabel("y (UA)")
plt.title("Órbita da Terra em torno do Sol (3 anos)")
plt.legend()
plt.grid()
plt.axis("equal")
plt.show()

# Forma da Trajetória:

# A forma da trajetória obtida no gráfico é elíptica. 
