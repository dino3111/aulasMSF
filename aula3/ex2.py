import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Exercício 2 -  Volante de badmington (aceleração uma função de velocidade)

# 1. Escrever a função que descreve o movimento do volante de badminton (lei do movimento) y(t) e fazer o gráfico

v_T = 6.80  # Velocidade terminal (m/s)
g = 9.81  # Aceleração da gravidade (m/s^2)

def y_t(t, v_T, g): # Definição da lei do movimento
    return (v_T**2 / g) * np.log(np.cosh(g * t / v_T)) # y(t) = (v_T^2 / g) * ln(cosh(g * t / v_T))

# Criar vetor de tempo de 0 a 4s
t_values = np.linspace(0, 4, 100)
y_values = y_t(t_values, v_T, g)

# Plotar o gráfico da posição y(t)
plt.figure(figsize=(8, 5))
plt.plot(t_values, y_values, label='$y(t)$', color='b')
plt.xlabel('Tempo (s)')
plt.ylabel('Altura (m)')
plt.title('Lei do Movimento do Volante de Badminton')
plt.legend()
plt.grid()
plt.show()

# O gráfico mostra que a altura diminui rapidamente no início, mas depois a queda fica mais lenta devido à resistência do ar.

# 2. Determinar a velocidade instantânea v(t) simbolicamente e  gráfico

t = sp.Symbol('t')
y_t_sym = (v_T**2 / g) * sp.log(sp.cosh(g * t / v_T)) # Expressão simbólica da posição y(t)
velocidade_t = sp.diff(y_t_sym, t)  # Derivada da posição para obter velocidade

# Converter para função numérica
velocidade_func = sp.lambdify(t, velocidade_t, 'numpy') # Converte a expressão simbólica numa função numérica
v_values = velocidade_func(t_values) # Calcular os valores da velocidade para os tempos t_values

# Gráfico da velocidade v(t)
plt.figure(figsize=(8, 5))
plt.plot(t_values, v_values, label='$v(t)$', color='r')
plt.xlabel('Tempo (s)')
plt.ylabel('Velocidade (m/s)')
plt.title('Velocidade do Volante de Badminton')
plt.legend()
plt.grid()
plt.show()

print("Expressão simbólica da velocidade v(t):")
print(velocidade_t)

# O gráfico mostra que a velocidade aumenta rapidamente no início, mas depois estabiliza perto da velocidade terminal.

# 3. Determinar a aceleração instantânea a(t) simbolicamente e Gráfico

aceleracao_t = sp.diff(velocidade_t, t)  # Derivada da velocidade para obter aceleração

# Converter para função numérica
aceleracao_func = sp.lambdify(t, aceleracao_t, 'numpy') # Converte a expressão simbólica numa função numérica
a_values = aceleracao_func(t_values) # Calcular os valores da aceleração para os tempos t_values

# Plotar o gráfico da aceleração a(t)
plt.figure(figsize=(8, 5))
plt.plot(t_values, a_values, color='g')
plt.xlabel('Tempo (s)')
plt.ylabel('Aceleração (m/s²)')
plt.title('Aceleração do Volante de Badminton')
plt.legend()
plt.grid()
plt.show()

print("Expressão simbólica da aceleração a(t):")
print(aceleracao_t)

#O gráfico mostra que a aceleração diminui com o tempo, pois a resistência do ar reduz a força resultante.

# 4. Mostrar que a aceleração é compatível com a equação a_y = g - (g / v_T^2) * v_y * |v_y|

# Definir expressão teórica da aceleração
a_teorico = g - (g / v_T**2) * velocidade_t * sp.Abs(velocidade_t)

a_teorico_func = sp.lambdify(t, a_teorico, 'numpy')

a_teorico_values = a_teorico_func(t_values) # Calcular os valores da aceleração teórica para os tempos t_values

plt.figure(figsize=(8, 5))
plt.plot(t_values, a_teorico_values, color='blue')
plt.plot(t_values, a_values, color='g')
plt.xlabel('Tempo (s)')
plt.ylabel('Aceleração (m/s^2)')
plt.title('Comparação com a equação da alínea anterior')
plt.grid()

plt.show()

#DADO QUE OS GRÁFICOS OBTIDOS SÃO IGUAIS, AMBAS AS FÓRMULAS SÃO COMPATÍVEIS.

# 5. Determinar o tempo para atingir o solo quando y(tempo) = 20m e comparar com a queda livre

y0 = 20  # Altura inicial
y_t = (v_T**2 / g) * sp.log(sp.cosh((g * t) / v_T)) - y0

t_queda_resistencia_do_ar = sp.nsolve(y_t, t, 2)  # Aproximação inicial de 2s
t_queda_livre = sp.sqrt(2 * y0 / g)  # Tempo de queda sem resistência do ar

print(f"O tempo de queda com resistência do ar é {t_queda_resistencia_do_ar:.2f} s, enquanto sem resistência do ar é {t_queda_livre:.2f} s.")

#  O tempo de queda com resistência do ar é maior, pois a força de arrasto reduz a aceleração.