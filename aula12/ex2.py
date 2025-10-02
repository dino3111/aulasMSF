import numpy as np
import matplotlib.pyplot as plt

# 1. Definir parâmetros do sistema
k = 2.0          # Constante elástica das molas externas (N/m)
k_prime = 0.5    # Constante elástica da mola de acoplamento (N/m)
m = 1.0          # Massa dos corpos (kg)
x_A_eq = 1.0     # Posição de equilíbrio do corpo A (m)
x_B_eq = 2.0     # Posição de equilíbrio do corpo B (m)

# 2. Calcular frequências dos modos normais
w1 = np.sqrt(k/m)
w2 = np.sqrt((k + 2*k_prime)/m)
print(f"Frequências dos modos normais: w1 = {w1:.2f} rad/s, w2 = {w2:.2f} rad/s")

# 3. Definir condições iniciais para os três casos
casos = [
    {"nome": "Caso 1) x_A0 = +0.2, x_B0 = -0.3", "x_A0": x_A_eq + 0.2, "x_B0": x_B_eq - 0.3, "v_A0": 0, "v_B0": 0},
    {"nome": "Caso 2) x_A0 = +0.2, x_B0 = -0.2", "x_A0": x_A_eq + 0.2, "x_B0": x_B_eq - 0.2, "v_A0": 0, "v_B0": 0},
    {"nome": "Caso 3) x_A0 = +0.3, x_B0 = +0.3", "x_A0": x_A_eq + 0.3, "x_B0": x_B_eq + 0.3, "v_A0": 0, "v_B0": 0}
]

# 4. Calcular parâmetros teóricos para cada caso
for caso in casos:
    # Calcular amplitudes dos modos normais
    caso["A1"] = (caso["x_A0"] - x_A_eq + caso["x_B0"] - x_B_eq)/2
    caso["A2"] = (caso["x_A0"] - x_A_eq - (caso["x_B0"] - x_B_eq))/2
    caso["phi1"] = 0  # Fases iniciais são zero porque v0 = 0
    caso["phi2"] = 0
    
    print(f"\n{caso['nome']}:")
    print(f"A1 = {caso['A1']:.2f} m, A2 = {caso['A2']:.2f} m")
    print(f"phi1 = {caso['phi1']}, phi2 = {caso['phi2']}")

# 5. Configurações para solução numérica (método de Euler)
dt = 0.01       # Passo de tempo (s)
t_max = 20.0    # Tempo máximo de simulação (s)
t = np.arange(0, t_max, dt)  # Vetor tempo

# 6. Função para calcular acelerações
def aceleracoes(x_A, x_B):
    F_A = -k*(x_A - x_A_eq) + k_prime*(x_B - x_A - (x_B_eq - x_A_eq))
    F_B = -k*(x_B - x_B_eq) - k_prime*(x_B - x_A - (x_B_eq - x_A_eq))
    return F_A/m, F_B/m

# 7. Simular e plotar cada caso
plt.figure(figsize=(15, 10))

for i, caso in enumerate(casos, 1):
    # Inicializar arrays para solução numérica
    x_A_num = np.zeros_like(t)
    v_A_num = np.zeros_like(t)
    x_B_num = np.zeros_like(t)
    v_B_num = np.zeros_like(t)
    
    # Condições iniciais
    x_A_num[0] = caso["x_A0"]
    x_B_num[0] = caso["x_B0"]
    v_A_num[0] = caso["v_A0"]
    v_B_num[0] = caso["v_B0"]
    
    # Integração numérica (Euler)
    for j in range(1, len(t)):
        a_A, a_B = aceleracoes(x_A_num[j-1], x_B_num[j-1])
        v_A_num[j] = v_A_num[j-1] + a_A * dt
        v_B_num[j] = v_B_num[j-1] + a_B * dt
        x_A_num[j] = x_A_num[j-1] + v_A_num[j-1] * dt
        x_B_num[j] = x_B_num[j-1] + v_B_num[j-1] * dt
    
    # Solução teórica
    x_A_teo = x_A_eq + caso["A1"]*np.cos(w1*t + caso["phi1"]) + caso["A2"]*np.cos(w2*t + caso["phi2"])
    x_B_teo = x_B_eq + caso["A1"]*np.cos(w1*t + caso["phi1"]) - caso["A2"]*np.cos(w2*t + caso["phi2"])
    
    # Plotar resultados
    plt.subplot(3, 2, 2*i-1)
    plt.plot(t, x_A_num - x_A_eq, 'b-', label='Numérico')
    plt.plot(t, x_A_teo - x_A_eq, 'r--', label='Teórico')
    plt.title(f"{caso['nome']} - Massa A")
    plt.xlabel('Tempo (s)')
    plt.ylabel('Deslocamento (m)')
    plt.legend()
    plt.grid(True)
    
    plt.subplot(3, 2, 2*i)
    plt.plot(t, x_B_num - x_B_eq, 'b-', label='Numérico')
    plt.plot(t, x_B_teo - x_B_eq, 'r--', label='Teórico')
    plt.title(f"{caso['nome']} - Massa B")
    plt.xlabel('Tempo (s)')
    plt.ylabel('Deslocamento (m)')
    plt.legend()
    plt.grid(True)

plt.tight_layout()
plt.show()