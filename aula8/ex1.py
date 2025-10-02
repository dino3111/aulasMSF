import numpy as np
import matplotlib.pyplot as plt

# dados
g = 9.81
rho = 1.225
massa = 0.057
diametro = 0.067
area = np.pi * (diametro / 2) ** 2
v_terminal = 120 * (1000 / 3600)

# coeficiente de arrasto
C_d = (2 * massa * g) / (rho * v_terminal ** 2 * area)

# dados iniciais
pos = np.array([0.0, 0.0, 3.0])  # 3 metros de altura
vel = np.array([160, 0, -20]) * (1000 / 3600)

# Parâmetros de simulação
dt = 0.01
tempo = 0.0

# Usar NumPy puro (sem append)
n_steps_max = 10000
traj = np.zeros((n_steps_max, 3))
traj[0] = pos
i = 1

# ciclo para calcular o arrasto, acelaração total, atualizar velocidade e posição e desenhar a trajetória até a bola cair no chão
while pos[2] > 0 and i < n_steps_max:
    v_norm = np.linalg.norm(vel)
    F_arrasto = -0.5 * rho * C_d * area * v_norm * vel if v_norm > 0 else np.zeros(3)
    acc = np.array([0, 0, -g]) + F_arrasto / massa
    vel += acc * dt
    pos += vel * dt
    tempo += dt
    traj[i] = pos
    i += 1

# cortar array até ao ponto real
traj = traj[:i]

# interpolação para ponto de impacto
p1 = traj[-2]
p2 = traj[-1]
frac = p1[2] / (p1[2] - p2[2])
impacto = p1 + (p2 - p1) * frac
tempo_final = tempo - dt + frac * dt
# vê com mais precisão qnd a bola atinge o solo

print(f"Bola caiu no solo em t = {tempo_final:.2f} s")
print(f"Posição de impacto: x = {impacto[0]:.2f} m, y = {impacto[1]:.2f} m")

# Preparar gráfico
fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111, projection='3d')

# Trajetória da bola
ax.plot(traj[:, 0], traj[:, 1], traj[:, 2], label="Trajetória", linewidth=2, color='green')
ax.scatter([impacto[0]], [impacto[1]], [0], color='red', s=100, label="Impacto")

# Configurações do campo
ax.set_xlabel('Comprimento X (m)')
ax.set_ylabel('Largura Y (m)')
ax.set_zlabel('Altura Z (m)')
ax.set_title("Djokovic > Federer")
ax.legend()
ax.grid(True)

# Solo (campo de ténis) em azul
x_solo = np.linspace(0, 23.77, 2)
y_solo = np.linspace(-4.115, 4.115, 2)
xx, yy = np.meshgrid(x_solo, y_solo)
zz = np.zeros_like(xx)
ax.plot_surface(xx, yy, zz, alpha=0.3, color='blue')  

# Rede (no centro do campo)
x_rede = 11.885
y_rede = np.linspace(-4.115, 4.115, 2)
z_rede = np.linspace(0, 0.914, 2)
yy, zz = np.meshgrid(y_rede, z_rede)
xx = np.full_like(yy, x_rede)
ax.plot_surface(xx, yy, zz, color='black', alpha=0.9)

# Linhas do campo (em cima do solo, z = 0) — agora a preto
linhas = [
    # Linhas laterais
    [[0, -4.115], [23.77, -4.115]],
    [[0, 4.115], [23.77, 4.115]],
    [[0, -4.115], [0, 4.115]],
    [[23.77, -4.115], [23.77, 4.115]],

    # Linhas de serviço
    [[5.485, -4.115], [5.485, 4.115]],
    [[18.285, -4.115], [18.285, 4.115]],

    # Linha central de serviço (curta, oficial)
    [[11.885, -1.37], [11.885, 1.37]],

    # Linha central completa (opcional, para visual)
    [[11.885, -4.115], [11.885, 4.115]],

    # Linhas laterais de serviço (zona entre linha de serviço e rede)
    [[5.485, 0], [18.285, 0]],

    # Linha de fundo central (pequena marca)
    [[0, 0], [0.15, 0]],
    [[23.77, 0], [23.62, 0]],
]

for linha in linhas:
    x_vals = [linha[0][0], linha[1][0]]
    y_vals = [linha[0][1], linha[1][1]]
    z_vals = [0, 0]
    ax.plot(x_vals, y_vals, z_vals, color='black', linewidth=2)  # agora a preto

# Limites do gráfico para parecer um corte lateral
ax.set_xlim(-0.5, 24.3)  
ax.set_ylim(-4.5, 4.5)
ax.set_zlim(0, 5)

plt.tight_layout()
plt.show()
