'''   
Ejercicio 11
Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y
muestre por pantalla su producto escalar.
'''
<<<<<<< HEAD
=======
import numpy as np

>>>>>>> 802d6343afff33174f7ed16b54159eec6ee8ef99
vector1 = [1,2,3]
vector2 = [-1,0,2]
resultado=0
for i in range(len(vector1)):
    resultado += vector1[i] * vector2[i]
print(resultado)