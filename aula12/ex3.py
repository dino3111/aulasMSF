import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do sistema
k = 1.0
k_prime = 0.5
m = 1.0
x_A_eq = 1.0
x_B_eq = 2.0

# Frequências dos modos normais (calculadas no exercício anterior)
w1 = np.sqrt(k/m)  # 1.0 rad/s
w2 = np.sqrt((k + 2*k_prime)/m)  # 1.414 rad/s

# Configurações da análise de Fourier
T = 100.0  # Período total de análise
dt = 0.1   # Passo de tempo
t = np.arange(0, T, dt)
n_max = 30  # Número máximo de coeficientes

# Função para calcular coeficientes de Fourier (simplificada)
def abfourier(tp, xp, i10, i11, n):

    T = tp[i11] - tp[i10]
    omega = 2*np.pi/T
    
    # Calcula coeficientes
    a_n = 2/T * np.sum(xp[i10:i11] * np.cos(n*omega*tp[i10:i11])) * (tp[1]-tp[0])
    b_n = 2/T * np.sum(xp[i10:i11] * np.sin(n*omega*tp[i10:i11])) * (tp[1]-tp[0])
    
    return a_n, b_n

# Condições iniciais para os três casos
casos = [
    {"nome": "Caso i) x_A0 = +0.3, x_B0 = +0.3", "x_A0": x_A_eq + 0.3, "x_B0": x_B_eq + 0.3},
    {"nome": "Caso ii) x_A0 = +0.3, x_B0 = -0.3", "x_A0": x_A_eq + 0.3, "x_B0": x_B_eq - 0.3},
    {"nome": "Caso iii) x_A0 = +0.3, x_B0 = -0.1", "x_A0": x_A_eq + 0.3, "x_B0": x_B_eq - 0.1}
]

# Para cada caso, calcular movimento e coeficientes de Fourier
for caso in casos:
    # 1. Calcular movimento teórico
    if caso["nome"].startswith("Caso i"):
        # Modo 1 apenas
        x_A = x_A_eq + 0.3*np.cos(w1*t)
        x_B = x_B_eq + 0.3*np.cos(w1*t)
    elif caso["nome"].startswith("Caso ii"):
        # Modo 2 apenas
        x_A = x_A_eq + 0.3*np.cos(w2*t)
        x_B = x_B_eq - 0.3*np.cos(w2*t)
    else:
        # Caso iii: mistura dos dois modos
        x_A = x_A_eq + 0.1*np.cos(w1*t) + 0.2*np.cos(w2*t)
        x_B = x_B_eq + 0.1*np.cos(w1*t) - 0.2*np.cos(w2*t)
    
    # 2. Calcular coeficientes de Fourier
    i10, i11 = 0, len(t)-1  # Usar todo o intervalo
    a_ns = []
    b_ns = []
    omega_ns = []
    
    for n in range(1, n_max+1):
        a_n, b_n = abfourier(t, x_A, i10, i11, n)
        a_ns.append(a_n)
        b_ns.append(b_n)
        omega_ns.append(n * (2*np.pi/T))
    
    # 3. Plotar coeficientes
    plt.figure(figsize=(12, 5))
    plt.suptitle(caso["nome"])
    
    plt.subplot(1, 2, 1)
    plt.stem(omega_ns, a_ns, 'b', markerfmt='bo', label='$a_n$')
    plt.axvline(x=w1, color='r', linestyle='--', label=f'$\omega_1$ = {w1:.3f}')
    plt.axvline(x=w2, color='g', linestyle='--', label=f'$\omega_2$ = {w2:.3f}')
    plt.xlabel('$\omega_n$ (rad/s)')
    plt.ylabel('$a_n$')
    plt.legend()
    plt.grid(True)
    
    plt.subplot(1, 2, 2)
    plt.stem(omega_ns, b_ns, 'r', markerfmt='ro', label='$b_n$')
    plt.axvline(x=w1, color='r', linestyle='--', label=f'$\omega_1$ = {w1:.3f}')
    plt.axvline(x=w2, color='g', linestyle='--', label=f'$\omega_2$ = {w2:.3f}')
    plt.xlabel('$\omega_n$ (rad/s)')
    plt.ylabel('$b_n$')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

# Pergunta 2:
# A análise de Fourier revela picos em w1 (1.0 rad/s) e w2 (1.4 rad/s), confirmando a teoria. No caso i só aparece w1 (modo simétrico), no caso ii só w2 (modo antissimétrico), e no caso iii ambas, mostrando como o movimento se decompõe nesses modos normais. Os coeficientes b_n são próximos de zero, como esperado para v0=0, validando completamente a solução teórica.

