import numpy as np
import matplotlib.pyplot as plt

# Parâmetros ajustados
d = 0.1          # diâmetro das esferas (m)
l = 1.0          # comprimento da corda (m) - mais estável que 10d
m = 0.3          # massa da esfera (kg)
g = 9.8          # aceleração gravitacional (m/s²)
k = 1e5          # constante da força elástica REDUZIDA (era 1e7)
N = 2            # número de esferas
dt = 1e-5        # passo de tempo reduzido (era 1e-4)
t_final = 2      # tempo final reduzido para análise inicial (era 5)

n_steps = int(t_final / dt)

# Vetores de estado
x = np.zeros((n_steps, N))
v = np.zeros((n_steps, N))

# Condições iniciais
x[0, 0] = -5 * d
x[0, 1] = d

# Funções auxiliares revisadas
def acc_elastica(dx, d):
    """Força elástica apenas quando as esferas estão comprimidas"""
    if dx < d:
        return k * (d - dx)  # Força linear de repulsão
    return 0.0

def acc_i(i, x_inst):
    """Aceleração da esfera i"""
    a = 0
    
    # Forças elásticas com vizinhos
    if i > 0:
        a += acc_elastica(x_inst[i] - x_inst[i-1], d) / m
    if i < N-1:
        a -= acc_elastica(x_inst[i+1] - x_inst[i], d) / m
    
    # Força gravitacional (pêndulo)
    a -= (g/l) * (x_inst[i] - d*i)
    
    return a

# Verificação de estabilidade numérica
def check_stability():
    """Verifica se os parâmetros são estáveis"""
    omega = np.sqrt(g/l)  # Frequência do pêndulo
    omega_elast = np.sqrt(k/m)  # Frequência da mola
    
    print(f"Frequência do pêndulo: {omega:.2f} rad/s")
    print(f"Frequência elástica: {omega_elast:.2f} rad/s")
    print(f"dt deve ser << {min(1/omega, 1/omega_elast):.2e} s")
    print(f"Seu dt: {dt:.2e} s")

check_stability()

# Simulação com verificação de overflow
for t in range(n_steps - 1):
    for i in range(N):
        a = acc_i(i, x[t])
        v[t+1, i] = v[t, i] + a * dt
        x[t+1, i] = x[t, i] + v[t+1, i] * dt
        
        # Verificação de overflow
        if not np.isfinite(x[t+1, i]) or not np.isfinite(v[t+1, i]):
            raise RuntimeError(f"Overflow detectado no passo {t} para esfera {i}")

# Cálculo de energias e momento
def calcular_energias(x, v):
    """Calcula energias de forma vetorizada para eficiência"""
    Ec = 0.5 * m * np.sum(v**2, axis=1)
    
    # Energia potencial gravitacional
    x_eq = np.array([d*i for i in range(N)])
    Ep_grav = 0.5 * m * (g/l) * np.sum((x - x_eq)**2, axis=1)
    
    # Energia potencial elástica
    Ep_elast = np.zeros_like(Ep_grav)
    for i in range(N-1):
        dx = x[:, i+1] - x[:, i]
        mask = dx < d
        Ep_elast[mask] += 0.5 * k * (d - dx[mask])**2
    
    return Ec, Ep_grav, Ep_elast

Ec, Ep_grav, Ep_elast = calcular_energias(x, v)
momentum_total = m * np.sum(v, axis=1)
energia_total = Ec + Ep_grav + Ep_elast

# Plotagem com limites razoáveis
tempo = np.linspace(0, t_final, n_steps)

plt.figure(figsize=(15, 10))

# Posições
plt.subplot(2, 2, 1)
plt.plot(tempo, x[:, 0], label='Esfera 0')
plt.plot(tempo, x[:, 1], label='Esfera 1')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.title('Posição das Esferas')
plt.legend()
plt.grid()

# Momento
plt.subplot(2, 2, 2)
plt.plot(tempo, momentum_total)
plt.xlabel('Tempo (s)')
plt.ylabel('Momento Total (kg·m/s)')
plt.title('Conservação do Momento Linear')
plt.grid()

# Energias
plt.subplot(2, 2, 3)
plt.plot(tempo, Ec, label='Energia Cinética')
plt.plot(tempo, Ep_grav, label='En. Pot. Gravitacional')
plt.plot(tempo, Ep_elast, label='En. Pot. Elástica')
plt.plot(tempo, energia_total, 'k--', label='Energia Total')
plt.xlabel('Tempo (s)')
plt.ylabel('Energia (J)')
plt.title('Conservação de Energia')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()