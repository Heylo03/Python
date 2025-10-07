'''
Escribir un programa que pida al usuario que introduzca una frase en la consola y
una vocal, y después muestre por pantalla la misma frase pero con la vocal
introducida en mayúscula.
'''
frase = input("Dame una frase: \n")
vocal = input("Dame una vocal: \n")

print(frase.replace(vocal.lower(), vocal.upper()))


