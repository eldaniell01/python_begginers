"""
    ejercicio 3: año bisiesto 
    pedir al usuario que introduzca un año y determine si es bisiesto
    un año bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400

"""
age = int(input("ingrese el año "))

resultado = str(age) + " es año bisiesto" if(age %4 ==0 and age % 100 !=0) or age % 400 ==0 else "no es bisiesto"

print(resultado)