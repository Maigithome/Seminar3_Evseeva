# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# для отрицательных индексов {\displaystyle F_{n}=F_{n+2}-F_{n+1}}:

def fibonacci(k):
    if k in [1, 2]:                       
        return 1
    else:
        return fibonacci(k-1) + fibonacci(k-2)

def nega_fibonacci(k):
    if k == 1:                       
        return 1
    elif k == 2:                       
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, k):
            num1, num2 = num2, num1 - num2
        return num2

list = [0]
k = int(input("Введите число: "))
for j in range(1, k + 1):
    list.append(fibonacci(j))
    list.insert(0, nega_fibonacci(j))
print(list)