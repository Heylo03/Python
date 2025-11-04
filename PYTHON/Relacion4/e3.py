'''
Escribir un programa que pida al usuario un número entero positivo y muestre por
pantalla todos los números impares desde 1 hasta ese número separados por
comas.
'''
entero = int(input("DAME UN NUMERO ENTERO POSITIVO:\n"))
impares = []
for i in range(1,entero):
    if(i % 2 != 0):
        impares.append(i)
print(impares)