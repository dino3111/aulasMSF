import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Dados da órbita
t = np.linspace(0, 2 * np.pi, 100)
x = np.cos(t)
y = np.sin(t)

# Criar figura
fig, ax = plt.subplots()
terra, = ax.plot([], [], 'bo', label='Terra')       # Terra (ponto azul)
trilha, = ax.plot([], [], 'b-', linewidth=1)        # Linha do movimento (trilha)
ax.plot(0, 0, 'yo', label='Sol')                    # Sol (ponto amarelo)

# Configuração do gráfico
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.grid(True) 
ax.legend(loc='upper right')


# Inicialização
def init():
    terra.set_data([], [])
    trilha.set_data([], [])
    return terra, trilha

# Atualização da animação
def update(frame):
    terra.set_data([x[frame]], [y[frame]])              # Atualiza posição
    trilha.set_data(x[:frame+1], y[:frame+1])           # Atualiza linha da trajetória
    return terra, trilha

# Criar animação
ani = FuncAnimation(fig, update, frames=len(x), init_func=init, interval=50, blit=True)

# Mostrar
plt.show()