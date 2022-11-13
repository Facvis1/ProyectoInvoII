import numpy as np

def main():
    print('Maximin - Minimax')
    while (True):
        print('Ingresar Nro de estrategias a usar:')
        cantEstrategias = int(input())
        estrategJugador1 = Pagos(cantEstrategias)
        print('\n')
        print('Matriz de estrategias:')
        matrizEstra = np.array(estrategJugador1)
        print(matrizEstra)
        minimo = maximin(matrizEstra)
        maximo = minimax(matrizEstra)
        max = maximominimo(minimo)
        min = minimomaximo(maximo)
        print('Resultado: ', end='')
        equilibrio(max, min)
        continuar = input("Quieres usar de nuevo la aplicacion? si/no: ")
        if(continuar.lower() == 'n'):
            break

def Pagos(cant):
    vector1 = []
    for i in range(cant):
        vector2 = []
        for j in range(cant):
            print(
                f'ingrese el pago de la celda [{i+1},{j+1}]:', end='')
            pago = int(input())
            vector2.append(pago)
        vector1.append(vector2)
    return vector1

def maximin(arrayij):
    max = arrayij[0][0]
    list = []
    for i in range(len(arrayij)):
        for j in range(len(arrayij[i])):
            if (max > arrayij[i][j]):
                max = arrayij[i][j]
        list.append(max)
        max = 0
    return list

def minimax(arrayij):
    min = arrayij[0][0]
    list = []
    for i in range(len(arrayij)):
        for j in range(len(arrayij[i])):
            if (min < arrayij[j][i]):
                min = arrayij[j][i]
        list.append(min)
        min = 0
    return list

def maximominimo(a):
    max = a[0]
    for i in range(len(a)):
        if (max < a[i]):
            max = a[i]
    return max

def minimomaximo(a):
    min = a[0]
    for i in range(len(a)):
        if (min > a[i]):
            min = a[i]
    return min

def equilibrio(a, b):
    if (a == b):
        print('Punto silla',end='')
        print(f' => {a}')
    else:
        print('Inestable')

main()