'''
Ejercicio 9
Escribir un programa que pregunte al usuario una cantidad a
invertir, el interés anual y el número de años, y muestre por
pantalla el capital obtenido en la inversión.
resultado = c*(1+i)**t
'''
c = int(input("Capital inicial: "))
i = float(input("Interes: "))
t = int(input("Número de años:"))

resultado = c*(1+i)**t
print(resultado)