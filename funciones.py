"""

funciones
bloques de codigo reutilizables y parametrizables para hacer tareas especificas

"""


def saludar():
    print("hola")
    
saludar()

def saludar_a(nombre):
    print(f"hola {nombre}")
    
saludar_a("daniel")

def suma(a, b):
    suma = a + b
    return suma

result = suma(2,3)

print(suma(2, 3))

def restar(a, b):
    """restar dos numeros y devuelve el resultado

    Args:
        a (int): valor numerico 1
        b (int): valor numerico 2
    """
    return a, b

print(restar.__doc__)

def multiplicar(a, b = 2):
    return a*b

print(multiplicar(2))

def describir_persona(nombre, edad, sexo):
    print(f"soy {nombre}, tengo {edad}, años y me identifico como {sexo}")

print(describir_persona(sexo="hombre", nombre="daniel", edad=27))

#argumentos de longitud de variable (*args)

def sumar_numeros(*args):
    suma = 0
    for numero in args:
        suma+=numero
    return suma

print(sumar_numeros(1,2,3,5,6,6))

#argumentos de clave-valor variable (**kwargs)
def mostrar_informacion(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
        
print(mostrar_informacion(nombre="daniel", edad=27, sexo="hombre"))