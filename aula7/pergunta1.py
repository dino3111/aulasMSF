# Pergunta 1
import numpy as np
import matplotlib.pyplot as plt

# Definição da função da pista: y = f(x)
def f(x):
    return 0.5 * np.exp(-0.05 * x) * x  # Exemplo de uma curva suave decrescente

# Derivada da função f(x) (declive da pista)
def df(x):
    return 0.5 * np.exp(-0.05 * x) * (1 - 0.05 * x)

# Aceleração ao longo da pista
def acceleration(x, g=9.81):
    f_prime = df(x)
    return -g * f_prime / np.sqrt(1 + f_prime**2)

# Geração dos pontos para x
x_vals = np.linspace(0, 20, 200)
y_vals = f(x_vals)
a_vals = acceleration(x_vals)

# Gráfico da pista
plt.subplot(1, 2, 1)
plt.plot(x_vals, y_vals, label='Pista: y = f(x)')
plt.title('Forma da pista')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

# Gráfico da aceleração
plt.subplot(1, 2, 2)
plt.plot(x_vals, a_vals, color='orange', label='Aceleração $a_x$')
plt.title('Aceleração ao longo da pista')
plt.xlabel('x')
plt.ylabel('Aceleração $a_x$ (m/s²)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

# Resposta:
# A aceleração da bola resulta da força da gravidade projetada na direção da pista. Como a gravidade atua na vertical, apenas uma parte dela contribui para o movimento ao longo da pista — essa parte é a componente tangencial. A direção da pista é dada pela inclinação f´(x) por isso a componente tangencial da gravidade é proporcional a -gf´(x). Assim, obtém-se diretamente a fórmula da aceleração: ar = -gf´(x). 

