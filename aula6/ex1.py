import numpy as np
import matplotlib.pyplot as plt

# Constantes no sistema astronômico de unidades
gm = 4 * np.pi**2  # G*M_sol (em AU³/ano²)

# Condições iniciais
x0 = 1.0    # AU
y0 = 0.0    # AU
vx0 = 0.0   # AU/ano
vy0 = 2 * np.pi  # AU/ano (velocidade orbital para órbita circular)

# Parâmetros da simulação
dt = 0.01           # Passo de tempo (anos)
t_max = 10.0        # Tempo total (anos)
n = int(t_max / dt) # Número de passos (1000)

# Arrays para armazenar os resultados
x = np.zeros(n+1)
y = np.zeros(n+1)
vx = np.zeros(n+1)
vy = np.zeros(n+1)

# Condições iniciais
x[0], y[0] = x0, y0
vx[0], vy[0] = vx0, vy0

# Método de Euler
for i in range(n):
    r = np.sqrt(x[i]**2 + y[i]**2)
    ax = -gm * x[i] / r**3
    ay = -gm * y[i] / r**3
    vx[i+1] = vx[i] + ax * dt
    vy[i+1] = vy[i] + ay * dt
    x[i+1] = x[i] + vx[i] * dt
    y[i+1] = y[i] + vy[i] * dt

# Gráfico da órbita
plt.plot(x, y, '--', color='green', linewidth=2, label='Órbita (Euler)')
plt.plot(0, 0, 'o', color='orange', markersize=10, label='Sol')
plt.plot(x0, y0, 'ro', label='Posição inicial')
plt.xlabel('x (AU)')
plt.ylabel('y (AU)')
plt.title(f'Órbita da Terra - Método de Euler (dt = {dt} anos)')
plt.grid()
plt.axis('equal')
plt.legend()
plt.show()
