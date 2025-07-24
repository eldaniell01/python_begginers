"""

range()
permite crear una secuencia de numeros. puede ser util para for

"""

print("range")

nums = range(5)
print(nums)

for num in range(10):
    print(num)
    
for num in range(5,10):
    print(num)
    
for num in range(0, 10, 2):
    print(num)
    
for num in range(-5, 0):
    print(num)

for num in range(10, 0, -1):
    print(num)

nums = range(10)
lista = list(nums)
print(lista)

for _ in range(5):
    print("algo")