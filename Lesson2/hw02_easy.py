from py_linq import Enumerable
# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ["яблоко", "банан", "киви", "арбуз"]

maxLen = 0
for fruit in fruits:
    if maxLen < len(fruit):
        maxLen = len(fruit)

symbol = '.'
for fruit in fruits:
    print(str(fruits.index(fruit) + 1).strip(),symbol, f'{fruit : >{maxLen}}')



# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
# 1 способ
names1 = ['Ivan', 'Alex', 'Olga', 'Georg']
names2 = ['Serg', 'Alex', 'Roman', 'Georg']

for name in names1:
    if name in names2:
        names1.remove(name)

print(names1)

#2 способ
names1 = Enumerable(['Ivan', 'Alex', 'Olga', 'Georg'])
names2 = Enumerable(['Serg', 'Alex', 'Roman', 'Georg'])
names1 = names1.except_(names2).select(lambda item : item).to_list()

print(names1)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

listOfIntegers = [1,4,2,8,3,6,9,4]
resultList = []

# 1 способ
for item in listOfIntegers:
    if item % 2 == 0:
        resultList.append(item / 4)
    else:
        resultList.append(item * 2)

print(resultList)

# 2 способ - возвращает только уникальные значения, поэтому если элементы будут одинаковые получаться в результате вычислений, этот способ не годится
enumOfIntegers = Enumerable([4,7,8,13,16,9])
resultList = enumOfIntegers.where(lambda item : item % 2 == 0).select(lambda item : item / 4).union(enumOfIntegers.where(lambda item : item % 2 != 0).select(lambda item : item * 2)).to_list()
print(resultList)