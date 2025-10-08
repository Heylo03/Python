'''
Escribir un programa que pregunte el nombre el un producto, su precio y un número
de unidades y muestre por pantalla una cadena con el nombre del producto seguido
de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con
tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
'''
nombre = input("Dame el nombre del producto: \n")
precio = float(input("Dame el precio del producto: \n"))
unidades = int(input("Dame el número de unidades: \n"))

coste_total = precio * unidades

# :08.2f  -> 8 dígitos enteros + 2 decimales
# :06.2f  -> 6 dígitos enteros + 2 decimales
# :03d    -> 3 dígitos para enteros
salida = f"{nombre} {precio:09.2f} {unidades:03d} {coste_total:010.2f}"

print(salida)
