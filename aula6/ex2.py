import numpy as np
import matplotlib.pyplot as plt

gm = 4 * np.pi**2  # Constante gravitacional (AU^3/ano^2)
x0, y0 = 1.0, 0.0  # Posição inicial (AU)
vx0, vy0 = 0.0, 2 * np.pi  # Velocidade inicial (AU/ano)

dt = 0.01  # Passo de tempo (anos)
t_max = 10.0  # Tempo total de simulação (anos)
n = int(t_max / dt)

# Arrays para resultados
t = np.zeros(n+1)
x, y = np.zeros(n+1), np.zeros(n+1)
vx, vy = np.zeros(n+1), np.zeros(n+1)
ax, ay = np.zeros(n+1), np.zeros(n+1)

# Condições iniciais
x[0], y[0] = x0, y0
vx[0], vy[0] = vx0, vy0

# Método de Euler-Cromer
for i in range(n):
    t[i+1] = t[i] + dt
    r = np.sqrt(x[i]**2 + y[i]**2)
    
    # Aceleração no passo atual
    ax[i] = -gm * x[i] / r**3
    ay[i] = -gm * y[i] / r**3
    
    # Atualização da velocidade (como no Euler)
    vx[i+1] = vx[i] + ax[i] * dt
    vy[i+1] = vy[i] + ay[i] * dt
    
    # Atualização da posição (Euler-Cromer: usa v[i+1] em vez de v[i]!)
    x[i+1] = x[i] + vx[i+1] * dt
    y[i+1] = y[i] + vy[i+1] * dt

# Plot
plt.plot(x, y, 'b-', label='Órbita da Terra (Euler-Cromer)')
plt.plot(0, 0, 'yo', markersize=12, label='Sol')
plt.plot(x0, y0, 'ro', label='Posição inicial')
plt.xlabel('x (AU)')
plt.ylabel('y (AU)')
plt.title(f'Órbita com Euler-Cromer (dt={dt} anos)')
plt.grid()
plt.legend()
plt.show()

# Pergunta 2: Se a posição inicial da planeta foi (0.5,0), a velocidade inicial deve ser maior ou menor, para conseguir uma órbita circular?

# Resposta: A velocidade deve ser maior, pois ao estar mais próximo do Sol, a força gravitacional é mais forte e é preciso mais velocidade para manter uma órbita circular.