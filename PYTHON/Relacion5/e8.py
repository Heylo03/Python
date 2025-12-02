'''
Ejercicio 8
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un
palíndromo.
'''

palabra = input("DAME UNA PALABRA \n").lower()
arbalap = palabra[::-1]
if(arbalap==palabra):
    print("PALINDROMO")
else:
    print("NO PALINDROMO")