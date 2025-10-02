import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do sistema
m = 1.0        # kg
k = 1.0        # N/m
b = 0.05       # kg/s
F0 = 7.5       # N

# Condições iniciais
x0 = 4.0       # posição inicial
v0 = 0.0       # velocidade inicial

# Tempo de simulação
dt = 0.01
t_max = 200
t_values = np.arange(0, t_max, dt)

# Função de aceleração
def acelera(t, x, vx, omega_f=0.5):
    return (-k * x - b * vx + F0 * np.cos(omega_f * t)) / m

# Método RK4 para posição e velocidade
def rk4_x_vx(t, x, vx, acelera, dt, omega_f):
    ax1 = acelera(t, x, vx, omega_f)
    c1x = vx * dt
    c1v = ax1 * dt

    ax2 = acelera(t + dt/2, x + c1x/2, vx + c1v/2, omega_f)
    c2x = (vx + c1v/2) * dt
    c2v = ax2 * dt

    ax3 = acelera(t + dt/2, x + c2x/2, vx + c2v/2, omega_f)
    c3x = (vx + c2v/2) * dt
    c3v = ax3 * dt

    ax4 = acelera(t + dt, x + c3x, vx + c3v, omega_f)
    c4x = (vx + c3v) * dt
    c4v = ax4 * dt

    xp = x + (c1x + 2*c2x + 2*c3x + c4x) / 6
    vxp = vx + (c1v + 2*c2v + 2*c3v + c4v) / 6

    return xp, vxp

# Simulação ponto (a) e (b)
def simula_osc(omega_f):
    x, vx = x0, v0
    x_list = []
    for t in t_values:
        x_list.append(x)
        x, vx = rk4_x_vx(t, x, vx, acelera, dt, omega_f)
    return np.array(x_list)

# a) Simulação para wf = 0.5
x_vals = simula_osc(0.5)

# Gráfico da posição no tempo
plt.figure()
plt.plot(t_values, x_vals)
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.title('Oscilador Harmônico Forçado (wf = 0.5 rad/s)')
plt.grid(True)
plt.show()

# b) Amplitude e período no regime estacionário
# Consideramos últimos 10 segundos para análise
x_regime = x_vals[-int(10/dt):]
amplitude = (np.max(x_regime) - np.min(x_regime)) / 2
print(f'Amplitude no regime estacionário: {amplitude:.3f} m')

# c) Estudo para diferentes wf
omega_range = np.linspace(0.2, 2.0, 100)
amplitudes = []

for omega in omega_range:
    x_vals = simula_osc(omega)
    x_regime = x_vals[-int(10/dt):]
    amp = (np.max(x_regime) - np.min(x_regime)) / 2
    amplitudes.append(amp)

# Gráfico da amplitude em função de wf
plt.figure()
plt.plot(omega_range, amplitudes)
plt.xlabel('Frequência angular wf (rad/s)')
plt.ylabel('Amplitude no regime estacionário (m)')
plt.title('Amplitude vs Frequência Forçadora')
plt.grid(True)
plt.show()

# Frequência com maior amplitude
omega_max_amp = omega_range[np.argmax(amplitudes)]
print(f'wf com maior amplitude: {omega_max_amp:.3f} rad/s')
