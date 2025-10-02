import numpy as np
import matplotlib.pyplot as plt

def maxminv(x, y):

    """
    x: vetor com 3 valores de tempo (em torno do máximo)
    y: vetor com os 3 valores correspondentes de theta
    retorna: tempo t do máximo e valor máximo de theta
    """

    a = ((y[2] - y[0]) - (x[2] - x[0]) * (y[1] - y[0]) / (x[1] - x[0])) / ((x[2]**2 - x[0]**2) - (x[2] - x[0]) * (x[1]**2 - x[0]**2) / (x[1] - x[0]))
    b = (y[1] - y[0] - a * (x[1]**2 - x[0]**2)) / (x[1] - x[0])
    c = y[0] - a * x[0]**2 - b * x[0]
    
    t_max = -b / (2 * a)
    theta_max = a * t_max**2 + b * t_max + c
    return t_max, theta_max

g = 9.8
L = 1.0
theta0 = 0.1
dt = 0.01
T_total = 10
N = int(T_total / dt)

t = np.linspace(0, T_total, N)
theta = np.zeros(N)
omega = np.zeros(N)
theta[0] = theta0

for i in range(N - 1):
    omega[i+1] = omega[i] - (g / L) * np.sin(theta[i]) * dt
    theta[i+1] = theta[i] + omega[i+1] * dt

max_indices = []
for i in range(1, N - 1):
    if theta[i - 1] < theta[i] and theta[i] > theta[i + 1]:
        max_indices.append(i)

tempos_maximos = []
for i in max_indices:
    if i > 0 and i < N - 1:
        x = t[i - 1:i + 2]
        y = theta[i - 1:i + 2]
        t_max, _ = maxminv(x, y)
        tempos_maximos.append(t_max)

if len(tempos_maximos) >= 2:
    periodo_medido = tempos_maximos[1] - tempos_maximos[0]
    print(f"Período medido: {periodo_medido:.4f} s")
else:
    print("Não foram encontrados dois máximos para calcular o período.")

periodo_teorico = 2 * np.pi * np.sqrt(L / g)
print(f"Período teórico: {periodo_teorico:.4f} s")

plt.plot(t, theta)
plt.title('Oscilação do pêndulo')
plt.xlabel('Tempo (s)')
plt.ylabel('Ângulo (rad)')
plt.grid()
plt.show()