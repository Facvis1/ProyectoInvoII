import numpy as np

def estrategiaDominada(matrizEstra):
    while (len(matrizEstra) != 1):
        matrizEstra = Jugador1(matrizEstra)
        matrizEstra = Jugador2(matrizEstra)
    return matrizEstra

def Pagos(cant):
    vec1 = []
    for i in range(cant):
        vec2 = []
        for j in range(cant):
            print(
                f'ingrese el pago al jugador en la celda: [{i+1},{j+1}]:')
            pago = int(input())
            vec2.append(pago)
        vec1.append(vec2)
    return vec1
    
def main():
    print('Estrategia dominante:')
    while (True):
        print('Ingresar Nro de estrategias a usar:')
        cantEstrategias = int(input())
        estrateg = Pagos(cantEstrategias)
        print('\n')
        print('Matriz de estrategias:')
        matrizEstra = np.array(estrateg)
        print(matrizEstra)
        matrizPago = estrategiaDominada(matrizEstra)
        print('Resultado:', end='')
        print(matrizPago)
        pregunta = input("Quieres usar de nuevo la aplicacion? si/no: ")
        if (pregunta.lower() == 'no'):
            break

def Jugador1(mat):
    for i in range(len(mat)):
        e1 = mat[i]
        breaker = False
        try:
            for j in range(i+1, len(mat)):
                band = True
                eo = mat[j]
                for k in range(len(eo)):
                    if (e1[k] < eo[k]):
                        band = False
                        break
                if (band):
                    mat = np.delete(mat, j, 0)
                    breaker = True
                    break
        except Exception as e:
            print(f"error => {e}")
        if (breaker):
            break
    return mat

def Jugador2(mat):
    for i in range(len(mat)):
        e1 = mat[:, i]
        breaker = False
        try:
            for j in range(len(mat)+1):
                band = True
                eo = mat[:, j]
                for k in range(len(eo)):
                    if (e1[k] > eo[k] or j == i):
                        band = False
                        break
                if (band):
                    try:
                        mat = np.delete(mat, j, j-1)
                    except:
                        mat = np.delete(mat, j, j)
                    breaker = True
                    break
        except Exception as e:
            print(f"error => {e}")
        if (breaker):
            break
    return mat

main()