"""

# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.

"""
palabras = ["casa", "arbol", "sol", "elefante", "luna"]

palabra = [p for p in palabras if len(p)>5]

print(palabra)