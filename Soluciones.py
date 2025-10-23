import math

# Pedir coeficientes asegurando que a ≠ 0
while True:
    a = float(input("Introduce el valor de a: "))
    if a != 0:
        break
    print("El valor de 'a' no puede ser 0. Inténtalo de nuevo.")

b = float(input("Introduce el valor de b: "))
c = float(input("Introduce el valor de c: "))

# Calcular el discriminante
discriminante = b**2 - 4*a*c

# Verificar si hay soluciones reales
if discriminante < 0:
    print("La ecuación no tiene soluciones reales.")
else:
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)

    # Mostrar resultados
    if discriminante == 0:
        print(f"La ecuación tiene una única solución real: x = {x1}")
    else:
        print(f"Las soluciones reales son: x1 = {x1} y x2 = {x2}")
