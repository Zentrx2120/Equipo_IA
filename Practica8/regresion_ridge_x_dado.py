import numpy as np
import matplotlib.pyplot as plt

# Definir X (Vector de caracteristicas) y Y (Vector de etiquetas)
X1 = np.array([1.0, 2.0, 3.0,  4.0,  5.0,  6.0,  7.0,    8.0,  9])
Yd = np.array([2.0, 5.0, 8.0, 10.0, 14.5, 19.0, 20.0, 24.5, 29.0])

# Defininir hiperparámetros/parámetros (Idealmente: Betas iniciadas aleatoriamente entre 0 y 1)
b0 = 0.1
b1 = 0.2
lr = 0.06 # Learning rate
m = len(X1) # Numero de muestras
L = 0.000002 # Factor de atenuación Lambda

# Definir epocas y Epsilon para Early Stopping
epochs_limite = 10000  # Límite máximo de épocas (anteriormente 'epochs')
E = 0.000001 # Tolerancia para early stopping (epsilon)

# Definir variables
ecm_actual = 0.0      # Error cuadratico medio (ECM actual)
ecm_anterior = float('inf') # ECM de la iteración anterior, inicializado para la condición del bucle
ECM_record = []
iter_epoch_actual = 0 # Contador de épocas actual

# Bucle de entrenamiento con early stopping
while iter_epoch_actual <= epochs_limite and abs(ecm_actual - ecm_anterior) > E:
    Yobt = b0 + b1 * X1

    # Descenso de gradiente
    b0 = b0 - (lr / m) * np.sum(Yobt - Yd)
    b1 = b1 - (lr / m) * np.dot((Yobt - Yd), X1) + 2 * L * b1

    # Actualizar ecm_anterior con el valor de ecm_actual 
    ecm_anterior = ecm_actual
    
    # Calcular nuevo ecm_actual
    ecm_actual = (1/(2 * m)) * np.sum((Yd - Yobt) ** 2) + L * b1 ** 2
    ECM_record += [ecm_actual] 

    iter_epoch_actual += 1
    

print("El valor de b0 es: ", b0)
print("El valor de b1 es: ", b1)
print("Ultimo valor de ECM: ", ecm_actual)

# Graficar ECM
plt.plot(ECM_record)
plt.show()

# Fase de operación: Predecir Y para un nuevo X dado por el usuario
print("\n--- Fase de Operación ---")
input_X_str = input("Ingrese los valores para el nuevo vector X (separados por espacios): ")
# Convertir la cadena de entrada a una lista de números flotantes
try:
    X_usuario_list = []
    for val_str in input_X_str.split():
        X_usuario_list = X_usuario_list + [float(val_str)] 
    X_usuario = np.array(X_usuario_list)

    if len(X_usuario) > 0:
        # Calcular Ypredict usando los b0 y b1 finales
        Y_predict = b0 + b1 * X_usuario
        print("\nValores de X ingresados por el usuario:", X_usuario)
        print("Valores de Y predichos (Y_predict):", Y_predict)
        
        # Comparar con Yd (si tienen la misma longitud para una comparación directa)
        # Nota: Yd corresponde a los datos de entrenamiento originales.
        # La comparación directa tiene más sentido si X_usuario es similar/igual a X1.
        print("\nValores originales de Y deseados (Yd) del conjunto de entrenamiento:", Yd)
        
        # Opcional: Si X_usuario tiene la misma forma que X1, se puede graficar
        if X_usuario.shape == X1.shape:
            plt.figure(figsize=(10, 6))
            plt.scatter(X1, Yd, color='blue', label='Valores Deseados (Yd)')
            plt.plot(X1, b0 + b1 * X1, color='red', label='Línea de Regresión (Entrenamiento)')
            plt.scatter(X_usuario, Y_predict, color='green', marker='x', s=100, label='Predicciones para X Usuario')
            plt.xlabel("X")
            plt.ylabel("Y")
            plt.title("Comparación de Predicciones del Modelo")
            plt.legend()
            plt.grid(True)
            plt.show()
        else:
            print("Nota: No se graficarán las nuevas predicciones ya que la forma de X_usuario no coincide con X1.")

    else:
        print("No se ingresaron valores para X.")

except ValueError:
    print("Error: Asegúrese de ingresar solo números separados por espacios.")