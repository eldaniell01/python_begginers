"""
    ejercicio 2: caculadora
    pedir al usuario dos numeros y una operacion (+,-,*,/)
    realiza la operacion y muestra el resultado (maneja la division entre zero)

"""

num1=int(input("ingrese el primer numero "))
num2=int(input("ingrese el segundo numero "))
operacion = input("ingrese la operacion +, -, *, /")
resultado = 0
if num2 ==0 and operacion =='/':
    print("no se pudede operar")
elif operacion =='/':
    resultado = num1/num2
elif operacion == '+':
    resultado = num1+num2
elif operacion == '-':
    resultado = num1-num2
elif operacion =='*':
    resultado = num1*num2
else:
    print("operacion no valida")    

print(f'el resultado es {resultado}')