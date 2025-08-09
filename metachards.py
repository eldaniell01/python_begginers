"""

meta caracteres
los metacaracteres son simbolos especiales con significados
especificos enlas expresiones regulares

"""

import re
# el punto
#coincidir con cualquier caracter excepto una nueva linea

text = "hola muno, H0la de nuevo, H2la otra vez"

pattern = "h.la"
found = re.findall(pattern, text, re.IGNORECASE)
print(found)

text = "casa caasa cosa cisa cesa causa"
pattern = "c.sa"
martches = re.findall(pattern, text)
print(martches)


text = "hola muno, H0la de nuevo, H2la otra vez"

pattern = r"h.la"
found = re.findall(pattern, text, re.IGNORECASE)
print(found)

#usar barra invertida para anular el significado de un simbolo o signo
text = "mi casa es blanca. mi carro es negro"

pattern = r"\."

found = re.findall(pattern, text)
print(found)


#\d coincide con cualquier digito (0-9)

text = "el numero de telefono 123456789"
found = re.findall(r'\d{9}', text)
print(found)

#detectar si hay un numero de españa en el texto gracias al prefijo +34

text = "mi numero de telefono es +34 487483843"
pattern = r"\+34 \d{9}"
found = re.search(pattern, text)
print(f"{found.group()}")

#\w coincde con cualquier caracter alfanumerico (a-z)(A-Z (0-9) -)
text = "elrubius69"
pattern = r"\w"
found = re.findall(pattern,text)
print(found)

#\s: coincide con cualquier espacio en blanco(espacio, tabulacion, salto de linea)

text = "hola mundo \n como estas\t"

pattern = r"\s"
found = re.findall(pattern, text)
print(found)

#^: coincide con el principio de una cadena

text = "454_name"
patter = r"^\w"
found = re.search(patter, text)
if found: print("es valido")
else: print("no es valido")


phone = "+322 848484848"
pattern = r"^\+\d{1,3} "
found = re.search(pattern, phone)
print(found)

#$ coincide con el final de una cadena

text =  "hola mundsddo"
pattern = r"mundo$"

found = re.search(pattern, text)
print(found)

#validacion de un correo electronico

text = "amontepeque@gmail.com"
pattern = r"@gmail.com$"
found = re.search(pattern, text)

if found: print("valido")
else: print("no valido")

#tenemos una lista de archivos, necesitamos saber los nombres de los ficheros con extension .txt
files = "file1.txt file2.pdf midu-of.webp secret.txt"
pattern = r"\S+\.txt"
found = re.findall(pattern, files)
if found: print("listado ", found)
else: print("no hay")

#b coincide con el principio o final de una palabra
text = "casa casada casado casa casa"
pattern = r"\bcasa\b"

found = re.findall(pattern, text)
print(found)

# | coincidir con una opcion u otra
frutas = "platano, manzana, aguacate, palta, pera"
pattern = r"palta|aguacate"
found = re.findall(pattern, frutas)
print(found)