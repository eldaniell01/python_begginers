"""
En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex, depositan un número par de huevos. Imagina que tienes una lista de números enteros en la que cada número representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los huevos que pertenecen a los dinosaurios carnívoros (es decir, la suma de todos los números pares en la lista).
"""

def huevos_dinosaurios(list_huevos)->int:
    total_huevos = 0
    
    for huevo in list_huevos:
        if huevo % 2 == 0:
            total_huevos+=huevo
    
    return total_huevos

egg_list = [3, 4, 7, 5, 8]
print(huevos_dinosaurios(egg_list))
