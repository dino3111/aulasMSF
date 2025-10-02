import numpy as np
import matplotlib.pyplot as plt

# Exercício 1 - Aula prática 4

# Uma bola de ténis é largada de uma altura elevada. Considere a queda livre, sem resistência do ar.
# Considere que a aceleração vertical é 𝑔 = 9.80 m/s

# a) Construa um programa que determine a posição do objeto, usando o método de Euler, no intervalo de tempo 0,4s.

# Dados
g = 9.80  # aceleração da gravidade (m/s^2)
dt = 0.01  # passo de tempo (s)
t_final = 4.0  # tempo final (s)

# Condições iniciais
t = 0.0  # tempo inicial (s)
y = 100.0  # altura inicial (m) (podes mudar)
v = 0.0  # velocidade inicial (m/s)

# Listas para armazenar os valores de tempo, posição e velocidade
tempo = [t]
posicao = [y]
velocidade = [v]

# Loop do Método de Euler
while t < t_final:
    v = v - g * dt  # Atualiza velocidade (a = -g)
    y = y + v * dt  # Atualiza posição
    
    t += dt  # Atualiza tempo
    
    tempo.append(t)
    posicao.append(y)
    velocidade.append(v)

# b) Qual a velocidade no instante 3s?
# Encontrar o valor de velocidade correspondente ao tempo mais próximo de 3s
menor_diferenca = float('inf')
indice_3s = 0
for i in range(len(tempo)):
    diferenca = abs(tempo[i] - 3.0)
    if diferenca < menor_diferenca:
        menor_diferenca = diferenca
        indice_3s = i

velocidade_3s = velocidade[indice_3s]

print(f"A velocidade no instante 3s é aproximadamente {velocidade_3s:.2f} m/s.")

# c) Repita as alíneas anteriores, com um passo de tempo 10 vezes menor.

# Dados
dt = 0.001  # passo de tempo 10 vezes menor (s)

# Condições iniciais
t = 0.0  # tempo inicial (s)
y = 100.0  # altura inicial (m) (podes mudar)
v = 0.0  # velocidade inicial (m/s)

# Listas para armazenar os valores de tempo, posição e velocidade
tempo_fino = [t]
posicao_fino = [y]
velocidade_fino = [v]

# Loop do Método de Euler com passo menor
while t < t_final:
    v = v - g * dt  # Atualiza velocidade (a = -g)
    y = y + v * dt  # Atualiza posição
    
    t += dt  # Atualiza tempo
    
    tempo_fino.append(t)
    posicao_fino.append(y)
    velocidade_fino.append(v)

# Encontrar a velocidade no instante 3s para dt menor
menor_diferenca_fino = float('inf')
indice_3s_fino = 0
for i in range(len(tempo_fino)):
    diferenca_fino = abs(tempo_fino[i] - 3.0)
    if diferenca_fino < menor_diferenca_fino:
        menor_diferenca_fino = diferenca_fino
        indice_3s_fino = i

velocidade_3s_fino = velocidade_fino[indice_3s_fino]

print(f"A velocidade no instante 3s com passo menor é aproximadamente {velocidade_3s_fino:.2f} m/s.")

# Comparação gráfica dos dois passos de tempo
plt.figure(figsize=(8,5))
plt.plot(tempo, posicao, label="Posição (dt=0.01s)")
plt.plot(tempo_fino, posicao_fino, label="Posição (dt=0.001s)", linestyle='dashed')
plt.xlabel("Tempo (s)")
plt.ylabel("Altura (m)")
plt.title("Comparação - Queda Livre - Método de Euler")
plt.legend()
plt.grid()
plt.show()

# d) Compare o resultado obtido em b) e c) com o resultado exato. Que conclui?
# O resultado obtido em b) e c) é aproximado, uma vez que o método de Euler é uma aproximação numérica.
# O resultado exato para a velocidade no instante 3s é -29.4 m/s.
# Mas tem um erro de 0.6m para o passo de tempo de 0.01s e 0.04m para o passo de tempo de 0.001s.

# e) Qual a posição em 3s, se o objeto partiu da posição 0 m? (Usa o passo de tempo da alínea b).)

# Dados modificados
t = 0.0  # tempo inicial (s)
y = 0.0  
v = 0.0  # velocidade inicial (m/s)

