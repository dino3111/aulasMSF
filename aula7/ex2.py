# Exercício 2

import numpy as np
import matplotlib.pyplot as plt

# 1. Simulação do movimento com Euler-Cromer

# Constantes
g = 9.81
dt = 0.01
x_max = 2.5

# Condições iniciais
x = 0.0
vx = 0.0
t = 0.0

# Listas para armazenar dados
x_list = [x]
vx_list = [vx]
t_list = [t]

# Simulação com Euler-Cromer
while x < x_max:
    if x < 2.0:
        ax = -g * 0.05 * (x - 2)
    else:
        ax = 0.0

    vx += ax * dt
    x += vx * dt
    t += dt

    x_list.append(x)
    vx_list.append(vx)
    t_list.append(t)

# 2. Tempo até atingir x = 2.5 m

# Converter listas para arrays
x_array = np.array(x_list)
vx_array = np.array(vx_list)
t_array = np.array(t_list)

# Encontrar o índice quando x >= 2.5
i_final = np.argmax(x_array >= x_max)
tempo_final = t_array[i_final]

print(f"Tempo para atingir x = 2.5 m: {tempo_final:.2f} s")

# 3. Gráfico de vx em função da altura y

# Função da pista parabólica
def f(x):
    return 0.025 * (x - 2)**2 if x < 2 else 0.0

# Calcular altura y para cada x
y_array = np.array([f(xi) for xi in x_array])

# Gráfico velocidade vs altura
plt.plot(y_array, vx_array)
plt.xlabel("Altura y (m)")
plt.ylabel("Velocidade vx (m/s)")
plt.title("Velocidade em função da altura (pista parabólica)")
plt.grid(True)
plt.show()
