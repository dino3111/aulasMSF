# Dados
P = 18.2
erroP = 0.1
Q = 10.7
erroQ = 0.2

# a)
S = P + Q
erroS = erroP + erroQ 

# b)
D = P - Q
erroD = erroP + erroQ 

# c)
M = P * Q
erroM = M * ((erroP / P) + (erroQ / Q))  

print(f' S = {S} +/- {erroS} cm \n D = {D} +/- {erroD} cm \n M = {M} {erroM}')
