import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image

def escalon(z):
    if z >= 0:
        return 1
    return 0

# --- Carga y preprocesamiento de imágenes ---
def cargar_imagenes(ruta_carpeta):
    imagenes = []
    etiquetas = []
    clases = {'arbol': 0, 'carro': 1, 'cubo': 2, 'resortera': 3}
    
    for nombre_archivo in sorted(os.listdir(ruta_carpeta)):
        if nombre_archivo.endswith('.png'):
            # Extraer clase del nombre del archivo
            nombre_clase = nombre_archivo.split('_')[0]
            etiqueta = clases[nombre_clase]
            
            # Cargar imagen y convertir a escala de grises y binarizar
            ruta_completa = os.path.join(ruta_carpeta, nombre_archivo)
            img = Image.open(ruta_completa).convert('L')
            img_array = np.array(img)
            # Binarizar la imagen: píxeles > 128 son 1, el resto 0
            img_binarizada = (img_array > 128).astype(int)
            
            imagenes.append(img_binarizada.flatten())
            etiquetas.append(etiqueta)
            
    return np.array(imagenes), np.array(etiquetas)

# --- Hiperparámetros y Carga de Datos ---
lr = 0.1
epoch = 100
ruta_imgs = os.path.join(os.path.dirname(__file__), 'imgs')

X, Yd = cargar_imagenes(ruta_imgs)

# --- Entrenamiento del Perceptrón (Uno-vs-Rest) ---
num_clases = 4
num_caracteristicas = X.shape[1]
W = np.random.uniform(-0.5, 0.5, (num_clases, num_caracteristicas))
w0 = np.random.uniform(-0.5, 0.5, num_clases)

print("Iniciando entrenamiento...")
for n_clase in range(num_clases):
    # Crear etiquetas binarias para la clase actual (1 vs Resto)
    Yd_binario = np.where(Yd == n_clase, 1, 0)
    
    for epochs in range(epoch):
        errores = 0
        for i in range(len(X)):
            z = w0[n_clase] + np.dot(W[n_clase], X[i])
            y = escalon(z)
            
            if y != Yd_binario[i]:
                error = Yd_binario[i] - y
                w0[n_clase] += lr * error
                W[n_clase] += lr * error * X[i]
                errores += 1
        
        if errores == 0:
            print(f"Clasificador para la clase {n_clase} entrenado en la época {epochs}.")
            break
    if errores != 0:
        print(f"Clasificador para la clase {n_clase} finalizó entrenamiento tras {epoch} épocas.")

print("Entrenamiento finalizado.")

# --- Prueba del Modelo ---
def predecir(imagen_plana, W, w0):
    activaciones = []
    for i in range(num_clases):
        z = w0[i] + np.dot(W[i], imagen_plana)
        activaciones.append(z) # Usamos la activación directa, no la salida de escalón
    return np.argmax(activaciones)

# Cargar una imagen de cada clase para probar
clases_mapa_inverso = {0: 'arbol', 1: 'carro', 2: 'cubo', 3: 'resortera'}
fig, axs = plt.subplots(1, 4, figsize=(12, 4))
fig.suptitle("Predicciones en nuevas imágenes")

for i, clase_nombre in enumerate(clases_mapa_inverso.values()):
    # Usamos la primera imagen de cada clase como prueba
    ruta_img_prueba = os.path.join(ruta_imgs, f'{clase_nombre}_1.png')
    img_prueba = Image.open(ruta_img_prueba).convert('L')
    img_array_prueba = (np.array(img_prueba) > 128).astype(int)
    
    # Predecir
    prediccion = predecir(img_array_prueba.flatten(), W, w0)
    
    # Mostrar imagen y resultado
    axs[i].imshow(img_array_prueba, cmap='gray')
    titulo = f"Real: {clase_nombre}\nPred: {clases_mapa_inverso[prediccion]}"
    axs[i].set_title(titulo)
    axs[i].axis('off')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()