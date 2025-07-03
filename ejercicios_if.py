

"""
    ejercicio 1: determinar el mayor de dos numeros 
    pedir al usuario que introduzca dos numeros y muestra un mensaje
    indicando cual es mayor o si son iguales

"""

num1 = int(input("ingrese el primer numero "))

num2 = int(input("ingrese el segundo numero "))

if num1 == num2:
    print("los numeros son iguales")
elif num1 > num2:
    print(f'el mayor es: {num1}')
else:
    print(f'el mayor es: {num2}')

