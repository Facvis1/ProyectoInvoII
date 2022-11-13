import numpy as np
import nashpy as nash

A = np.array([[4, 0], [0, 2]])
B = np.array([[2, 0], [0, 4]])
Juego = nash.Game(A, B)
Juego
getEquilibrium= lambda: Juego.support_enumeration()

print("3 lineas de salida")

eq = getEquilibrium()
for item in eq:
    print(item)

eq = getEquilibrium()
sigma_r, sigma_c = [array for array in eq][-1]
pd = nash.Game(A, B)

print("punto de equilibrio con estrategias mixtas")
print(pd[sigma_r, sigma_c])