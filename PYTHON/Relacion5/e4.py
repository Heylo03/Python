'''
Escribir un programa que pregunte al usuario los números ganadores de la lotería
primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor
a mayor.
'''

loteria = [534,642,6234,3123,6,234,3245,6756,86763]
loteria.sort()
for i in loteria:
    print(i)