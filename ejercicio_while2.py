"""
# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.

"""
print("\nEjercicio 2:")

numeros = 1
suma = 0
while numeros <=20:
    if numeros %2 ==0:
        suma+=numeros
        
    numeros+=1
print(suma)