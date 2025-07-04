"""

listas
secuencias mutables de elementos
pueden contener elementos de diferentes tipos


"""

print("crear listas")

lista1 = [1, 2, 3, 4, 5]
lista2 = ["manzana", "pera", "platanos"]
lista3 = [1, "hola", 3.14, True]

lista_vacia = []
lista_de_lista = [[1,2], [3,4]]
matrix = [[1,2],[2,3],[4,5]]

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_lista)
print(matrix)

print("acceso a la lista por indice")

print(lista2[0])
print(lista2[1])
print(lista2[-1])
print(lista2[-2])

print( lista_de_lista[1][0])

print("slicing de listas")

print(lista1[1:4])
print(lista1[:3])
print(lista1[3:])
print(lista1[:])

print("revertir lista")

print(lista1[1:5:2])
print(lista1[::-1])

print("modificar lista")
lista1[0]=20

print(lista1)

print("añadir elementos a la lista")

#forma larga
lista1 = lista1+[2, 5, 6]
print(lista1)

#forma corta y eficiente
lista1 +=[8, 87, 9]
print(lista1)

print("recuperar longitud")
print("longitud es ", len(lista1))