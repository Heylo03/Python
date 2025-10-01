'''
Ejercicio 12
Una panadería vende barras de pan a 3.49€ cada una. El pan
que no es el día tiene un descuento del 60%. Escribir un
programa que comience leyendo el número de barras vendidas
que no son del día. Después el programa debe mostrar el
precio habitual de una barra de pan, el descuento que se le
hace por no ser fresca y el coste final total.
'''
descuento = 0.60
precioBarra = 3.49
precioDescuento = round(precioBarra-precioBarra*descuento,2)

panes = int(input("Dame el número de barras de pan: \n"))

costeTotal = round(panes*precioDescuento,2)
totalDescontado = round(precioBarra*panes-costeTotal,2)
totalSinDescuento = round(precioBarra*panes,2)

print(f"Número de barras: {panes}\nCoste barra NO fresca:  {precioDescuento}€\nCoste barra fresca: {precioBarra}€\nCoste total: {costeTotal}€\nDescuento obtenido: {totalDescontado}€")
