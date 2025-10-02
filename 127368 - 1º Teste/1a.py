# Claudino José Martins - 127368

import numpy as np
import matplotlib.pyplot as plt

L = np.array([1.2, 4.2, 11, 20, 22, 37, 45]) 
X = np.array([0.03, 0.54, 9.1, 38, 57, 230, 480]) 

x = L
y = X
npontos = len(X) 

xy = x*y
xx = x**2
yy = y**2

sx = x.sum()
sy = y.sum()
sxy = xy.sum()
sxx = xx.sum()
syy = yy.sum()

n = npontos
m = (n*sxy - sx*sy)/(n*sxx - sx**2)
b = (sxx*sy - sx*sxy)/(n*sxx - sx**2)
r2 = (n*sxy - sx*sy)**2/((n*sxx - sx**2)*(n*syy - sy**2))

equacao=m*x+b
plt.plot(x, equacao, label="Reta de regressão linear") 
plt.scatter(x, y, marker='o', color='m',label="Pontos")
plt.xlabel("Comprimento do Fêmur (cm)")
plt.ylabel("Massa (kg)")
plt.legend("Exercício 1. A")
plt.grid(True)
plt.show()

print("\nO Coeficiente de Determinação r**2 = ", r2)
# O Coeficiente de Determinação r**2 =  0.8151276625448709
