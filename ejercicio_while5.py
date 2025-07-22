"""

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.

"""

num = int(input("ingrese un numero "))

contador = 1

while contador <=10:
    print(f"{contador} * {num} = {contador*num}")
    contador+=1
    