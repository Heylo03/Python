'''
Escribir un programa que almacene la cadena de caracteres contraseña en una
variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña
correcta.'''

password = "administrador"
r = ""
while(r != password):
    print("LONGITUD CONTRASEÑA : ","*"*len(password))
    r = input("DAME LA CONTRASEÑA: \n")
print("CONTRASEÑA CORRECTA, ACCESO CONCEDIDO")