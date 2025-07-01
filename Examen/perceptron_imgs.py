import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image

def escalon(z):
    if z >= 0:
        return 1
    return 0

# Carga y preprocesamiento de imágenes 
def cargar_imagenes(ruta_carpeta):
    imagenes_binarizadas = []
    etiquetas = []
    imagenes_originales = []  # Para visualización
    clases = {'arbol': 0, 'carro': 1, 'cubo': 2, 'resortera': 3}
    
    for nombre_archivo in sorted(os.listdir(ruta_carpeta)):
        if nombre_archivo.endswith('.png'):
            # Extraer clase del nombre del archivo
            nombre_clase = nombre_archivo.split('_')[0]
            etiqueta = clases[nombre_clase]
            
            # Cargar imagen y convertir a escala de grises
            ruta_completa = os.path.join(ruta_carpeta, nombre_archivo)
            img = Image.open(ruta_completa).convert('L')
            img_array = np.array(img)
            imagenes_originales.append(img_array)  # Guardar original para plot
            
            # Binarizar la imagen para el entrenamiento: píxeles > 128 son 1, el resto 0
            img_binarizada = (img_array > 128).astype(int)
            
            imagenes_binarizadas.append(img_binarizada.flatten())
            etiquetas.append(etiqueta)
            
    return np.array(imagenes_binarizadas), np.array(etiquetas), imagenes_originales

#  Hiperparámetros y Carga de Datos 
lr = 0.1
epoch = 100
ruta_imgs = os.path.join(os.path.dirname(__file__), 'imgs', 'dataset')

X, Yd, imagenes_originales_entrenamiento = cargar_imagenes(ruta_imgs)

#  Visualización de Muestras de Entrenamiento 
print("Mostrando muestras de entrenamiento...")
fig, axs = plt.subplots(4, 5, figsize=(12, 10))
fig.suptitle("Muestras de Entrenamiento (Originales en escala de grises)")
clases_mapa_inverso_viz = {0: 'arbol', 1: 'carro', 2: 'cubo', 3: 'resortera'}

# Organizar imágenes por clase para una fácil visualización
imagenes_por_clase = [[] for _ in range(len(clases_mapa_inverso_viz))]
for img, label in zip(imagenes_originales_entrenamiento, Yd):
    imagenes_por_clase[label].append(img)

for i in range(4):  # 4 clases
    for j in range(5):  # 5 muestras por clase
        if j < len(imagenes_por_clase[i]):
            axs[i, j].imshow(imagenes_por_clase[i][j], cmap='gray', vmin=0, vmax=255)
            if j == 0:
                axs[i, j].set_ylabel(clases_mapa_inverso_viz[i], rotation=90, size='large')
            axs[i, j].set_xticks([])
            axs[i, j].set_yticks([])
        else:
            axs[i, j].axis('off') # Ocultar si no hay imagen

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()


#  Entrenamiento del Perceptrón (Uno-vs-Rest) 
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

#  Etapa de Operación 
def predecir(imagen_plana, W, w0):
    activaciones = []
    for i in range(num_clases):
        z = w0[i] + np.dot(W[i], imagen_plana)
        activaciones.append(z) # Usamos la activación directa, no la salida de escalón
    return np.argmax(activaciones)

clases_mapa_inverso = {0: 'arbol', 1: 'carro', 2: 'cubo', 3: 'resortera'}
ruta_operacion = os.path.join(os.path.dirname(__file__), 'imgs', 'operacion')

# Corregir posible error tipográfico en la extensión del archivo
nombre_cubo_incorrecto = os.path.join(ruta_operacion, 'cubo.npg')
nombre_cubo_correcto = os.path.join(ruta_operacion, 'cubo.png')
if os.path.exists(nombre_cubo_incorrecto):
    os.rename(nombre_cubo_incorrecto, nombre_cubo_correcto)

imagenes_operacion = [f for f in os.listdir(ruta_operacion) if f.endswith('.png')]

if not imagenes_operacion:
    print(f"No se encontraron imágenes de prueba en la carpeta: {ruta_operacion}")
else:
    # Seleccionar una imagen aleatoria de la carpeta de operación
    nombre_imagen_aleatoria = np.random.choice(imagenes_operacion)
    ruta_completa_img = os.path.join(ruta_operacion, nombre_imagen_aleatoria)
    
    # Cargar y preprocesar la imagen de prueba
    img_prueba_original = Image.open(ruta_completa_img).convert('L')
    img_array_original = np.array(img_prueba_original)
    
    # Binarizar la imagen para la predicción
    img_array_binarizada = (img_array_original > 128).astype(int)
    
    # Realizar la predicción
    prediccion_idx = predecir(img_array_binarizada.flatten(), W, w0)
    clase_predicha_nombre = clases_mapa_inverso[prediccion_idx]
    
    # Mostrar la imagen y el resultado de la predicción
    plt.figure(figsize=(6, 6))
    plt.imshow(img_array_original, cmap='gray', vmin=0, vmax=255)
    plt.title(f"Imagen de Prueba: {nombre_imagen_aleatoria}\nClase Predicha: {clase_predicha_nombre}")
    plt.axis('off')
    plt.show()