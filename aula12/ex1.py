import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do sistema
k = 1.0  # N/m
k_prime = 0.5  # N/m
m = 1.0  # kg
x_A_eq = 1.0  # m
x_B_eq = 2.0  # m

# Configuração da simulação
dt = 0.01  # passo de tempo (s)
t_max = 20.0  # tempo máximo de simulação (s)
steps = int(t_max / dt)  # número de passos

# Função que calcula as acelerações
def calculate_accelerations(x_A, x_B):
    # Forças atuando em A e B
    F_A = -k * (x_A - x_A_eq) + k_prime * (x_B - x_A - (x_B_eq - x_A_eq))
    F_B = -k * (x_B - x_B_eq) - k_prime * (x_B - x_A - (x_B_eq - x_A_eq))
    
    # Acelerações
    a_A = F_A / m
    a_B = F_B / m
    
    return a_A, a_B

# Casos a serem simulados
cases = [
    {
        'name': 'Caso i) x_A0 = +0.3, x_B0 = +0.3',
        'initial_conditions': [x_A_eq + 0.3, 0, x_B_eq + 0.3, 0]
    },
    {
        'name': 'Caso ii) x_A0 = +0.3, x_B0 = -0.3',
        'initial_conditions': [x_A_eq + 0.3, 0, x_B_eq - 0.3, 0]
    },
    {
        'name': 'Caso iii) x_A0 = +0.3, x_B0 = -0.1',
        'initial_conditions': [x_A_eq + 0.3, 0, x_B_eq - 0.1, 0]
    }
]

# Simular e plotar cada caso
plt.figure(figsize=(15, 10))

for case_num, case in enumerate(cases, 1):
    # Inicializar arrays para armazenar resultados
    time = np.zeros(steps)
    x_A = np.zeros(steps)
    v_A = np.zeros(steps)
    x_B = np.zeros(steps)
    v_B = np.zeros(steps)
    
    # Condições iniciais
    x_A[0], v_A[0], x_B[0], v_B[0] = case['initial_conditions']
    
    # Integração numérica (método de Euler)
    for i in range(1, steps):
        time[i] = time[i-1] + dt
        
        # Calcular acelerações no passo anterior
        a_A, a_B = calculate_accelerations(x_A[i-1], x_B[i-1])
        
        # Atualizar velocidades e posições
        v_A[i] = v_A[i-1] + a_A * dt
        v_B[i] = v_B[i-1] + a_B * dt
        x_A[i] = x_A[i-1] + v_A[i-1] * dt
        x_B[i] = x_B[i-1] + v_B[i-1] * dt
    
    # Plotar os resultados
    plt.subplot(3, 1, case_num)
    plt.plot(time, x_A - x_A_eq, label='Deslocamento A (m)')
    plt.plot(time, x_B - x_B_eq, label='Deslocamento B (m)')
    plt.title(case['name'])
    plt.xlabel('Tempo (s)')
    plt.ylabel('Deslocamento (m)')
    plt.legend()
    plt.grid(True)

plt.tight_layout()
plt.show()

# Pergunta 1:
# Se k´= 0, as massas A e B não estão mais acopladas. Cada uma oscilaria independentemente, como um oscilador harmônico simples, com frequência angular w = raiz(k/m). Os movimentos seriam independentes e não haveria transferência de energia entre elas.