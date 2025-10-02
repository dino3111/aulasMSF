import numpy as np
import matplotlib.pyplot as plt

# a) Simulação com Euler-Cromer

g = 9.8
L = 1.0
theta0 = 0.1
omega0 = 0.0
dt = 0.01
T = 10
N = int(T/dt)

t = np.linspace(0, T, N)
theta = np.zeros(N)
omega = np.zeros(N)

theta[0] = theta0
omega[0] = omega0

for i in range(N - 1):
    omega[i+1] = omega[i] - (g/L) * np.sin(theta[i]) * dt
    theta[i+1] = theta[i] + omega[i+1] * dt

plt.plot(t, theta, label='Euler-Cromer (θ₀ = 0.1 rad)')
plt.xlabel('Tempo (s)')
plt.ylabel('Ângulo θ (rad)')
plt.title('Movimento do pêndulo simples')
plt.grid()
plt.legend()
plt.show()

# b) Comparação com a solução analítica

A = theta0
phi = 0 

theta_analitico = A * np.cos(np.sqrt(g/L) * t + phi)

plt.plot(t, theta, label='Euler-Cromer')
plt.plot(t, theta_analitico, '--', label='Solução analítica')
plt.xlabel('Tempo (s)')
plt.ylabel('Ângulo θ (rad)')
plt.title('Comparação: Euler-Cromer vs Solução analítica (θ₀ = 0.1 rad)')
plt.grid()
plt.legend()
plt.show()

# c) Comparar com ângulos maiores + calcular erro

def simula_pendulo(theta0):
    theta = np.zeros(N)
    omega = np.zeros(N)
    theta[0] = theta0
    omega[0] = 0.0
    for i in range(N - 1):
        omega[i+1] = omega[i] - (g/L) * np.sin(theta[i]) * dt
        theta[i+1] = theta[i] + omega[i+1] * dt
    return theta

# Comparação visual das soluções
plt.figure(figsize=(10, 6))

for theta0 in np.arange(0.1, 0.7, 0.1):  
    theta_simulado = simula_pendulo(theta0)
    theta_analitico = theta0 * np.cos(np.sqrt(g/L) * t)

    erro_absoluto = np.abs(theta_simulado - theta_analitico)
    erro_relativo = np.abs((theta_simulado - theta_analitico) / theta_analitico) * 100
    dma = np.mean(erro_absoluto)
    erro_relativo_medio = np.mean(erro_relativo[np.isfinite(erro_relativo)]) 

    print(f"omega zero = {theta0:.1f} rad:")
    print(f"  -  Desvio médio absoluto: {dma:.6f} rad")
    print(f"  - Erro relativo médio: {erro_relativo_medio:.2f}%\n")

    plt.plot(t, theta_simulado, label=f'Numérico w0={theta0:.1f}')
    plt.plot(t, theta_analitico, '--', label=f'Analítico w0={theta0:.1f}')

plt.xlabel('Tempo (s)')
plt.ylabel('Ângulo θ (rad)')
plt.title('Comparação Euler-Cromer vs Analítica (w0 de 0.1 a 0.6 rad)')
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()


theta0_vals = np.arange(0.1, 0.7, 0.1)
erros_médios = []

for theta0 in theta0_vals:
    theta_simulado = simula_pendulo(theta0)
    theta_analitico = theta0 * np.cos(np.sqrt(g/L) * t)
    erro_absoluto = np.abs(theta_simulado - theta_analitico)
    dma = np.mean(erro_absoluto)
    erros_médios.append(dma)

plt.figure(figsize=(8, 5))
plt.plot(theta0_vals, erros_médios, 'o', label='Desvio médio absoluto')  
plt.xlabel('Ângulo inicial θ₀ (rad)')
plt.ylabel('Desvio médio absoluto (rad)')
plt.title('Erro médio vs Ângulo inicial (1 ponto por θ₀)')
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()


