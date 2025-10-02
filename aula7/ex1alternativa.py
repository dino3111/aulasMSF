import numpy as np
import matplotlib.pyplot as plt

# Condições iniciais
x0 = 0
vx0 = 0
g = 9.8
t0 = 0
tf = 10
dt = 0.001
y0 = 0.1

# Função da pista
def y_func(x: float) -> float:
    return 0.1 - 0.05 * x if x < 2.0 else 0.0

def dydx_func(x: float) -> float:
    return -0.05 if x < 2.0 else 0.0

# Vetor de tempo
t = np.arange(t0, tf, dt)

# Inicialização de arrays
ax = np.zeros(np.size(t))
vx = np.zeros(np.size(t))
vx[0] = vx0

x = np.zeros(np.size(t))
x[0] = x0

y = np.zeros(np.size(t))
y[0] = y0

# Simulação com Euler-Cromer
for i in range(np.size(t)-1):
    ax[i] = -g * dydx_func(x[i])
    vx[i+1] = vx[i] + ax[i] * dt
    x[i+1] = x[i] + vx[i] * dt
    y[i+1] = y_func(x[i+1])  # usar x[i+1] para que y esteja atualizado com a nova posição

# Gráfico com dois eixos
fig, ax1 = plt.subplots()
color = 'tab:blue'
ax1.set_xlabel('tempo (s)')
ax1.set_ylabel('x (m)', color=color)
ax1.plot(t[x < 2.5], x[x < 2.5], color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('y (m)', color=color)
ax2.plot(t[x < 2.5], y[x < 2.5], color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.show()
