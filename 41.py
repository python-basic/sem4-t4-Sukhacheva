"""
Создание программы по заполнению массивов случайными значениями. Сортировка значений в списке методом вставки, плавной сортировки, с помощью встроенных функций языка.
"""
import random

arr = [round(random.random() * 10) for i in range(5)]

def SortVst(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst
    
print(arr)

arr1 = SortVst(arr.copy())
print("Сортировка вставкоми: ", arr1)

arr3 = sorted(arr)
print("Сортировка встроенной функцией: ", arr3)
