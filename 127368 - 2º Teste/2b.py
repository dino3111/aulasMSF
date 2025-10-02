# Claudino José Martins - 127368

import matplotlib.pyplot as plt
import numpy as np

dt = 0.001
t = np.arange(0, 200+dt, dt)

ax = np.zeros(t.size)
vx = np.zeros(t.size)
x = np.zeros(t.size)

u = 0.005               
Cres = 0.8              
area = 0.3              
Par = 1.225             
m = 75                  
Potencia = 250           
vx[0] = 2               
g = 9.8
N = m * g               

for i in range(t.size-1):
    if vx[i] < 0.1:     
        vx[i] = 0.1
    Fcic = Potencia / vx[i]
    FRes = -(Cres/2) * area * Par * abs(vx[i]) * vx[i]
    FRol = -u * N
    F = Fcic + FRes + FRol

    ax[i] = F / m
    vx[i+1] = vx[i] + ax[i] * dt
    x[i+1] = x[i] + vx[i] * dt

print("Vel Terminal: " + str(vx[vx.argmax()])) # Vel Terminal: 11.23911746246343 m/s

for i in range(x.size-1):
    if(x[i] == 3000): 
        print(t[np.where(x == x[i])])
    elif(x[i] > 3000): 
        t1 = t[np.where(x == x[i])]
        t2 = t[np.where(x == x[i-1])]
        tmed = (t1+t2)/2
        print(tmed)
print("Tempo que demora a percorrer 3km: ", end="")
