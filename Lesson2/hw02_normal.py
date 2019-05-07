import math
import datetime
import locale
import random
# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

sourceList = [2, -5, 8, 9, -25, 25, 4]
targetList = []

for item in sourceList:
    if item >= 0 and (int(math.sqrt(item)) - math.sqrt(item) == 0):
        targetList.append(int(math.sqrt(item)))

print(targetList)


# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

mydate = datetime.date(2013,11,2)

dayNames = {1 : 'первое',2 : 'второе', 3 : 'третье', 4 : 'четвертое', 5 : 'пятое', 6 : 'шестое', 7 : 'седьмое', 8 : 'восьмое', 9 : 'девятое',10 : 'десятое'} # и т.д. до 31

loc = locale.getlocale()
locale.setlocale(locale.LC_ALL, 'ru_RU')
print(dayNames[mydate.day], mydate.strftime("%B %Y года").lower().replace('рь','ря').replace('ль','ля').replace('т','та').replace('й','я').replace('нь','ня'))
locale.setlocale(locale.LC_ALL, loc)

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

resultList = []
min = -100
max = 100;
n = 10
myrange = range(n)
for _ in myrange:
    resultList.append(random.randint(min,max))

print(resultList)



# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

sourceLst = [1, 2, 4, 5, 6, 2, 5, 2]
targetLst1 = []
targetLst2 = []

for item in sourceLst:
    if item not in targetLst1:
        targetLst1.append(item)

print(targetLst1)

tmp = [] # list(set(a))
for item in sourceLst:
    if item not in targetLst2:
        targetLst2.append(item)
    else:
        tmp.append(item)

for item in tmp:
    if item in targetLst2:
        targetLst2.remove(item)
		# if a.count(elem)==1
		# targetLst2.append(elem)

print(targetLst2)