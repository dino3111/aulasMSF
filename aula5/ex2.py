# Exercício 2: Bola de futebol com rotação (movimento a 3D)

# Determinar se é golo ou não, a bola ser chutada do canto
# com rotação. Implementar o movimento da bola usando o
# método de Euler com 3 dimensões.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constantes e parâmetros iniciais
m = 0.45  # massa da bola (kg)
r = 0.11  # raio da bola (m)
A = np.pi * r**2  # área transversal (m²)
rho_ar = 1.225  # densidade do ar (kg/m³)
g = 9.81  # aceleração gravítica (m/s²)

# Posição e velocidade iniciais
r0 = np.array([0, 0, 23.8])  # posição inicial (x, y, z) (m)
v0 = np.array([25, 5, -50])  # velocidade inicial (vx, vy, vz) (m/s)
omega = np.array([0, 390, 0])  # velocidade angular (rad/s)

# Parâmetros da simulação
dt = 0.001  # passo de tempo (s)
t_max = 2.0  # tempo máximo de simulação (s)
n_steps = int(t_max / dt)  # número de passos

# Arrays para armazenar resultados
t = np.zeros(n_steps)
r_vals = np.zeros((n_steps, 3))  # posições (x, y, z)
v_vals = np.zeros((n_steps, 3))  # velocidades (vx, vy, vz)

# Condições iniciais
t[0] = 0
r_vals[0] = r0
v_vals[0] = v0

# Coeficiente de arrasto (estimado para uma bola de futebol)
C_d = 0.2

# Método de Euler para resolver a equação do movimento
for i in range(1, n_steps):
    # Velocidade atual
    v = v_vals[i-1]
    
    # Força de Magnus
    F_magnus_x = 0.5 * A * rho_ar * r * omega[1] * v[2]
    F_magnus_z = -0.5 * A * rho_ar * r * omega[1] * v[0]
    F_magnus = np.array([F_magnus_x, 0, F_magnus_z])
    
    # Força de arrasto (oposta à velocidade)
    v_norm = np.linalg.norm(v)
    if v_norm > 0:
        F_drag = -0.5 * C_d * A * rho_ar * v_norm * v
    else:
        F_drag = np.zeros(3)
    
    # Força gravítica
    F_gravity = np.array([0, 0, -m * g])
    
    # Força total
    F_total = F_magnus + F_drag + F_gravity
    
    # Aceleração
    a = F_total / m
    
    # Atualizar velocidade e posição (método de Euler)
    v_vals[i] = v_vals[i-1] + a * dt
    r_vals[i] = r_vals[i-1] + v_vals[i-1] * dt
    t[i] = t[i-1] + dt
    
    # Parar se a bola atingir o chão (z <= 0)
    if r_vals[i, 2] <= 0:
        r_vals = r_vals[:i+1]
        v_vals = v_vals[:i+1]
        t = t[:i+1]
        break

# Extrair componentes da posição
x = r_vals[:, 0]
y = r_vals[:, 1]
z = r_vals[:, 2]

# Verificar se é golo
is_goal = False
if x[-1] <= 0 and -3.66 < z[-1] < 3.66 and 0 < y[-1] < 2.4:
    is_goal = True

# Plot 3D da trajetória
plt.figure(figsize=(8, 8))
ax = plt.axes(projection='3d')

# Desenhar a baliza
goalx = [0, 0, 0, 0]
goaly = [0, 2.4, 2.4, 0]
goalz = [-3.66, -3.66, 3.66, 3.66]
ax.plot3D(goalx, goalz, goaly, 'k', linewidth=2)

# Trajetória da bola (apenas para x >= 0)
ax.plot3D(x[x >= 0], -z[x >= 0], y[x >= 0], 'r', linewidth=2)

# Ajustar eixos
ax.set_xlim3d(0, 5)
ax.set_ylim3d(-25, 5)
ax.set_zlim3d(0, 5)
ax.set_box_aspect((2, 6, 2))
ax.set_xlabel('x (m)')
ax.set_ylabel('z (m)')
ax.set_zlabel('y (m)')
ax.set_title(f'Trajetória da bola - {"GOLO!" if is_goal else "Não é golo"}')

plt.tight_layout()
plt.show()

# Resultados
print(f"Posição final: ({x[-1]:.2f}, {y[-1]:.2f}, {z[-1]:.2f}) m")
print(f"Velocidade final: ({v_vals[-1,0]:.2f}, {v_vals[-1,1]:.2f}, {v_vals[-1,2]:.2f}) m/s")
print(f"Tempo de voo: {t[-1]:.2f} s")
print(f"Resultado: {'GOLO!' if is_goal else 'Não é golo'}")

# Pergunta 2: A velocidade de rotação da bola deve ser aumentada ou diminuída
# para que a bola se aproxime mais do centro da baliza?

# A velocidade de rotação da bola deve ser diminuída para que ela se aproxime mais do centro da baliza, pois quanto maior a rotação, maior é a força de Magnus, que provoca o desvio lateral da trajetória. Ao reduzir essa rotação, a bola faz menos curva e segue um caminho mais direto em direção ao centro.