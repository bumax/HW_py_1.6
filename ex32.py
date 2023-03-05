# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не
# больше заданного максимума)

import random

n = int(input("Введите кол-во элементов: "))
min = int(input("Введите нижнюю границу: "))
max = int(input("Введите верхнюю границу: "))

list_n = [random.randint(-100, 100) for x in range(n)]
print(list_n)

# Без рекурсии:
# for i in range(len(list_n)):
#     if min  < list_n[i] < max :
#         print(f"Элемент с индексом {i} и значением {list_n[i]} находится в границе диапазона")

# С рекурсией:


def is_in_range(lst, min, max, i=0):
    if len(lst) > 0:
        if min < lst.pop(0) < max:
            print(f"Элемент с индексом {i} находится в границе диапазона!")
        i += 1
        is_in_range(lst, min, max, i)


is_in_range(list_n, min, max)