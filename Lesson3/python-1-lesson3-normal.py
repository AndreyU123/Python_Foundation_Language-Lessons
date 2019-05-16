# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.
import os

def writeSalaryFile(pathToFile, namesToSalaries):
    with open(pathToFile, 'w', encoding='UTF-8') as salaryFile:
        salaryFile.write(f"{'Имя'} - {'Зарплата'}\n")
        salaryFile.write("---------------\n")
        for name in namesToSalaries.keys():
            salaryFile.write(f"{name} - {namesToSalaries[name]}\n")

def readSalaryFile(pathToFile, maxVisibleSalary):
    i = 0
    with open(pathToFile, 'r', encoding='UTF-8') as salaryFile:
        for item in salaryFile:
            if i < 2:
                i += 1
                continue
            nameToSalary = item.rstrip().split("-")
            salary = int(nameToSalary[1].strip())
            if len(list(filter(lambda x: x <= maxVisibleSalary, [salary]))) == 0:
                continue
            salaryMinusNalog = salary - salary / 100 * 13
            print( f"{nameToSalary[0].upper()} - {int(salaryMinusNalog)}")

#####################################################################################

maxVisibleSalary = 500000

names =    ["Саша","Петя", "Вася", "Роман", "Андрей","Николай","Денис"]
salaries = [70000, 100000,  600000, 300000 , 550000,  40000,    80000]
namesToSalaries = dict(zip(names,salaries))

filename = "salary.txt"
pathToFile = os.path.join(os.path.abspath(os.curdir),filename)

# if os.path.exists(pathToFile):
#     os.remove(pathToFile)

writeSalaryFile(pathToFile,namesToSalaries)

readSalaryFile(pathToFile, maxVisibleSalary)

