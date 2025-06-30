# -*- coding: utf-8 -*-
# percer.py
# Ejemplo de perceptrón simple

import numpy as np
import itertools

# funcion de activación escalón
def escalon(z):
    if z >= 0:
        return 1
    else:
        return 0
    
def sigmoide(z):
    zz = 1 / (1 + np.exp(-z))
    return zz

def tanh(z):
    zz = np.tanh(z)
    return zz

def bipolar(z):
    if z>0:
        return 1
    elif z==0:
        return 0
    elif z<0:
        return -1

def relu(z):
    return max(0, z)

def escalon_modificada(z):
    if z>=0.5:
        return 1
    else:
        return 0

# Selección de compuerta
while True:
    tipo = input("Selecciona la compuerta (AND/OR): ").strip().upper()
    if tipo in ["AND", "OR"]:
        break
    print("Opción no válida. Elige AND o OR.")

# Selección de número de características
while True:
    n = int(input("Número de características (2 a 5): "))
    if 2 <= n <= 5:
        break
    print("Debe ser un número entre 2 y 5.")

# Selección de función de activación
while True:
    func = input("Selecciona la función de activación (escalon/sigmoide/tanh/bipolar/relu/escalon_modificada): ").strip().lower()
    if func in ["escalon", "sigmoide", "tanh", "bipolar", "relu", "escalon_modificada"]:
        break
    print("Opción no válida. Elige una función de activación válida.")

# Entradas
# itertools.product genera el producto cartesiano de los valores 0 y 1
# repeat=n indica que queremos combinaciones de n bits
X = np.array(list(itertools.product([0, 1], repeat=n)))

# Salidas
# X == 1 verifica si todos los elementos de la fila son 1
# .asºtype(int) convierte el resultado booleano a entero
if tipo == "AND":
    Yd = np.all(X == 1, axis=1).astype(int)
else:
    Yd = np.any(X == 1, axis=1).astype(int)

yobt = np.zeros_like(Yd) #Salida obtenida

# Inicialización de pesos y sesgo
np.random.seed()  # Para aleatoriedad real
W = np.array(np.random.uniform(0, 1, n))  # Pesos aleatorios entre 0 y 1
w0 = -2 #np.random.uniform(-1, 1)
x0 = 1
lr = 0.2
epochs = 8

# Entrenamiento
for i in range(epochs):
    print(f"\nÉpoca {i+1}:")
    print(f"Pesos iniciales: W = {W}, w0 = {w0}")

    for j in range(len(Yd)):
        z = w0 * x0 + np.sum(W * X[j, :])
        if func == "escalon":
            yobt[j] = escalon(z)
        elif func == "sigmoide":
            yobt[j] = sigmoide(z)
        elif func == "tanh":
            yobt[j] = tanh(z)
        elif func == "bipolar":
            yobt[j] = bipolar(z)
        elif func == "relu":
            yobt[j] = relu(z)
        elif func == "escalon_modificada":
            yobt[j] = escalon_modificada(z)
        if yobt[j] != Yd[j]:
            w0 = w0 - lr * (yobt[j] - Yd[j])
            W = W - lr * (yobt[j] - Yd[j]) * X[j, :]
            print(f"    Nuevos pesos: W = {W}, w0 = {w0}")

# Imprimir tabla de verdad
print(f"\nTabla de verdad para compuerta {tipo} con {n} características:")
print("Entradas\t\tSalida esperada\tSalida obtenida")
for i in range(len(X)):
    print(f"{X[i]}\t{Yd[i]}\t\t{yobt[i]}")