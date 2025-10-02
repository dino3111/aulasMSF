# exemplo


import numpy as np



# Constantes
m = 0.057  # massa da bola em kg
g = 9.81   # aceleração da gravidade

# Tempos (em segundos)
t = np.array([0.0, 0.2, 0.4])

# Velocidades em m/s nos tempos t0, t1, t2: [vx, vy, vz]
v = np.array([
    [10.0, 5.0, 3.0],   # t0
    [8.0, 4.0, 1.0],    # t1
    [6.0, 2.0, -1.0]    # t2
])

# Alturas (posição z) da bola nos tempos t0, t1, t2
h = np.array([1.2, 0.8, 0.0])  # em metros

# Força de resistência do ar em Newtons: [Fx, Fy, Fz]
Fres = np.array([
    [-0.2, -0.1, -0.05],   # t0
    [-0.25, -0.15, -0.1],  # t1
    [-0.3, -0.2, -0.15]    # t2
])

# 1. Energia mecânica total em cada tempo
Ec = 0.5 * m * np.sum(v**2, axis=1)  # Energia cinética
Ep = m * g * h                       # Energia potencial
Em = Ec + Ep                         # Energia mecânica total

print("Energia Mecânica (J):", Em)

# 2. Trabalho da força de resistência (regra do trapézio)
FdV = np.sum(Fres * v, axis=1)       # Produto escalar F . v
Wres = np.trapz(FdV, t)
print("Trabalho da força de resistência (J):", Wres)

# 3. Trabalho via variação da energia mecânica (conservação de energia)
Wres_energia_02 = Em[2] - Em[0]
print("Trabalho (pela energia mecânica) entre t0 e t2 (J):", Wres_energia_02)
