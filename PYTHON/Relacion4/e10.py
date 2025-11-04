'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla si
es un número primo o no.
'''

entero = int(input("DAME UN NUMERO ENTERO: \n"))
primo = True

for i in range (2,entero):
    if(entero % i == 0 or entero<=1):
        primo = False

if primo:
    print("ES PRIMO")
else : 
    print("NO ES PRIMO")
