lam = float(input("Ingrese la tasa de llegada (λ): "))
tasaserv = float(input("Ingrese la tasa de servicio (tasaserv): "))
varia = float(input("Ingrese la varia de la distribución del servicio: "))

rho = lam / tasaserv
Lq = ((lam**2 * varia) + rho**2) / (2 * (1-rho))
L = Lq + rho
Wq = Lq/lam
W = Wq + 1/tasaserv

print("Medidas de Eficacia del Sistema:")
print(f"\tCantidad promedio en el sistema: L = {L}")
print(f"\tCantidad promedio esperando en la cola: Lq = {Lq}")
print(f"\tTiempo promedio en el sistema: W = {W}")
print(f"\tTiempo promedio esperando en la cola: W = {Wq}")
print(f"\tFactor de utilización del unico servidor: rho = {rho}")