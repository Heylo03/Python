'''
Ejercicio 7
Escribir un programa que almacene el abecedario en una lista, elimine de la lista las
letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista
resultante.
'''
abc = []
abc3 = []
for a in range(ord('a'),ord('z')+1):
    abc.append(chr(a))
print(abc)
for i in range(0,len(abc)):
    if(i % 3 == 0):
        abc3.append(abc[i])
print(abc3)