# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "иНевозможно создать/удалить/перейт"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
import hw05_easy as lib

operations = {
    1: lambda foldername: lib.change_folder(foldername),
    2: lambda foldername: lib.list_filesAndFolders(os.getcwd()),
    3: lambda foldername: lib.delete_folder(foldername),
    4: lambda foldername: lib.create_folder(foldername)
}

def process_user_choice(choice, foldername):
    return operations[choice](foldername)


def start():
    default_foldername = os.path.join(os.getcwd(),"temp")
    foldername = input("Введите имя папки или просто ввод для значения папки по умолчания=temp:")
    if foldername == "":
        foldername = default_foldername
    while True:
        try:
            choice = int(input('Выберите пункт:\n'
                               '1. Перейти в папку\n'
                               '2. Просмотреть содержимое текущей папки\n'
                               '3. Удалить папку\n'
                               '4. Создать папку\n'
                               '5. Выход\n'
                               '---------------------\n'
                               'Ваш выбор:'))
        except ValueError:
            print('Неверный ввод!')
            continue
        if choice == 5:
            break
        process_user_choice(choice, foldername)


start()
