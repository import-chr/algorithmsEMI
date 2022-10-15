#========================================#
#                                        #
#Cabo Cdtes. Christian Jair Loeza Ramirez#
#                                        #
#========================================#

import numpy as np

def bubbleSort(vector):
    limite_elementos = vector.size - 1
    pasos = 0
    #print(limite_elementos)
    for i in range(0, limite_elementos):
        #pasos += 1
        print(f'pasadas #{i + 1}')
        for j in range(0, limite_elementos):
            print(f'comparacion: {vector[j]} > {vector[j + 1]}')
            if vector[j] > vector[j + 1]:
                print(f'intercambia: {vector[j]} x {vector[j + 1]}')
                aux = vector[j]
                vector[j] = vector[j + 1]
                vector[j + 1] = aux
    return vector


inputs = np.array([70, 90, 0, 80, 60, 85, 44])
print("No ordenado")
print(inputs)
print("Ordenado")
print(bubbleSort(inputs))