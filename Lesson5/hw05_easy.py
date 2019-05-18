# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


import os
import shutil
import sys

def change_folder(newFolder):
    if os.path.exists(newFolder):
        os.chdir(newFolder)
        print("Успешно перешел в папку:" + newFolder )
    else:
        print("Невозможно перейт в папку:" + newFolder)

def copy_file(filename):
    try:
        if os.path.isfile(filename):
            newfile = filename + '.copy'
            shutil.copy(filename, newfile)
            if os.path.exists(newfile):
                print("Файл ", newfile, " был успешно скопирован")
            else:
                print("Возникли проблемы копирования")
        else:
            print("Это не файл!")
    except FileExistsError as file:
        print(file.filename, ' - Такой файл уже существует')


def copy_folder(foldername):
    try:
        if os.path.isdir(foldername):
            newfolder = foldername + '.copy'
            shutil.copytree(foldername, newfolder)
            if os.path.exists(newfolder):
                print("Папка ", newfolder, " была успешно скопирована")
            else:
                print("Возникли проблемы копирования")
        else:
            print("Это не папка!")
    except FileExistsError as dir:
        print(dir.filename, ' - Такая папка уже существует')

def create_folder2(folderPath, folderName):
    try:
        os.mkdir(os.path.join(folderPath, folderName))
        print("Папка создана: ",os.path.join(folderPath, folderName))
    except FileExistsError as dir:
        print(dir.filename, ' - Такая папка уже существует')
		
def create_folder(folderFullPath):
    try:
        os.mkdir(folderFullPath)
        print("Папка создана: ",folderFullPath)
    except FileExistsError as dir:
        print(dir.filename, ' - Такая директория уже существует')

def create_folders(startNum, endNum, folderPath, folderName):
    for i in range(startNum, endNum):
        create_folder2(folderPath, folderName + str(i))

def delete_folder2(folderPath, folderName):
    try:
        if os.path.join(folderPath, folderName) == os.getcwd():
            change_folder(folderPath)
        os.removedirs(os.path.join(folderPath, folderName))
        print("Папка удалена: ",os.path.join(folderPath, folderName))
    except FileNotFoundError as dir:
        print(dir.filename, ' - Такая директория не существует.')
		
def delete_folder(folderFullPath):
    try:
        if folderFullPath == os.getcwd():
            change_folder(os.path.dirname(folderFullPath))
        shutil.rmtree(folderFullPath)
        print("Папка удалена: ",folderFullPath)
    except FileNotFoundError as dir:
        print(dir.filename, ' - Такая директория не существует.')


def delete_folders(startNum, endNum, folderPath, folderName):
    for i in range(startNum, endNum):
        delete_folder2(folderPath, folderName + str(i))

def list_folders(folderPath):
    dirs = [item for item in os.listdir(folderPath) if os.path.isdir(item)]
    print(dirs)

def list_files(folderPath):
    files = [item for item in os.listdir(folderPath) if os.path.isfile(item)]
    print(files)
	
def list_filesAndFolders(folderPath):
    files = [item for item in os.listdir(folderPath)]
    print(files)

def test_lib():
    # Задача-1:
    create_folders(1, 10, os.getcwd(), "dir_")
    tmp = input("Каталоги созданы. Нажмите ввод для удаления.")
    delete_folders(1, 10, os.getcwd(), "dir_")
    # Задача-2:
    list_folders(os.getcwd())
    list_files(os.getcwd())
    # Задача-3:
    copy_file(sys.argv[0])
    create_folder2(os.getcwd(),"tmp")
    copy_folder(os.path.join(os.getcwd(),"tmp"))


if __name__ == '__main__':
    test_lib()




