import sympy as sp
import numpy as np

x = sp.symbols('x')

# -----------------------------
# Entrada
# -----------------------------
func_str = input("Ingrese f(x): ")
a = float(sp.sympify(input("Ingrese a: ")))
b = float(sp.sympify(input("Ingrese b: ")))
k_max = int(input("Ingrese k (columnas): "))

f_sym = sp.sympify(func_str)
f = sp.lambdify(x, f_sym, 'numpy')

# -----------------------------
# Cálculo Romberg
# -----------------------------
R = np.zeros((k_max, k_max))

for i in range(k_max):
    n = 2**i
    h = (b - a) / n
    xs = np.linspace(a, b, n + 1)
    ys = f(xs)

    R[i, 0] = h * (0.5*ys[0] + np.sum(ys[1:-1]) + 0.5*ys[-1])

    for j in range(1, i + 1):
        R[i, j] = R[i, j-1] + (R[i, j-1] - R[i-1, j-1]) / (4**j - 1)

# -----------------------------
# Impresión (estructura validada)
# -----------------------------
print("\nTABLA DE ROMBERG\n")

print(f"{'n':>6}", end="")
for k in range(1, k_max + 1):
    print(f"{'k=' + str(k):>15}", end="")
print()

for fila in range(k_max):
    n = 2**fila
    print(f"{n:>6}", end="")

    for k in range(1, k_max + 1):
        i = fila + k - 1
        j = k - 1

        if i < k_max:
            print(f"{R[i, j]:>15.6f}", end="")
        else:
            print(f"{'':>15}", end="")
    print()

# -----------------------------
# Cálculo del error verdadero
# -----------------------------
I_romberg = R[k_max - 1, k_max - 1]

try:
    I_exacta = sp.integrate(f_sym, (x, a, b))

    if I_exacta.has(sp.Integral):
        raise ValueError

    I_exacta = float(I_exacta)
    origen = "simbólico"

except:
    I_exacta = float(input("\nNo se pudo calcular la integral exacta.\nIngrese el valor verdadero: "))
    origen = "usuario"

error = abs((I_exacta - I_romberg)/I_exacta)*100

# -----------------------------
# Resultados finales
# -----------------------------
print("\nRESULTADOS FINALES")
print(f"Mejor aproximación (Romberg): {I_romberg:.6f}")
print(f"Integral verdadera: {I_exacta:.6f}")
print(f"Error verdadero: {error:.6f}")
