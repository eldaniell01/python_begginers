"""

bucle while
permite ejecutar un bloque de codigo repetidamente mientras se cumpla una condicion

"""

print("blucle while")

contador = 0

while contador <=5:
    print(contador)
    contador +=1
    
    
#break para romper el bucle

print("bucle while con break")
contador = 0

while True:
    print(contador)
    contador+=1
    if contador==5:
        break
    
print("bucle con continue")

contador = 0
while contador <10:
    contador +=1
    if contador % 2 ==0:
        continue
    print(contador)


print("bucle while con else")

contador = 0
while contador < 5:
    print(contador)
    contador+=1
else:
    print("bucle ha terminado")
    

"""

pedirle al usuario un numero que tiene que ser positivo hasta que lo ingrese

"""
numero =-1

while numero<0:
    try:
        numero = int(input("escribe un numero positivo: "))
        if numero < 0:
            print("el numero debe ser positivo")
    except:
        print("debe de ser un numero")
    
        
print(f"el numero que ha introducido es {numero}")