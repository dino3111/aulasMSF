import numpy as np
import matplotlib.pyplot as plt

# a)

def maxminv(x, y):
    a = ((y[2] - y[0]) - (x[2] - x[0]) * (y[1] - y[0]) / (x[1] - x[0])) / ((x[2]**2 - x[0]**2) - (x[2] - x[0]) * (x[1]**2 - x[0]**2) / (x[1] - x[0]))
    b = (y[1] - y[0] - a * (x[1]**2 - x[0]**2)) / (x[1] - x[0])
    c = y[0] - a * x[0]**2 - b * x[0]
    t_max = -b / (2 * a)
    theta_max = a * t_max**2 + b * t_max + c
    return t_max, theta_max

def medir_periodo(L, g=9.8, theta0=0.1, dt=0.001, T_total=10):
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
        if theta[i-1] < theta[i] and theta[i] > theta[i+1]:
            max_indices.append(i)
    
    tempos_maximos = []
    for i in max_indices:
        if i > 0 and i < N - 1:
            x = t[i - 1:i + 2]
            y = theta[i - 1:i + 2]
            t_max, _ = maxminv(x, y)
            tempos_maximos.append(t_max)
    
    if len(tempos_maximos) >= 2:
        return tempos_maximos[1] - tempos_maximos[0]
    else:
        return np.nan

Ls = np.linspace(0.2, 2.0, 10)
Ts = np.array([medir_periodo(L) for L in Ls])

# b)

log_L = np.log(Ls)
log_T = np.log(Ts)

plt.scatter(log_L, log_T, label='Dados simulados')
plt.xlabel('log(L)')
plt.ylabel('log(T)')
plt.title('log(T) em função de log(L)')
plt.grid()
plt.legend()
plt.show()

# c)

A = np.vstack([log_L, np.ones_like(log_L)]).T
m, b = np.linalg.lstsq(A, log_T, rcond=None)[0]

residuos = log_T - (m * log_L + b)
sigma2 = np.sum(residuos**2) / (len(log_L) - 2)
cov_m = sigma2 * np.linalg.inv(A.T @ A)
erro_m = np.sqrt(cov_m[0, 0])

plt.scatter(log_L, log_T, label='Dados simulados')
plt.plot(log_L, m * log_L + b, 'r--', label=f'Ajuste linear: m = {m:.3f} ± {erro_m:.3f}')
plt.xlabel('log(L)')
plt.ylabel('log(T)')
plt.title('Ajuste linear ao gráfico log-log (sem scipy)')
plt.grid()
plt.legend()
plt.show()

print(f"Declive (m): {m:.4f} ± {erro_m:.4f}")

