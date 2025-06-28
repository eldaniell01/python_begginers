"""
    sentencias condicionales (if, elif, else)
        permiten ejecutar bloques de c`odigo solo si se cumple ciertas condiciones
"""
import os 
os.system("clear")

edad = 18
if edad >= 18:
    print("eres mayor de edad")

print("sentencia condicional con else")

edad = 15
if edad>=18:
    print("eres mayor de edad")
else: 
    print("eres menor de edad")

print("sentencia condicional con elif")
nota = 7
if nota >= 9:
    print("sobresaliente")
elif nota == 7:
    print("notable")
elif nota == 5:
    print("aprobado")
else:
    print("no calificado")
    
print("condiciones multiples")

edad = 8
carnet= False

if edad >=18 and carnet:
    print("conducir")
else:
    print("policia")
    
    
if edad >=18 or carnet:
    print("conducir")
else:
    print("pagar policia")
    
fin_de_semana = False
if fin_de_semana:
    print("si")
elif not fin_de_semana:
    print("no")