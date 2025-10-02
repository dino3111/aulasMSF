import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Exercício 2 - Aula prática 4

# Uma bola é lançada verticalmente para cima com a velocidade 10 m/s. 

# a) Encontre analiticamente a lei do movimento 𝑦 = 𝑦(𝑡) , se não considerar a resistência do ar.

# Definir variáveis simbólicas
t = sp.Symbol('t')
g = 9.8  # Aceleração da gravidade (m/s^2)
v0 = 10  # Velocidade inicial (m/s)

# Equação do movimento
y_t = v0 * t - (1/2) * g * t**2

# b) Qual a altura máxima e o instante em que ocorre, no caso da alínea a)?
# Encontrar o instante em que a altura máxima ocorre
t_max = sp.solve(sp.diff(y_t, t), t)[0]

# Calcular a altura máxima substituindo t_max na equação de y(t)
y_max = y_t.subs(t, t_max)

print(t_max, y_max)

# c) Em que instante volta a passar pela posição inicial, no caso da alínea a)?

# Resolver a equação y(t) = 0 para encontrar o instante em que a bola volta à posição inicial
t_initial_position = sp.solve(y_t, t)

# Filtrar a solução positiva (t > 0)
t_initial_position = [sol for sol in t_initial_position if sol > 0][0]

print(t_initial_position)

# d) Resolva a alínea a), considerando a resistência do ar, usando o método de Euler. A
# velocidade terminal da bola no ar é de 100 km/h.

# Definir parâmetros
v_terminal = 100 * 1000 / 3600  # Converter km/h para m/s
dt = 0.01  # Passo de tempo
t_max = 2 * v0 / g  # Tempo máximo de simulação (aproximado)
n_steps = int(t_max / dt)  # Número de passos de tempo

# Inicializar variáveis
t_values = np.linspace(0, t_max, n_steps)
y_values = np.zeros(n_steps)
v_values = np.zeros(n_steps)
y_values[0] = 0
v_values[0] = v0

# Método de Euler
for i in range(1, n_steps):
    v_values[i] = v_values[i-1] - g * dt - (g / v_terminal) * v_values[i-1] * dt
    y_values[i] = y_values[i-1] + v_values[i-1] * dt

# Plotar resultados
plt.plot(t_values, y_values)
plt.xlabel('Tempo (s)')
plt.ylabel('Altura (m)')
plt.title('Movimento da bola com resistência do ar')
plt.grid(True)
plt.show()

# e) Repita alíneas b) e c) nas condições de alínea d). Deve encontrar uma maneira numérica de
# estimar os instantes da altura máxima e do retorno ao posição inicial.

# Encontrar o instante da altura máxima (quando a velocidade se torna zero)
t_max_numerical = t_values[np.argmin(np.abs(v_values))]

# Encontrar a altura máxima correspondente
y_max_numerical = y_values[np.argmin(np.abs(v_values))]

print(f"Instante da altura máxima (numérico): {t_max_numerical}")
print(f"Altura máxima (numérica): {y_max_numerical}")

# Encontrar o instante de retorno à posição inicial (quando a altura se torna zero)
t_initial_position_numerical = t_values[np.argmin(np.abs(y_values))]

print(f"Instante de retorno à posição inicial (numérico): {t_initial_position_numerical}")

# Plotar resultados
plt.plot(t_values, y_values, label='Altura (m)')
plt.axvline(t_max_numerical, color='r', linestyle='--', label='Altura Máxima')
plt.axvline(t_initial_position_numerical, color='g', linestyle='--', label='Retorno à Posição Inicial')
plt.xlabel('Tempo (s)')
plt.ylabel('Altura (m)')
plt.title('Movimento da bola com resistência do ar')
plt.legend()
plt.grid(True)
plt.show()


