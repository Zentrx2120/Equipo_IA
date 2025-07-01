import numpy as np

# funcion de activación escalón
def escalon(z):
    if z >= 0:
        return 1
    else:
        return 0
    
def relu(z):
    # maximizar el valor de z con 0
    return max(0, z)

# Definicion de hiperparámetros
#lr toma valores entre 0 y 1
lr = 0.2

# Los pesos "w", se recomienda inicializarlos entre 0 y 1
# de forma aleatoria
w0 = -2
x0 = 1

W = np.array([0.1, 0.7])
##
epochs = 130

# Problema a resolver
Yd = np.array([0, 0, 1, 2, 1, 1])  # Salida deseada
yobt = np.zeros_like(Yd)  # Salida obtenida

# Entradas del problema
X = np.array([[-1, 0.1], 
              [-0.9, 0.7], 
              [0.8, 0.1], 
              [0.9, 0.9], 
              [0.7, 0.2], 
              [0.85, 0.95]])  # Entradas

## Implementar el early stop

for i in range(epochs):
    print(f"Epoca {i}: ")
    print("Yobt = ", yobt)
    print("W = ", W)
    print("w0 = ", w0)

    for j in range(len(Yd)):
        z = w0*x0+np.sum(W*X[j,:])  # Producto punto + sesgo
        # yobt[j] = escalon(z)  # Aplicar función de activación
        yobt[j] = relu(z)
        # Actualizar pesos
        if yobt[j]!=Yd[j]:
            w0 = w0-lr*(yobt[j]-Yd[j])
            W = W-lr*(yobt[j]-Yd[j])*X[j,:]
            print(f"nuevos pesos w0 = {w0}, W = {W}")

## Etapa de operación
X1 = float(input("Ingrese el valor de x1: "))
X2 = float(input("Ingrese el valor de x2: "))

X_op = [X1, X2]
z = w0 * x0 + np.sum(W * X_op)  # Producto punto + sesgo
yobt_op = relu(z)
print("El valor de salida es: ", yobt_op)
