"""

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.

"""

lista = [5, 2, 8, 1, 9, 4, 2]

lista.sort()
print(lista)

print(lista.count(2))
print(7 in lista)