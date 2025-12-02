'''
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y
muestre por pantalla el número de veces que aparece la letra en la frase.
'''

frase = "Escribir un programa en el que se pregunte al usuario por una frase y una letra, y \
muestre por pantalla el número de veces que aparece la letra en la frase."

letra = input("DAME UNA LETRA: \n").lower()
frase.lower()
c = 0
for i in range(0,len(frase)):
    if frase[i] == letra:
        c += 1
print(c)


