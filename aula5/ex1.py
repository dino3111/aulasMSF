# Exercício 1: Vetores de um robô

# Um simples robô pode deslocar-se no chão executando dois tipos de instruções. 
# Pode rodar por um determinado ângulo, e pode avançar em linha reta uma 
# determinada distância. 

# As instruções são dados ao robô na forma de tuples (ang,dist), que significa que o 
# robô deve rodar por um ângulo ang (em graus) no sentido horário e depois 
# avançar uma distância dist (metros).

# O robô começa na origem, orientado ao longo do eixo x. É-lhe dada a seguinte 
# sequência de instruções:

# (45,3), (90,2), (45,3), (45,2), (90,3)

import matplotlib.pyplot as plt
import numpy as np

# a) Calcule a posição do robô após cada passo. Faça um gráfico da trajetória do robô.

# Instruções dadas ao robô (ângulo em graus, distância em metros)
instrucoes = [(45, 3), (90, 2), (45, 3), (45, 2), (90, 3)]

# Posição e direção inicial
x, y = 0, 0
angulo_total = 0  # inicialmente apontando para o eixo x

# Para armazenar as posições
trajetoria = [(x, y)]

# Criar a figura
plt.figure()
plt.axis('equal')

# Executar cada instrução
for ang, dist in instrucoes:
    angulo_total -= ang  # sentido horário => subtrair
    rad = np.radians(angulo_total)  # converter para radianos

    # Calcular deslocamento
    dx = dist * np.cos(rad)
    dy = dist * np.sin(rad)

    # Desenhar seta
    plt.arrow(x, y, dx, dy, color='blue', width=0.05, length_includes_head=True)

    # Atualizar posição
    x += dx
    y += dy
    trajetoria.append((x, y))

# Marcar a trajetória com pontos
trajetoria = np.array(trajetoria)
plt.plot(trajetoria[:,0], trajetoria[:,1], 'ro--', label='Trajetória')

# Melhorar o gráfico
plt.title("Trajetória do Robô")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.grid(True)
plt.legend()
plt.show()

# b) Quais são as coordenadas finais do robô?

print(f"Coordenadas finais do robô: ({x:.2f}, {y:.2f})")
# Coordenadas finais do robô: (-1.59, -0.00)

# c) Qual é a instrução necessária para fazer o robô retornar ao ponto inicial?

# Vetor de retorno para o sentido oposto (do ponto final até a origem)
dx_retorno = -x 
dy_retorno = -y 

# Distância até a origem
dist_retorno = np.hypot(dx_retorno, dy_retorno) # calculo da hipotenusa (distância) 

# Ângulo do vetor retorno em relação ao eixo x (em graus)
angulo_vetor = np.degrees(np.arctan2(dy_retorno, dx_retorno))

# Diferença entre a direção atual e a direção para a origem
ang_girar = (angulo_total - angulo_vetor) % 360  # rotação no sentido horário

print(f"\nPara retornar ao ponto inicial:")
print(f"Deve rodar {ang_girar:.2f}° no sentido horário")
print(f"E avançar {dist_retorno:.2f} metros")
print(f"Instrução final: ({ang_girar:.2f}, {dist_retorno:.2f})")


# Pergunta 1:
somaang = 45 + 90 + 45 + 45 + 90
print(f"\nSoma dos ângulos: {somaang}°")
orientaçaoininitial = 360 - somaang
print(f"Orientação inicial: {orientaçaoininitial}°")

# Resposta : A soma dos ângulos em que o robô rodou para regressar à origem são 45 + 90 + 45 + 45 + 90 = 315°. 
# E em geral, a rotação que seria necessária para que o robô voltasse à origem seria de 360 - 315 = 45°, tudo no sentido horário.
