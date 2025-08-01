"""

diccionarios
los diccionarios son colecciones de pares clave-valor
sirven para almacenar datos relacionados

"""

persona = {
    "nombre": "eldaniell01",
    "edad": 27,
    "direccion": "centro dos",
    "numero": 2415
}

#para acceder a los valores
print(persona["edad"])

#para cambiar valores
persona["nombre"]="daniel"
print(persona["nombre"])

#eliminar una propiedad
del persona["edad"]

print(persona)
estudiante = persona.pop("nombre")
print(f"estudiante: {estudiante}")
print(persona)

#actualizar o sobreescribir un diccionario con otro

a = {"name": "eldaniell01", "age": 27}
b = {"name": "angela", "estudiante": True}

a.update(b)
print(a)

#comprobar si existe una propiedad

print("name" in persona)
print("nombre" in persona)

#obtener todas las claves
print(persona.keys())

#obtener todos los valores
print(persona.values())

#obtener claves y valores
print(persona.items())

for key, value in persona.items():
    print(f"{key}: {value}")