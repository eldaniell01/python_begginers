"""

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).

"""

palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]

letra = input("ingrese una letra ")

contador = 0
cantidad = [contador+1 for x in palabras if x[0]==letra]
print(len(cantidad))
    