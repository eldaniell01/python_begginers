"""

# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().

"""

num = int(input("ingrese un numero "))

for n in range(1,11):
    print(f" {num} *  {n} = {num*n}")