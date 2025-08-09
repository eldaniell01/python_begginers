"""

cuantificadores
los cuantificadores se utilizan para especificar cuantas ocurrencias de un caracter o grupo de caracteres se deben encontrar en una cadena.

"""

import re

text = "aaaab"
pattern = "a*"
found = re.findall(pattern, text)
print(found)


#cuantas palabras tienen de 0 a mas a y despues una b?
text = "alejandrab"
pattern = "a*b"
found = re.findall(pattern, text)
print(found)

# + una a mas veces
text = "ddd aaa ccc bb aa casa"
pattern = "a+"
found = re.findall(pattern, text)
print(found)

#? cero o una vez
text = "aaabacb"
pattern = "a?b"
found = re.findall(pattern, text)
print(found)

#has opcional que aparezca un +34 en el siguiente texto

phone = "+34 203209309020"
pattern = r"\+?34 \d{9}"
found = re.search(pattern, phone)
print(found.group())

#{n} exactamente n veces
text = "aaaaaaaa"
pattern = "a{3}"
found = re.findall(pattern, text)
print(found)

#{n, m} de n a m veces
text = "uuu uu uuuu"
pattern = "u{2,3}"
found = re.findall(pattern, text)
print(found)

#encuentra las palabras de 4 a 6 letras en el siguiente texto

words = "ala casa arbol leon cinco murcielago"
pattern = r"\b\w{4,6}\b"
found = re.findall(pattern, words)
print(found)

#encuentra las palabras de mas de 6 letras
words = "ala fantastico casa arbol leon cinco murcielago"
pattern = r"\b\w{6,}\b"
found = re.findall(pattern, words)
print(found)