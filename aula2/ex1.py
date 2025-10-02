# Exercício 1 - Aula 2

import numpy as np
import matplotlib.pyplot as plt

def regressao_linear(x, y):
    N = len(x)  # Número de elementos na amostra

    soma_x = np.sum(x)  # Soma dos valores de x
    soma_y = np.sum(y)  # Soma dos valores de y
    soma_x2 = np.sum(x**2)  # Soma dos quadrados dos valores de x
    soma_y2 = np.sum(y**2)  # Soma dos quadrados dos valores de y
    soma_xy = np.sum(x * y)  # Soma dos produtos x * y

    # Cálculo do m
    m = (N * soma_xy - soma_x * soma_y) / (N * soma_x2 - soma_x**2)
    
    # Cálculo do b
    b = (soma_y - m * soma_x) / N
    
    # Cálculo do coeficiente de determinação (r²)
    r2 = ((N * soma_xy - soma_x * soma_y) ** 2) / ((N * soma_x2 - soma_x**2) * (N * soma_y2 - soma_y**2))
    
    # Cálculo da incerteza em m (Δm)
    im = abs(m) * np.sqrt((1 / r2 - 1) / (N - 2))
    
    # Cálculo da incerteza em b (Δb)
    ib = im * np.sqrt(soma_x2 / N)

    return m, b, r2, im, ib

