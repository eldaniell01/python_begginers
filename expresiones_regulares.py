import re

#crear un patron, de una cadena de texto que describe lo que se quiere encontrar
pattern = "hola"

text = "hola mundo"

#usar la funcion de busqueda de re
result = re.search(pattern, text)

print(result)


#devuelve la cadena que coincide con el pattern
print(result.group())

#devolver la posicion inicial de la coincidencia
print(result.start())

# devolver la posicion final de la coincidencia
print(result.end())

"""

encuentra la primera ocurrencia de la palabra IA en el siguiente texto
e indica en que posicion empieza y termina la coincidencia

"""

text = "todo el mundo dice que la IA nos va a quitar el trabajo. pero solo hace falta ver como la puede cargar con las regex para ir con cuidado"

pattern = "IA"

result = re.search(pattern, text)
print(result.group())
print(result.start())
print(result.end())


#encontrar todas las coincidencias de un patron
##findall() devuelve una lista con todas las coincidencias

text = "me gusta python, python es lo maximo, aunque python no es tan dificil, ojo con python"

pattern = "py.hon"

result = re.findall(pattern, text)

print(result)

#iter() devuelve un iterador que contiene todos los resultados de la busqueda

matches = re.finditer(pattern, text)

for match in matches:
    print(match.group(), match.start(), match.end())
    

"""

encuentra todas las ocurrencias de la palabra midu en el siguiente texto e indica en que posicion empieza y termina cada coincidencia y cuantas veces se encontro

"""

text = "este es el curso de python de midudev. ¡suscribete a midudev si te gusta este contenido! midu"

pattern = "midu*"

busqueda = re.finditer(pattern, text)
contador = 0
for match in busqueda:
    print(match.group(), match.start(), match.end())
    contador+=1
print(contador)

#modificadores 
#los modificadores son opciones que se puden agregar a un patron para cambiar su comportamiento
#re.IGNORECASE: ignora las mayusculas y minusculas

text = "todo el mundo dice que la iA nos va a quitar el trabajo. pero solo hace falta ver como la puede cargar con las regex para ir con cuidado viva la Ia"

pattern = "ia"

busqueda = re.findall(pattern, text, re.IGNORECASE)
print(busqueda)

#encuentra todas las ocurrencias de la palabra python en el siguiente texto, sin distinguir entre mayusculas y minusculas

text = "este es el curso de Python de midudev. suscribete a python is te gusta este contenido PYTHON"

pattern = "python"

busqueda = re.findall(pattern, text, re.IGNORECASE)

print(busqueda)


#reemplazar el texto
#sub() reemplaza todas las coincidencias de un patron en un texto

texto = "hola mundo, hola de nuevo"

pattern = "hola"
replacement = "adios"

new_text = re.sub(pattern, replacement, texto, re.IGNORECASE)
print(new_text)