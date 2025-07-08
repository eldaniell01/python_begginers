"""

    metodos de listas
    los metodos mas importantes para trabajar con listas

"""

lista = [1,2,3,4,5]

lista.append(6)#añade un elemento al final
print(lista)

lista.insert(1, 4)#inserta un elemento en la posicion que le indiquemos
print(lista)

lista.extend([8,9])#agrega elementos al final de la lista
print(lista)

lista.remove(4)#elimina la primera aparcion de un elemento
print(lista)

ultimo = lista.pop()#elimina el ultimo de la lista

print(ultimo)
print(lista)

lista.pop(1)
print(lista)

del lista[-1]#elimina 
print(lista)

lista.clear()#elimina todos los elementos
print(lista)

#eliminar rango de elementos
listaf = ['a', 'b', 'c', 'd', 'e', 'f']

del listaf[1:]

print(listaf)

#ordenamiento de listas

numeros = [2,1,5,6,4,3]
numeros.sort()
print(numeros)


print("ordena una lista conservando la original")
numeros = [2,1,5,6,4,3]
num = sorted(numeros)
print(num)
print(numeros)

print("ordenar una lista de cadena de texto mayusculas y minusculas")
fruts = ['manzada', 'pera', 'limon', 'Limon', 'Pera']

fru = sorted(fruts)
print(fru)

fruts = ['manzada', 'pera', 'limon', 'Limon', 'Pera']
fruts.sort(key=str.lower)
print(fruts)

#contando numero de elementos en la lista
lista2 = [1,2,2,3,3,3,4]
print(lista2.count(4))

#comprobar si hay un elemento la lista
print(4 in lista2)