"""
Создание программы по распределению списка с случайными значениями на два списка по определенному критерию (четность/нечетность, положительные/отрицательные числа).
Создание программы по разделению одного словаря на произвольное количество словарей по определенному критерию, задаваемому в виде лямбда функции.
"""
import random

list = [random.randint(-100, 100) for i in range(10)]
print(list)

pol = []
otr = []
for i in list:
    (lambda i: pol.append(i) if i>0 else otr.append(i))(i)

print(pol)
print(otr)

chet = []
nechet = []
for i in list:
    (lambda i: chet.append(i) if i % 2 else nechet.append(i))(i)

print(chet)
print(nechet)
