''''
Ejercicio 6
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y
el nombre. El grupo A está formado por las mujeres con un nombre anterior a la M y
los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un
programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo
que le corresponde.
'''

nombre = input("DAME TU NOMBRE: \n")
genero = input("DAME TU GENERO: \n")

if ((genero[0] == "F" and nombre[0] < "M") or (genero[0] == "M" and nombre[0] > "N")):
    print("GRUPO A")
else:
    print("GRUPO B")