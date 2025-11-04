'''
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
y el número de años, y muestre por pantalla el capital obtenido en la inversión cada
año que dura la inversión.'''


cantidad = float(input("Introduce la cantidad a invertir: "))
interes_anual = float(input("Introduce el interés anual (en %): "))
year = int(input("Introduce el número de años: "))

for i in range(1, year + 1):
    capital = cantidad * (1 + interes_anual / 100) ** i
    print(f"Año {i}: capital = {capital:.2f}")
