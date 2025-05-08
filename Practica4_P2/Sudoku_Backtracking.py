"""Código para resolver el Sudoku utilizando un enfoque de backtracking
Este código utiliza un enfoque de backtracking para encontrar una solución al Sudoku."""

# -*- coding: utf-8 -*-

import random
import copy

#----------------------------------------------------------------------------------------------------
def imprimir_tablero(tablero, n):
    for i in range(n):
        for j in range(n):
            print(tablero[i][j], end=" ")
        print()
    print()
#---------------------------------------------------------------------------------------------------
def llenar_aleatorio(tablero, cantidad, n):
    celdas_vacias = [(i, j) for i in range(n) for j in range(n) if tablero[i][j] == 0]
    random.shuffle(celdas_vacias)
    for _ in range(cantidad):
        if not celdas_vacias:
            break
        fila, colum = celdas_vacias.pop()
        num = random.randint(1, n)
        if es_valido(tablero, fila, colum, num, n):
            tablero[fila][colum] = num
#---------------------------------------------------------------------------------------------------
def es_valido(tablero, fila, colum, num, n):
    # Verifica si el número ya está en la fila
    for j in range(n):
        if tablero[fila][j] == num:
            return False

    # Verifica si el número ya está en la columna
    for i in range(n):
        if tablero[i][colum] == num:
            return False

    # Verifica si el número ya está en el subcuadro 3x3
    sub_fila = (fila // 3) * 3  # Calcula la fila inicial del subcuadro
    sub_colum = (colum // 3) * 3  # Calcula la columna inicial del subcuadro
    for i in range(3):
        for j in range(3):
            if tablero[sub_fila + i][sub_colum + j] == num:
                return False

    return True
#---------------------------------------------------------------------------------------------------
def resolver(tablero, n):
    # Busca una celda vacía (valor 0)
    for fila in range(n):
        for colum in range(n):
            if tablero[fila][colum] == 0:
                # Intenta colocar un número del 1 al 9
                for num in range(1, n + 1):
                    if es_valido(tablero, fila, colum, num, n):
                        print(f"Intentando colocar {num} en posición ({fila}, {colum})")
                        tablero[fila][colum] = num
                        
                        # Llama recursivamente para resolver el resto del tablero
                        if resolver(tablero, n):
                            return True
                        
                        # Si no funciona, retrocede
                        print(f"Regresando: quitando {num} de posición ({fila}, {colum})")
                        tablero[fila][colum] = 0
                
                # Si ningún número es válido, no hay solución
                return False
    
    # Si no hay celdas vacías, el tablero está resuelto
    return True
#---------------------------------------------------------------------------------------------------
def sudoku():
    n = 9  # Fijar el tamaño del Sudoku a 9x9
    print("Sudoku de tamaño", n, "x", n)
    
    # Tablero predefinido
    tablero = [
        [9, 6, 1, 0, 4, 3, 0, 0, 2],
        [7, 0, 3, 0, 8, 5, 9, 4, 1],
        [0, 4, 5, 9, 2, 1, 0, 0, 0],
        [3, 9, 0, 1, 0, 0, 0, 0, 5],
        [1, 0, 4, 0, 9, 2, 3, 6, 8],
        [5, 0, 2, 4, 3, 0, 0, 0, 7],
        [4, 3, 7, 8, 0, 9, 2, 0, 0],
        [0, 1, 0, 2, 5, 0, 8, 3, 0],
        [0, 5, 8, 3, 0, 4, 7, 0, 0]
    ]

    tablero_inicial = copy.deepcopy(tablero)

    if validar_tablero_inicial(tablero, n):
        if resolver(tablero, n):
            print("Solución encontrada:")
            imprimir_tablero(tablero, n)
        else:
            print("No se encontró solución.")
    else:
        print("El tablero inicial no es válido.")

#---------------------------------------------------------------------------------------------------
def validar_tablero_inicial(tablero, n):
    for fila in range(n):
        for colum in range(n):
            num = tablero[fila][colum]
            if num != 0:
                tablero[fila][colum] = 0
                if not es_valido(tablero, fila, colum, num, n):
                    print(f"Conflicto detectado con el número {num} en la posición ({fila}, {colum})")
                    return False
                tablero[fila][colum] = num
    return True

# Llamada a la función
sudoku()