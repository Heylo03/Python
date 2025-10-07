'''
Escribir un programa que pregunte por consola el precio de un producto en euros
con dos decimales y muestre por pantalla el número de euros y el número de
céntimos del precio introducido.
'''
precio = input("Dame el precio con dos decimales: \n")
precio = precio.split(".")
print(f"EUROS: {precio[0]}€ \nCENTIMOS: {precio[1]}")