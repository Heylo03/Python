'''
Ejercicio 1
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10
veces.
'''
nombre = input("Dame una palabra:\n")

for i in range (0,10):
    print(i+1," : ",nombre)
