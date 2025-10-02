# EXERCÍCIO 3 - AULA PRÁTICA 1

import numpy as np
import matplotlib.pyplot as plt

N = 10  # Tamanho da amostra

X = np.random.normal(4.5, 0.5, size=N) # Gera 10 números aleatórios com média 4.5 e desvio padrão 0.5
Xmedia = np.mean(X) 
Xerro = np.std(X) / np.sqrt(N) 
print(Xmedia, Xerro)

Y = np.random.normal(10.0, 1.0, size=N) # Gera 10 números aleatórios com média 10.0 e desvio padrão 1.0
Ymedia = np.mean(Y)
Yerrou = np.std(Y) / np.sqrt(N)
print(Ymedia, Yerrou)

Z = X + Y
Zmedia = np.mean(Z)
print(Zmedia)

Zerro_direct = np.std(Z) / np.sqrt(N) # incerteza de Z diretamente do desvio padrão
print(Zerro_direct)

Zerro_propag = np.sqrt(Xerro**2 + Yerrou**2) # incerteza de Z pela propagação de incertezas
print(Zerro_propag)

W = X * Y
Wmedia = np.mean(W)
print(Wmedia)

Werro_direct = np.std(W) / np.sqrt(N) # incerteza de W diretamente do desvio padrão
print(Werro_direct)

Werro_propag = Wmedia * np.sqrt((Xerro / Xmedia)**2 + (Yerrou / Ymedia)**2) # incerteza de W pela propagação de incertezas
print(Werro_propag)



# Pergunta 1:
# Sim, as fórmulas de propagação de erros (ii) e o método direto (i) são muito parecidas. 
# Pequenas diferenças podem aparecer por causa do acaso nas medições, mas, com mais medições os dois métodos vão se aproximar cada vez mais.


