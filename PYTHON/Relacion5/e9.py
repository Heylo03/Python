''''
Ejercicio 9
Escribir un programa que pida al usuario una palabra y muestre por pantalla el
número de veces que contiene cada vocal.
'''
palabra = input("DAME UNA PALABRA \n")
countA=countE=countI=countO=countU = 0

for i in palabra:
    if i == 'a':
        countA+=1
    if i == 'e':
        countE+=1
    if i == 'i':
        countI+=1
    if i == 'o':
        countO+=1
    if i == 'u':
        countU+=1

print(f"A:{countA}\nE:{countE} \nI:{countI} \nO:{countO} \nU:{countU}")