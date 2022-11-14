import numpy as np
lamda = int(input("ingrese valor de λ:"))
tasaserv = int(input("ingrese valor de tasaserv:"))
Q_servidores = 1

P = []
C = []

rho = lamda/tasaserv
L = lamda/(tasaserv-lamda)  
W = 1/(tasaserv-lamda)  
Wq = lamda/(tasaserv*(tasaserv-lamda))  
Lq = Wq * lamda  

P0 = 1-rho
P.append(P0)
pacum = []
for i in range(1, 40):
    Pn = P[-1]
    Pi = Pn * rho
    P.append(Pi)
    pacum.append(sum(P))

print(np.array(P))
print(np.array(pacum))