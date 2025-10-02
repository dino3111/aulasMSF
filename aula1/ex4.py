import numpy as np
import matplotlib.pyplot as plt

# Lista de N em escala logarítmica de 10 a 10000
N = np.logspace(1, 4, num=20, dtype=int)

# Média e desvio padrão esperados
media_esperada = 5.0
desvio_esperado = 1.0

medias = []

# Simular medições para cada N
for i in N: 
    valores = np.random.normal(media_esperada, desvio_esperado, i) # Gera N números aleatórios com média 5.0 e desvio padrão 1.0
    medias.append(np.mean(valores)) # Calcula a média dos valores

# Criar o gráfico
plt.figure(figsize=(8, 5)) # Tamanho da figura
plt.plot(N, medias, marker='o', label='Médias simuladas') # Gráfico de médias
plt.axhline(media_esperada, color='red', linestyle='--', label='Média esperada') # Linha da média esperada
plt.fill_between(N, media_esperada - desvio_esperado/np.sqrt(N), media_esperada + desvio_esperado/np.sqrt(N), color='gray', alpha=0.2, label='Limites esperados (σ/√N)') # Limites de variação
plt.xscale('log') # Escala logarítmica no eixo x
plt.xlabel('Número de medições (N)') # Rótulo do eixo x
plt.ylabel('Média das medições') # Rótulo do eixo y
plt.title('Média das medições vs. N com limites de variação') # Título do gráfico
plt.legend() # Mostrar legenda
plt.show() # Mostrar gráfico

#Pergunta 2:
# À medida que N aumenta, a média fica mais próxima do valor real porque os erros vão se equilibrando.
# A maioria dos valores fica dentro dos limites, pois eles mostram a variação esperada.
# Com mais medições, o erro diminui e o resultado fica mais preciso.
