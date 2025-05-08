# -*- coding: utf-8 -*-
# Codigo para resolver el problema de las N reinas utilizando un enfoque iterativo
# Este código utiliza un enfoque de backtracking iterativo para encontrar todas las soluciones
# al problema de las N reinas.

# Para imprimir el tablero de forma más legible
import numpy as np

#---------------------------------------------------------------------------------------------------
def imprimir_tablero(tablero, n):
        tablerito = np.zeros((n, n))

        for i in range(n):
            for j in range(n):
                if tablero[i] == j:
                    tablerito[i][j] = 1

        print(f"{tablerito}\n")
#---------------------------------------------------------------------------------------------------
# Definición de la función n_reinas que toma un entero n como argumento
def n_reinas(n):

    # Inicializa el tablero con -1, lo que indica que no hay reinas colocadas
    # Inicializa la fila en 0 y un arreglo colum para llevar el seguimiento de las columnas
    tablero = [-1] * n
    fila = 0
    colum = [0] * n

    # if fila == n:
    #     imprimir_tablero(tablero, n)
    #     return True

    # mientras haya filas por procesar
    while fila >= 0:

        # Si hemos procesado todas las filas, significa que hemos encontrado una solución
        if fila == n:
            imprimir_tablero(tablero, n)
            fila -= 1
            colum[fila] += 1
            break

        # Backtracking
        # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        # Si hemos procesado todas las columnas en la fila actual, retrocedemos
        if colum[fila] >= n:
            tablero[fila] = -1
            colum[fila] = 0
            fila -= 1
            print(f"Backtracking: Retirando la reina de la fila {fila}, columna {col}")

            if fila >= 0:
                colum[fila] += 1
            continue
        # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

        # Colocamos una reina en la fila actual y columna actual
        # y verificamos si es una posición válida
        col = colum[fila]
        validez = True 
        i = 0

        # Verificamos si la posición es válida comparando con las reinas ya colocadas
        while i < fila:
            if tablero[i] == col or tablero[i] - i == col - fila or tablero[i] + i == col + fila:
                validez = False
                break
            i += 1

        if validez:
            tablero[fila] = col
            imprimir_tablero(tablero, n)
            fila += 1
            # if resolvedor(tablero, fila + 1):
            #     return True
        else:
            # print(f"Backtracking: Retirando la reina de la fila {fila}, columna {col}")
            colum[fila] += 1
#-----------------------------------------------------------------------------------------
n_reinas(8)