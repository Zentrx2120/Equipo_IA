import random
import numpy as np
import matplotlib.pyplot as plt

mov = np.array(["Izquierda","Derecha"]) 

mapa = np.array([[1,1,1,0,1,1,1,0,1,1],
                 [0,0,1,1,1,0,1,1,1,0],
                 [1,0,1,0,0,0,1,0,1,0],
                 [1,1,1,0,0,1,1,0,1,0],
                 [1,0,0,0,1,0,0,1,1,0],
                 [1,1,1,1,1,1,0,1,0,0],
                 [1,0,0,0,0,1,0,1,0,0],
                 [1,1,1,1,0,1,1,1,1,1]])

plt.imshow(mapa, cmap='gray')
plt.scatter(9,7, color='red')
plt.show()

i, j = 9, 7

#while True:
#print("Is there an object blocking (Y/N)?")
#entrada = input()

for k in range(10):

    print("Is there an object blocking (Y/N)?")
    entrada = input()

    if (entrada == "y" or entrada == "Y"):
        movimientos = random.randint(0,1)
        #print(f"Moving to: {mov[movimientos]}")

        if (movimientos == 0):
            i = i-1
            print("Moving izquierda")
            if(i<0):
                print("No se puede mover a la izquierda")
                i = i + 1
                #print("Moving derecha")

            if(mapa[j][i] == 0):
                print("No se puede mover a la izquierda")
                i = i + 1
                #print("Moving derecha")

        else:
            i = i + 1
            print("Moving derecha")
            if(i>9):
                print("No se puede mover a la derecha")
                i = i - 1
                #print("Moving izquierda")

            if(mapa[j][i] == 0):
                print("No se puede mover a la derecha")
                i = i - 1
                #print("Moving izquierda")
    else:
        j = j - 1
        print("Moving forward")
        if(j<0):
            print("No se puede mover hacia adelante")
            j = j + 1
            #print("Moving back")
        if(mapa[j][i] == 0):
            print("No se puede mover hacia adelante")
            j = j + 1
            #print("Moving back")
    
    plt.imshow(mapa, cmap='gray')
    plt.scatter(i,j, color='red')
    plt.show()