'''
Ejercicio 10
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
Los ingredientes para cada tipo de pizza aparecen a continuación.
● Ingredientes vegetarianos: Pimiento y tofu.
● Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y
en función de su respuesta le muestre un menú con los ingredientes disponibles
para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el
tomate que están en todas las pizzas. Al final se debe mostrar por pantalla si la
pizza elegida es vegetariana o no y todos los ingredientes que lleva.
'''


print("Tipos de pizza disponibles:")
print("1. Vegetariana")
print("2. No vegetariana")

# Preguntar al usuario qué tipo de pizza desea
tipo = input("¿Qué tipo de pizza deseas (vegetariana/no vegetariana)? ").strip().lower()

# Ingredientes comunes
ingredientes_base = ["mozzarella", "tomate"]

# Ingredientes según tipo
if tipo == "vegetariana":
    ingredientes_opciones = ["pimiento", "tofu"]
    print("\nHas elegido una pizza vegetariana.")
elif tipo == "no vegetariana":
    ingredientes_opciones = ["peperoni", "jamón", "salmón"]
    print("\nHas elegido una pizza no vegetariana.")
else:
    print("Opción no válida. Por favor, escribe 'vegetariana' o 'no vegetariana'.")
    exit()

# Mostrar ingredientes y pedir elección
print("Ingredientes disponibles:")
for i, ing in enumerate(ingredientes_opciones, 1):
    print(f"{i}. {ing}")

opcion = int(input("Elige un ingrediente (1, 2 o 3 según corresponda): "))

# Validar
if 1 <= opcion <= len(ingredientes_opciones):
    ingrediente_elegido = ingredientes_opciones[opcion - 1]
else:
    print("Opción no válida.")
    exit()

# Mostrar resultado final
ingredientes_finales = ingredientes_base + [ingrediente_elegido]
print("\n--- Resumen de tu pedido ---")
print(f"Tipo de pizza: {'Vegetariana' if tipo == 'vegetariana' else 'No vegetariana'}")
print("Ingredientes:", ", ".join(ingredientes_finales))
print("-----------------------------")
