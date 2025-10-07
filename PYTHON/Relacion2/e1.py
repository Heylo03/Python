'''
Escribir un programa que pregunte el nombre del usuario en la consola y un número
entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces
como el número introducido.

for _ in range(numero):
    print(nombre)
'''
nombre = input("Introduce tu nombre: \n")
numero = int(input("Introduce un número entero: \n"))

print(f"{nombre}\n"*numero)