tempo_novo = [t]
posicao_nova = [y]

# Loop do Método de Euler com dt = 0.01s
while t < t_final:
    v = v - g * dt  # Atualiza velocidade (a = -g)
    y = y + v * dt  # Atualiza posição
    
    t += dt  # Atualiza tempo
    
    tempo_novo.append(t)
    posicao_nova.append(y)

# Encontrar a posição no instante 3s
menor_diferenca_nova = float('inf')
indice_3s_novo = 0
for i in range(len(tempo_novo)):
    diferenca_nova = abs(tempo_novo[i] - 3.0)
    if diferenca_nova < menor_diferenca_nova:
        menor_diferenca_nova = diferenca_nova
        indice_3s_novo = i

posicao_3s_nova = posicao_nova[indice_3s_novo]

print(f"\nA posição no instante 3s, partindo de 0 m, é aproximadamente {posicao_3s_nova:.2f} m.")

# f) Repita a alínea anterior, com um passo de tempo 10 vezes menor.

# Novas condições com passo menor
dt_fino = 0.001  # Passo de tempo 10 vezes menor
t = 0.0  # Tempo inicial (s)
y = 0.0  # Altura inicial (m)
v = 0.0  # Velocidade inicial (m/s)

tempo_novo_fino = [t]
posicao_nova_fino = [y]

# Loop do Método de Euler com dt = 0.001s
while t < t_final:
    v = v - g * dt_fino  # Atualiza velocidade (a = -g)
    y = y + v * dt_fino  # Atualiza posição
    
    t += dt_fino  # Atualiza tempo
    
    tempo_novo_fino.append(t)
    posicao_nova_fino.append(y)

# Encontrar a posição no instante 3s para dt menor
menor_diferenca_nova_fino = float('inf')
indice_3s_novo_fino = 0
for i in range(len(tempo_novo_fino)):
    diferenca_nova_fino = abs(tempo_novo_fino[i] - 3.0)
    if diferenca_nova_fino < menor_diferenca_nova_fino:
        menor_diferenca_nova_fino = diferenca_nova_fino
        indice_3s_novo_fino = i

posicao_3s_nova_fino = posicao_nova_fino[indice_3s_novo_fino]

print(f"A posição no instante 3s, partindo de 0 m, com passo menor, é aproximadamente {posicao_3s_nova_fino:.2f} m.")

# g) Compare o resultado obtido em e) e f) com o resultado exato. Que conclui?
# O resultado obtido em e) e f) é aproximado, uma vez que o método de Euler é uma aproximação numérica, logo a posição no instante 3 segundos,
# é igual a -44.11 m, sem ou com passo menor.
# Mas tem um erro de 0.01m para o passo de tempo de 0.01s e 0.001m para o passo de tempo de 0.001s.

# h) Calcule novamente a posição no instante 2s, para vários valores do. Faça o gráfico do desvio do valor
# aproximado com o valor exato em função do passo. Como varia o erro com o passo?

dt_values = [0.1, 0.05, 0.01, 0.005, 0.001, 0.0005, 0.0001]
erros = []
t_final = 2.0  # Tempo final de 2s

# Cálculo do valor exato da posição no instante 2s
y_exato = 100.0 - 0.5 * g * (2.0 ** 2)

for dt in dt_values:
    t = 0.0  # Tempo inicial (s)
    y = 100.0  # Altura inicial (m)
    v = 0.0  # Velocidade inicial (m/s)
    
    while t < t_final:
        v = v - g * dt  # Atualiza velocidade (a = -g)
        y = y + v * dt  # Atualiza posição
        t += dt  # Atualiza tempo
    
    erro = abs(y - y_exato)
    erros.append(erro)

# Gráfico do erro em função do passo de tempo
plt.figure(figsize=(8,5))
plt.plot(dt_values, erros, marker='o', linestyle='-', label='Erro numérico')
plt.xscale('log')
plt.yscale('log')
plt.xlabel("Passo de Tempo (s)")
plt.ylabel("Erro Absoluto (m)")
plt.title("Erro da Posição no Instante 2s vs. Passo de Tempo")
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()

# Conclusão:
# O erro diminui à medida que o passo de tempo (dt) é reduzido, mas nunca desaparece completamente.
# O método de Euler tem um erro proporcional a dt, explicando a tendência observada no gráfico.
