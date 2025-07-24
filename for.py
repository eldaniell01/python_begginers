"""

bucle for
permite ejecutar un bloque de codigo repetidamente mientras itera un iterable o una lista

"""
frutas = ["manzana", "pera", "mandarina"]
for fruta in frutas:
    print(fruta)

cadena = "eldaniell01"
for ca in cadena:
    print(ca)
    
#enumerate()
frutas = ["manzana", "pera", "mandarina"]
for index, fruta in enumerate(frutas):
    print(f"indice: {index} fruta: {fruta}")
    
#bucles anidados
letras= ["a", "b", "c"]
numeros = [1,2,3]

for letra in letras:
    for numero in numeros:
        print(f"{letra} {numero}")

#break y continue
animales = ["conejo", "gato", "raton", "loro", "pez", "canario"]
for animal in animales:
    print(animal)
    if animal == "loro":
        break
    
animales = ["conejo", "gato", "raton", "loro", "pez", "canario"]
for animal in animales:
    
    if animal == "loro":
        continue
    print(animal)
    
#list comprehension
animales = ["conejo", "gato", "raton", "loro", "pez", "canario"]
animal_m = [animal.upper() for animal in animales]
print(animal_m)

pares = [num for num in [1,2,3,4,5,6] if num % 2 ==0]
print(pares)