'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla
un triángulo rectángulo como el de más abajo.'''

n = int(input("DAME UN NUMERO: \n"))
r = " "
for i in range (1,n+1):
    if(i % 2 != 0):
        print(r)
        r = str(i) + r
