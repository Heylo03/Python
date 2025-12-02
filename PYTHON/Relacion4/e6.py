'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla
un triángulo rectángulo como el de más abajo, de altura el número introducido.
'''

n = int(input("DAME UN NUMERO ENTERO: \n"))

for i in range(n+1,0,-1):
    print("*"*i)
