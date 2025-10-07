'''
Ejercicio 5
Escribir un programa que pregunte al usuario por el número de
horas trabajadas y el coste por hora. Después debe mostrar
por pantalla la paga que le corresponde.
'''
hora = input("Dame las horas trabajadas: \n")
coste = input("Dame el precio por hora: \n")
total = float(hora)*float(coste)
print(f"Total: {total}€")