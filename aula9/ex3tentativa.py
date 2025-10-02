import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parâmetros físicos
d = 0.1     # diâmetro (m)
l = 1.0     # comprimento das cordas (m)
m = 0.3     # massa (kg)
g = 9.8
k = 1e7
q = 2.0

# Simulação
dt = 0.0001
t_final = 5
n_steps = int(t_final / dt)
N = 5
n_levantadas = 2

# Estado
x = np.zeros((n_steps, N))
v = np.zeros((n_steps, N))
for i in range(N):
    if i < n_levantadas:
        x[0, i] = -5*d + d*i
    else:
        x[0, i] = d*i

def acc_toque(dx, d):
    if dx < d:
        return (-k * abs(dx - d)**q) / m
    return 0.0

def acc_i(i, x_inst):
    a = 0
    if i > 0:
        a -= acc_toque(x_inst[i] - x_inst[i - 1], d)
    if i < N - 1:
        a += acc_toque(x_inst[i + 1] - x_inst[i], d)
    a -= g * (x_inst[i] - d*i) / l
    return a

# Euler-Cromer
for t in range(n_steps - 1):
    for i in range(N):
        a = acc_i(i, x[t])
        v[t+1, i] = v[t, i] + a * dt
        x[t+1, i] = x[t, i] + v[t+1, i] * dt

# Reduzir número de frames (por exemplo, 1 a cada 10)
x_anim = x[::20]
tempo = np.linspace(0, t_final, len(x_anim))

# === Animação ===
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-N*d, (N+1)*d)
ax.set_ylim(-l - d, d)

cordas = []
bolas = []

for i in range(N):
    corda, = ax.plot([], [], 'k-', lw=1)
    bola = plt.Circle((0, 0), d/2, fc='gray', ec='black')
    ax.add_patch(bola)
    cordas.append(corda)
    bolas.append(bola)

def init():
    for corda in cordas:
        corda.set_data([], [])
    for bola in bolas:
        bola.center = (0, 0)
    return cordas + bolas

def update(frame):
    for i in range(N):
        xi = x_anim[frame, i]
        # posição do topo da corda (fixo)
        x0 = d * i
        # posição da esfera
        bola_x = xi
        bola_y = -np.sqrt(l**2 - (xi - x0)**2)  # forma circular da corda

        # Atualizar corda
        cordas[i].set_data([x0, bola_x], [0, bola_y])
        # Atualizar esfera
        bolas[i].center = (bola_x, bola_y)
    return cordas + bolas

ani = animation.FuncAnimation(fig, update, frames=len(x_anim),
                              init_func=init, blit=True, interval=0.5)
plt.title("Animação do Pêndulo de Newton")
plt.show()
