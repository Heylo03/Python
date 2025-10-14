'''
Ejercicio 3
Escribir un programa que pida al usuario dos números y muestre por pantalla su
división. Si el divisor es cero el programa debe mostrar un error.
'''
dividendo = int(input("DAME EL DIVIDENDO: \n"))
divisor = int(input("DAME EL DIVISOR (NO PUEDE SER CERO): "))

if(divisor<=0):
    print("ERROR,DIVIDIENDO ENTRE 0")
else:
    print("RESULTADO: ",dividendo/divisor)
