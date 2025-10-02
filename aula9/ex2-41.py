import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parâmetros físicos
d = 0.1     # diâmetro das esferas (m)
l = 1.0     # comprimento da corda (m)
m = 0.3     # massa da esfera (kg)
g = 9.8     # gravidade (m/s²)
k = 1e7     # constante elástica
q = 2.0     # expoente da força de contacto

# Parâmetros de simulação
dt = 0.0001
t_final = 5
n_steps = int(t_final / dt)

# Número de esferas e quantas são levantadas
N = 4               # total de esferas
n_levantadas = 1    # número de esferas deslocadas inicialmente

# Vetores de posição e velocidade
x = np.zeros((n_steps, N))
v = np.zeros((n_steps, N))

# Condições iniciais
for i in range(N):
    if i < n_levantadas:
        x[0, i] = -5 * d + d * i
    else:
        x[0, i] = d * i

# Funções auxiliares
def acc_toque(dx, d):
    if dx < d:
        return (-k * abs(dx - d)**q) / m
    else:
        return 0.0

def acc_i(i, x_inst):
    a = 0
    if i > 0:
        a -= acc_toque(x_inst[i] - x_inst[i - 1], d)
    if i < N - 1:
        a += acc_toque(x_inst[i + 1] - x_inst[i], d)
    a -= g * (x_inst[i] - d * i) / l
    return a

# Simulação com Euler-Cromer
for t in range(n_steps - 1):
    for i in range(N):
        a = acc_i(i, x[t])
        v[t + 1, i] = v[t, i] + a * dt
        x[t + 1, i] = x[t, i] + v[t + 1, i] * dt

# Animação acelerada
fig, ax = plt.subplots()
ax.set_xlim(-0.5, N * d + 0.5)
ax.set_ylim(-0.2, 0.2)
ax.set_aspect('equal')
ax.set_title('Animação rápida do sistema de esferas')
ax.axis('off')

bolas, = ax.plot([], [], 'ko', ms=20)

def init():
    bolas.set_data([], [])
    return bolas,

def update(frame):
    bolas.set_data(x[frame, :], np.zeros(N))
    return bolas,

ani = FuncAnimation(
    fig,
    update,
    frames=range(0, n_steps, 150),  
    init_func=init,
    blit=True,
    interval=10                    
    )

plt.show()
