"""

 Ejercicio 4: Categorizar edades
    # Pide al usuario que introduzca una edad y la clasifique en:
    # - Bebé (0-2 años)
    # - Niño (3-12 años)
    # - Adolescente (13-17 años)
    # - Adulto (18-64 años)
    # - Adulto mayor (65 años o más)

"""

edad = int(input("ingrese la edad "))

if 0<= edad <=2:
    print("bebe")
elif 3<= edad <=12:
    print("niño")
elif 13<= edad <=17:
    print("adolescente")
elif 18<= edad <= 64:
    print("adulto")
elif edad >= 65:
    print("adulto mayor")
else:
    print("edad no valida")