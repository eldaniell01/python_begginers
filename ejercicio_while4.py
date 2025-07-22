"""

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".

"""
contraseña = ""

while len(contraseña)<8:
    contraseña = input("ingrese la contraseña ")
    if len(contraseña)<8:
        print("la contraseña no cumple con los requisitos")
        
print("contraseña valida")