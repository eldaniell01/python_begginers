#[]coincide con cualquier caracter dentro de los corchetes
import re
username = "rub.is_69+"
pattern = r"^[\w._%+-]+$"
found = re.search(pattern, username)
print(found.group())

#buscar todas las vocales de una palabra

text = "hola mundo"
pattern = r"[aeiou]"
found = re.findall(pattern, text)
print(found)

#una regex para encontrar las palabras man, fan y ban, pero ignora el resto

text = "man ran fan ñan ban"
pattern = r"[mfb]an"
found = re.findall(pattern, text)
print(found)

#nos han complicado el asunto, porque ahora hay palabras que encajan pero no empiezan por esas letras. solo queremos las palabras man, fan y ban

text = "omniman fanatico man bandana banban"
pattern = r"[mfb]an"
found = re.findall(pattern, text)
print(found)

#[^] coincide con cualquier caracter que no este dentro de de los corchetes
text = "hola mundo"
pattern = r"[^aeiou]"
found = re.findall(pattern, text)
print(found)