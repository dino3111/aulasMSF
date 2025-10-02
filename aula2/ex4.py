import numpy as np
import matplotlib.pyplot as plt

# Dados fornecidos no problema
tempo = np.arange(0, 50, 5)  # Tempo em dias, de 0 a 45 com passos de 5 dias
atividade = np.array([9.676, 6.355, 4.261, 2.729, 1.862, 1.184, 0.7680, 0.4883, 0.3461, 0.2119])  # Atividade em mCi

# Criar o gráfico da atividade ao longo do tempo
plt.figure(figsize=(8, 5))
plt.scatter(tempo, atividade, label="Dados experimentais", color='blue')
plt.plot(tempo, atividade, linestyle='dashed', color='blue')
plt.xlabel("Tempo (dias)")
plt.ylabel("Atividade (mCi)")
plt.title("Decaimento da Atividade ao longo do Tempo")
plt.legend()
plt.grid()
plt.show()

# Verificação da lineralidade 

# Aplicar transformação logarítmica para verificar 
log_atividade = np.log(atividade)

# Criar o gráfico do logaritmo da atividade versus tempo
plt.figure(figsize=(8, 5))
plt.scatter(tempo, log_atividade, label="ln(Atividade) vs Tempo", color='red')
plt.xlabel("Tempo (dias)")
plt.ylabel("ln(Atividade) (ln(mCi))")
plt.title("Gráfico de ln(Atividade) vs Tempo")
plt.legend()
plt.grid()
plt.show()

# Sim é linear, porque tem comportamento de uma reta.

# Ajuste linear para encontrar a equação do decaimento
coeficiente_angular, coeficiente_linear = np.polyfit(tempo, log_atividade, 1)
taxa_decaimento = -coeficiente_angular
atividade_inicial = np.exp(coeficiente_linear)

# Exibir a equação encontrada
print(f"A função que descreve a atividade é: A(t) = {atividade_inicial:.4f} * e^(-{taxa_decaimento:.4f} * t)")