# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import shutil
import sys

def duplicate_file(filename):
    if os.path.isfile(filename):
        newfile = filename + '.copy'
        shutil.copy(filename, newfile)
        if os.path.exists(newfile):
            print("Файл ", newfile, " был успешно создан")
        else:
            print("Возникли проблемы копирования")
    else:
        print("Это не файл!")


directory = os.getcwd()

for i in range(1,10):
    try:
        os.mkdir(os.path.join(directory,"dir_" + str(i)))
    except FileExistsError  as dir:
        print(dir.filename,' - Такая директория уже существует')

tmp = input("Каталоги созданы. Нажмите ввод для удаления.")

for i in range(1,10):
    try:
        shutil.rmtree(os.path.join(directory,"dir_" + str(i)))
    except FileNotFoundError as dir:
        print(dir.filename,' - Такая директория не существует.')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

dirs = [item for item in os.listdir(directory) if os.path.isdir(item)]
print(dirs)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

duplicate_file(sys.argv[0])