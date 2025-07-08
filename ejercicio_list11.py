"""

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.

"""

lista =  [1,2,3]

copia1 = lista[:]
print(copia1)

copia2 = lista.copy()
print(copia2)

referencia = lista
referencia[0]=10
print(lista)
print(copia1)
print(copia2)
print(referencia)