# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]
n=int(input("Введите длину массива: "))
list_new = [int(list[i]) for i in range(n)]
list_diff=[round((float(list[i]) - int(list_new[i])), 3) for i in range(n)]
print(list)
print(list_new)
print(list_diff)
print(max(list_diff)-min(list_diff))