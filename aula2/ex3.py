# Exercício 3 - Aula 2

import matplotlib.pyplot as plt
import numpy as np

# Dados fornecidos
T = np.array([200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100])
E = np.array([0.6950, 4.363, 15.53, 38.74, 75.08, 125.2, 257.9, 344.1, 557.4, 690.7])

# Criando o gráfico
plt.figure(figsize=(8, 5))
plt.scatter(T, E, color='red', label='Dados experimentais')
plt.xlabel('Temperatura (K)')
plt.ylabel('Energia Emitida (J)')
plt.title('Relação entre Energia Emitida e Temperatura')
plt.grid(True)
plt.legend()
plt.show()
