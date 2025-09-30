'''
Escribir un programa que pida al usuario dos números enteros
y muestre por pantalla la <n> entre <m> da un cociente <c>
y un resto <r> donde <n> y <m> son los números introducidos
por el usuario, y <c> y <r> son el cociente y el resto de la
división entera respectivamente.
'''
n1 = int(input("Dame un numero entero: \n"))
n2 = int(input("Dame otro numero entero: \n"))

c = float(n1/n2)
r = float(n1%n2)
print(f"Dividendo: {n1}\n Divisor: {n2}\n Cociente: {c}\n Resto: {r}")

