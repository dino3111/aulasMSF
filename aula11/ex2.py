import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do sistema
alpha = 1.0   # N/m^3
k = 0.2       # N/m
b = 0.01      # kg/s
F0 = 5.0      # N
omega_f = 0.6 # rad/s
m = 1.0       # kg

# Condições iniciais
x0 = 1.0      # m
v0 = 0.0      # m/s

# Tempo de simulação
dt = 0.01
t_max = 50
t_values = np.arange(0, t_max, dt)

# Função de aceleração
def acelera(t, x, vx):
    return (-k * x - 4 * alpha * x**3 - b * vx + F0 * np.cos(omega_f * t)) / m

# Método de Runge-Kutta de 4ª ordem
def rk4_x_vx(t, x, vx, acelera, dt):
    ax1 = acelera(t, x, vx)
    c1x = vx * dt
    c1v = ax1 * dt

    ax2 = acelera(t + dt/2, x + c1x/2, vx + c1v/2)
    c2x = (vx + c1v/2) * dt
    c2v = ax2 * dt

    ax3 = acelera(t + dt/2, x + c2x/2, vx + c2v/2)
    c3x = (vx + c2v/2) * dt
    c3v = ax3 * dt

    ax4 = acelera(t + dt, x + c3x, vx + c3v)
    c4x = (vx + c3v) * dt
    c4v = ax4 * dt

    xp = x + (c1x + 2*c2x + 2*c3x + c4x) / 6
    vxp = vx + (c1v + 2*c2v + 2*c3v + c4v) / 6

    return xp, vxp

# Simulação
x_vals = []
vx_vals = []
x, vx = x0, v0

for t in t_values:
    x_vals.append(x)
    vx_vals.append(vx)
    x, vx = rk4_x_vx(t, x, vx, acelera, dt)

# Gráficos
plt.figure(figsize=(12, 5))

# Posição vs tempo
plt.subplot(1, 2, 1)
plt.plot(t_values, x_vals)
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.title('Posição vs Tempo')

# Espaço de fase
plt.subplot(1, 2, 2)
plt.plot(x_vals, vx_vals)
plt.xlabel('Posição (m)')
plt.ylabel('Velocidade (m/s)')
plt.title('Espaço de Fase: v(t) vs x(t)')
plt.tight_layout()
plt.grid(True)
plt.show()
