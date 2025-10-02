# Claudino José Martins - 127368

import numpy as np
import matplotlib.pyplot as plt

L = np.array([1.2, 4.2, 11, 20, 22, 37, 45])
X = np.array([0.03, 0.54, 9.1, 38, 57, 230, 480])
x = L
y = X
npontos = x.size

y = np.log(y)

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

errom= np.abs(m)*np.sqrt(((1/r2)-1)/(n-2)) 

print("O valor do declive m = ", m)
# O valor do declive m =  0.19329499827571386
print("O erro associado ao declive = ",errom)
# O erro associado ao declive =  0.038411731742998514
print("O coeficiente de determinação r**2 = ", r2)
# O coeficiente de determinação r**2 =  0.8351081253935738

equacao=m*x+b
plt.plot(x, equacao,label="Reta de regressao linear") # reta
plt.scatter(x, y, marker='o', color='m',label="Pontos") # pontos
plt.xlabel("Comprimento do Fêmur (cm)")
plt.ylabel("Massa (kg)")
plt.legend("Exercício 1. B")
plt.grid(True)
plt.show()

# -----------------------------------------------------------------------

L = np.array([1.2, 4.2, 11, 20, 22, 37, 45])
X = np.array([0.03, 0.54, 9.1, 38, 57, 230, 480])
x = L
y = X
npontos = x.size

x = np.log(x) 
y = np.log(y) 

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

errom= np.abs(m)*np.sqrt(((1/r2)-1)/(n-2))

print("\nO declive m = ", m, "+/-", errom)
# O declive m =  2.6669805798913058 +/- 0.05887341253330232
print("O erro associado ao declive = ",errom)
# O erro associado ao declive =  0.05887341253330232
print("O coeficiente de determinação r**2 = ", r2)
# O coeficiente de determinação r**2 =  0.9975694092514619

equacao=m*x+b
plt.plot(x, equacao,label="Reta de regressao linear") 
plt.scatter(x, y, marker='o', color='m',label="Pontos") 
plt.xlabel("Comprimento do Fêmur (cm)")
plt.ylabel("Massa (kg)")
plt.legend("Exercício 1. B")
plt.grid(True)
plt.show()

