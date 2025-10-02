import numpy as np
import matplotlib.pyplot as plt

# EXERCÍCIO 1
# Alínea a)

# Constantes
g = 9.81             # Aceleração da gravidade (m/s²)
dt = 0.01            # Passo de tempo (s)
x_max = 2.5          # Posição final da simulação (m)

# Condições iniciais
x = 0.0              # Posição inicial (m)
vx = 0.0             # Velocidade inicial (m/s)

# Listas para armazenar os resultados
t_list = [0.0]
x_list = [x]
vx_list = [vx]

# Loop da simulação (Euler-Cromer)
while x < x_max:
    # Aceleração depende da posição
    if x < 2.0:
        ax = 0.05 * g
    else:
        ax = 0.0

    # Atualização de velocidade e posição (Euler-Cromer)
    vx += ax * dt
    x += vx * dt

    # Armazenar os resultados
    t_list.append(t_list[-1] + dt)
    x_list.append(x)
    vx_list.append(vx)

# Plot da posição em função do tempo
plt.plot(t_list, x_list)
plt.xlabel("Tempo (s)")
plt.ylabel("Posição x (m)")
plt.title("Movimento da bola - Euler-Cromer")
plt.grid(True)
plt.show()

# Alínea b)

# Converter as listas para arrays NumPy
x_array = np.array(x_list)
vx_array = np.array(vx_list)
t_array = np.array(t_list)

# Encontrar o índice onde a posição ultrapassa ou atinge x = 2.5 m
index_final = np.argmax(x_array >= x_max)

# Obter a velocidade final e o tempo correspondente
velocidade_final = vx_array[index_final]
tempo_final = t_array[index_final]

# Mostrar os resultados
print(f"Velocidade final da bola: {velocidade_final:.2f} m/s")
print(f"Tempo para atingir x = 2.5 m: {tempo_final:.2f} s")

# Alínea c)

# Parâmetros do sistema
m = 1.0  # massa da bola (kg) — valor arbitrário pois será simplificado

# Energia potencial inicial (altura inicial da rampa)
y_inicial = 0.1  # em metros
Ep_inicial = m * g * y_inicial

# Energia cinética final (obtida pela conservação de energia)
Ec_final = Ep_inicial

# Calcular velocidade final teórica
v_final_teorica = np.sqrt(2 * Ec_final / m)

# Mostrar resultados
print(f"Velocidade final teórica (conservação da energia): {v_final_teorica:.2f} m/s")
print(f"Velocidade final da simulação (Euler-Cromer): {velocidade_final:.2f} m/s")

# Comparação
if np.isclose(v_final_teorica, velocidade_final, atol=0.05):
    print("Os resultados são consistentes com a conservação da energia.")
else:
    print("Há uma diferença significativa; pode haver erro numérico ou aproximação.")

