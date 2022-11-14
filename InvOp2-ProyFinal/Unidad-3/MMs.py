import numpy as np
def factorial(num): 
    if num < 0: 
        print("Factorial de numero negativo")

    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 
lamda = int(input("ingrese valor de λ:"))
tasaserv = int(input("ingrese valor de tasaserv:"))
s = int(input("ingrese cantidad de servidores:"))

P = []
C = []

rho = lamda/tasaserv
P0 = 1-rho
Lq = (P0*((lamda/tasaserv)**s)*rho/(factorial(s)*((P0)**2)))  
Wq = Lq / lamda
W = Wq + (1/tasaserv)
L = Lq + (lamda/tasaserv)

P.append(P0)
pacum = []
for i in range(1, 40):
    Pn = P[-1]
    if(i<=0 and i<=s):
        Pi = (((lamda/tasaserv)**i)/factorial(i))*Pn
    else:
        Pi = (((lamda/tasaserv)**i)/(factorial(s)*(s**(i-s))))*Pn
    P.append(Pi)
    pacum.append(sum(P))

print(f'λ: {lamda}')
print(f'Mu: {tasaserv}')
print(f'c: {s}')
print(f'Wq: {Wq}')
print(f'Lq: {Lq}')
print(f'L: {L}')
print(f'W: {W}')
print(np.array(P))