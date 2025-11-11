'''
Ejercicio 6
Escribir un programa que almacene las asignaturas de un curso (por ejemplo
Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la
nota que ha sacado en cada asignatura y elimine de la lista las asignaturas
aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el
usuario tiene que repetir.'''

asignaturas = ['Fisica','Química','Historia','Lengua']
suspensas = []

for i in asignaturas:
    n = int(input(f"Dame la nota que has sacado en {i}\n"))
    if(n<5):
        suspensas.append(i)
print("Debes recuperar:")
for i in suspensas:
    print(i)