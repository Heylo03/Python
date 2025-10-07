'''
Escribir un programa que pregunte por consola por los productos de una cesta de la
compra, separados por comas, y muestre por pantalla cada uno de los productos en
una línea distinta.
'''
cesta = input("Ingresa su cesta de la compra: \n")
lista_productos = cesta.split(',')
for producto in lista_productos:
    print(producto.strip())