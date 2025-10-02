import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Exercício 2 - Acelaração Constante
# Um avião arranque do repouso e acelera com aceleração constante 𝑎𝑥 = 3m/s2 até atingir a velocidade de descolagem de 250 km/h.

# 1. Escreve a função que descreve o movimento do avião (lei do movimento) 𝑥(𝑡). Faça o gráfico da lei do movimento.

acelaracao = 3 # m/s^2
velocidadef = 69.44 # m/s (convertido dos 250km/h) / (250*1000/3600) = 69.44
tempof = velocidadef/acelaracao # Tempo para atingir a velocidade final - velocidadefinal/acelaracao

def funcaomovimento(t): 
    return 1.5 * t**2  # x(t) = 1.5 * t^2

t_values = np.linspace(0, tempof, 100)
x_values = funcaomovimento(t_values)
plt.figure(figsize=(8, 5))
plt.plot(t_values, x_values, label='$x(t) = 1.5 t^2$', color='b')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.title('Lei do Movimento do Avião')
plt.legend()
plt.grid()
plt.show()

# Derivada da equação da posição em função do tempo é a velocidade, e o grafico mostra a trajetória do avião.

#2. Em que instante e qual a distância percorrida pelo avião quando atinge a velocidade de descolagem?
#   Encontre a solução com cálculo analítico.

distanciaf = 0.5 * acelaracao * tempof**2 # Distancia percorrida até atingir a velocidade final

print(f"O avião atinge a velocidade de descolagem em {tempof:.2f} segundos.")
print(f"A distância percorrida até esse instante é {distanciaf:.2f} metros.")
# O avião atinge a velocidade de descolagem em 23.15 segundos.
# A distância percorrida até esse instante é 26.72 metros.

# Calculei o tempo necessario para atingir a velocidade de descolagem e a distancia percorrida até esse instante.

# 3. Use sympy.integrate() para integrar a aceleração em função de tempo duas vezes, para obter a velocidade e a
#    posição do avião como funções (simbólicos) de tempo. Está de acordo com o que se esperava? 

t = sp.symbols('t')
velocidade = sp.integrate(acelaracao, t) # Integração da aceleração em função do tempo para obter a velocidade
posicao = sp.integrate(velocidade, t) # Integração da velocidade em função do tempo para obter a posição

velocidade = velocidade.subs('C1', 0) # Constante de integração = 0
posicao = posicao.subs('C2', 0) # Constante de integração = 0
print("Expressão simbólica da velocidade v(t):") 
print(velocidade)
print("Expressão simbólica da posição x(t):")
print(posicao)

# Os resultados obtidos com integração simbólica confirmam exatamente o que tínhamos encontrado analiticamente na Alínea 1. 
# Isto demonstra que a modelação do movimento do avião está correta!

# 4. Use sympy.nsolve() para encontrar o tempo e a posição de descolagem. Concorde com a solução encontrada em 2.?

time_symbol = sp.Symbol('t')
time_solution = sp.nsolve(velocidade - velocidadef, time_symbol, 10)  # Aproximação inicial = 10s
position_solution = posicao.subs(t, time_solution) # Posição de descolagem

print("\nSolução numérica usando sympy.nsolve:")
print(f"Tempo de descolagem: {time_solution:.2f} segundos")
print(f"Posição de descolagem: {position_solution:.2f} metros")

# Comparação com os valores da alínea 2
print("\nComparação com a solução analítica:")
print(f"Tempo analítico: {tempof:.2f} segundos")
print(f"Posição analítica: {distanciaf:.2f} metros")

# Os valores são praticamente identicos, entao confirma que os calculos anteriores estao corretos,
# Então, os métodos numéricos e analíticos estão de acordo!





