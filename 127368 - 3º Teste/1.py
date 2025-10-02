import numpy as np
import matplotlib.pyplot as plt



# a)

m = 0.5      
k = 2        
b = 0.2      
x0 = 2       
v0 = 2       

ti = 0
tf = 30
dt = 0.001
n = int((tf - ti) / dt)

t = np.linspace(ti, tf, n + 1)

def osc_amortecido_1D(x0, v0, k, b, m, n, dt):
    x = np.empty(n + 1)
    v = np.empty(n + 1)
    a = np.empty(n + 1)
    x[0] = x0
    v[0] = v0
    for i in range(n):
        a[i] = (-k * x[i] - b * v[i]) / m
        v[i + 1] = v[i] + a[i] * dt
        x[i + 1] = x[i] + v[i + 1] * dt
    return x, v

x, v = osc_amortecido_1D(x0, v0, k, b, m, n, dt)

plt.figure()
plt.plot(t, x)
plt.xlabel("t (s)")
plt.ylabel("x (m)")
plt.title("Posição vs Tempo")
plt.grid()
plt.show()

plt.figure()
plt.plot(t, v)
plt.xlabel("t (s)")
plt.ylabel("v (m/s)")
plt.title("Velocidade vs Tempo")
plt.grid()
plt.show()



# b)

max_indices = []
for i in range(1, len(x)-1):
    if x[i-1] < x[i] and x[i] > x[i+1]:
        max_indices.append(i)
    if len(max_indices) == 4:
        break

maximos_lagrange = []
tempos_maximos = []

for idx in max_indices:
    if idx == 0:
        pts = [idx, idx+1, idx+2]
    elif idx == len(x)-1:
        pts = [idx-2, idx-1, idx]
    else:
        pts = [idx-1, idx, idx+1]
    t_pts = t[pts]
    x_pts = x[pts]

    coef = np.polyfit(t_pts, x_pts, 2)
    a, b_coef, c = coef
    t_max = -b_coef / (2 * a)
    x_max = np.polyval(coef, t_max)
    tempos_maximos.append(t_max)
    maximos_lagrange.append(x_max)

for i, (tm, xm) in enumerate(zip(tempos_maximos, maximos_lagrange), 1):
    print(f"Máximo {i}: t = {tm} s, x = {xm} m")

# Máximos:
# 1: t = 0.22190125849647985 s, x = 2.2217679723454724 m
# 2: t = 3.37900755685463 s, x = 1.181465581082172 m
# 3: t = 6.536113850698465 s, x = 0.6282658390326716 m
# 4: t = 9.693220140023199 s, x = 0.33409180158516705 m

# Os valores dos máximos locais da posição diminuem progressivamente, evidenciando o efeito do amortecimento no sistema. 
# Ocorre porque a energia do sistema é dissipada ao longo do tempo, reduzindo a amplitude das oscilações.



# c) 

intervalos = np.diff(tempos_maximos)

periodo_medio = np.mean(intervalos)

frequencia = 1 / periodo_medio

print(intervalos)
print(periodo_medio)
print(frequencia)

# Intervalos entre máximos: [3.1571063  3.15710629 3.15710629]
# Período médio: 3.1571062938422396 s
# Frequência estimada: 0.31674574972355046 Hz