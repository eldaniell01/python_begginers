"""

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
# Un número es primo si es divisible por sólo uno de los números enteros entre 1 y él mismo, incluido.


"""

num = int(input("ingresa un numero "))

num1 = 2
if num >0:
    while num1 <=num:    
        primo = True
        divisor = 2
        while divisor * divisor <= num1:
            if num1 % divisor == 0:
                primo = False
                break
            divisor+=1
        if primo:
            print(num1)
        num1+=1

else:
    print("error en el numero")