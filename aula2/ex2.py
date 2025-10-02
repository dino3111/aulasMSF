# Exercício 2 - Aula 2

import numpy as np
import matplotlib.pyplot as plt

# Alínea a) Dados fornecidos no gráfico
L = np.array([222.0, 207.5, 194.0, 171.5, 153.0, 133.0, 113.0, 92.0])
X = np.array([2.3, 2.2, 2.0, 1.8, 1.6, 1.4, 1.2, 1.0])
plt.figure(figsize=(8,6))
plt.scatter(L, X, color='blue', label="Dados experimentais")
plt.xlabel("L (cm)")
plt.ylabel("X (cm)")
plt.title("Representação da Regressão Linear")
plt.legend()
plt.grid(True)
plt.show()

# Alínea b) Calculo das Quantidades
N = len(L)

soma_L = np.sum(L)
soma_X = np.sum(X)
soma_L2 = np.sum(L**2)
soma_X2 = np.sum(X**2)
soma_LX = np.sum(L * X)

m = (N * soma_LX - soma_L * soma_X) / (N * soma_L2 - soma_L**2)
b = (soma_X - m * soma_L) / N
r2 = ((N * soma_LX - soma_L * soma_X) ** 2) / ((N * soma_L2 - soma_L**2) * (N * soma_X2 - soma_X**2))
im = abs(m) * np.sqrt((1 / r2 - 1) / (N - 2))
ib = im * np.sqrt(soma_L2 / N)

print(f"m: {m}")
print(f"b: {b}")
print(f"Coeficiente de determinação: {r2}")
print(f"Incerteza em m: {im}")
print(f"Incerteza em b: {ib}")

# Alínea c) Representação da Regressão Linear
L_reta = np.linspace(min(L), max(L), 100)
X_reta = m * L_reta + b

plt.figure(figsize=(8,6))
plt.scatter(L, X, color='blue', label="Dados experimentais")
plt.plot(L_reta, X_reta, color='red', label="Ajuste linear")
plt.xlabel("L (cm)")
plt.ylabel("X (cm)")
plt.title("Representação da Regressão Linear")
plt.legend()
plt.grid(True)
plt.show()

# Alínea d) Interpolação
L_interp = 165.0
X_interp = m * L_interp + b
print(f"Para L = {L_interp} cm, o valor interpolado de X é: {X_interp} cm")

# Alínea e) Impacto de um Ponto Alterado na Regressão Linear
# Vamos adicionar um ponto alterado para ver o impacto na regressão linear
X_alterado = X.copy() # Criar uma cópia dos dados originais
X_alterado[3] += 1.0   # Adicionar 1.0 cm ao valor de X na posição 3

soma_X_alterado = np.sum(X_alterado) 
soma_X2_alterado = np.sum(X_alterado**2) 
soma_LX_alterado = np.sum(L * X_alterado)

m_alterado = (N * soma_LX_alterado - soma_L * soma_X_alterado) / (N * soma_L2 - soma_L**2) 
b_alterado = (soma_X_alterado - m_alterado * soma_L) / N

X_reta_alterada = m_alterado * L_reta + b_alterado

plt.figure(figsize=(8,6))
plt.scatter(L, X, color='blue', label="Dados originais")
plt.scatter(L, X_alterado, color='red', label="Dado alterado", marker='o', s=100)
plt.plot(L_reta, X_reta, color='red', linestyle='dashed', label="Ajuste original")
plt.plot(L_reta, X_reta_alterada, color='green', label="Novo ajuste linear")
plt.xlabel("L (cm)")
plt.ylabel("X (cm)")
plt.title("Impacto de um Ponto Alterado na Regressão Linear")
plt.legend()
plt.grid(True)
plt.show()

# Exibir os novos coeficientes
print(f"Nova equação da reta após a alteração: X = {m_alterado}L + {b_alterado}")

# Alínea f)

# Recalcular os valores de m, b e r² com o ponto afastado (alterado)
soma_X_alterado = np.sum(X_alterado)
soma_X2_alterado = np.sum(X_alterado**2)
soma_LX_alterado = np.sum(L * X_alterado)

m_alterado = (N * soma_LX_alterado - soma_L * soma_X_alterado) / (N * soma_L2 - soma_L**2)
b_alterado = (soma_X_alterado - m_alterado * soma_L) / N
r2_alterado = ((N * soma_LX_alterado - soma_L * soma_X_alterado) ** 2) / ((N * soma_L2 - soma_L**2) * (N * soma_X2_alterado - soma_X_alterado**2))

print("\nComparação entre os valores antes e depois da alteração:")
print(f"Coeficiente angular original (m): {m} | Alterado: {m_alterado}")
print(f"Coeficiente linear original (b): {b} | Alterado: {b_alterado}")
print(f"Coeficiente de determinação original (r²): {r2} | Alterado: {r2_alterado}")

# Criando a nova reta ajustada após a alteração
X_reta_alterada = m_alterado * L_reta + b_alterado

# Plotando o gráfico comparando as duas regressões
plt.figure(figsize=(8,6))
plt.scatter(L, X, color='blue', label="Dados originais")
plt.scatter(L, X_alterado, color='red', label="Dado alterado", marker='o', s=100)
plt.plot(L_reta, X_reta, color='red', linestyle='dashed', label="Ajuste original")
plt.plot(L_reta, X_reta_alterada, color='green', label="Novo ajuste linear")
plt.xlabel("L (cm)")
plt.ylabel("X (cm)")
plt.title("Comparação entre Ajustes Originais e Alterados")
plt.legend()
plt.grid(True)
plt.show()

