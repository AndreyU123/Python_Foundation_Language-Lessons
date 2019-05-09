# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.
import os
def armorFactor(damage, armor):
    return damage / armor

def attack(person1, person2):
    person2["health"] = round( person2["health"] - armorFactor(person1["damage"], person2["armor"]))
    if person2["health"] < 0 :
        person2["health"] = 0
    return person2

def game(player1, player2):
    while (player1["health"] > 0 and player2["health"] > 0):
        player2 = attack(player1, player2)
        print(player2)
        if player2["health"] == 0:
            break
        player1 = attack(player2, player1)
        print(player1)

def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

def isNum(value):
  try:
      int(value)
      return True
  except:
      try:
          float(value)
          return True
      except:
          return False

def loadPlayerFromFile(pathToFile):
    playerFromFile = {}
    with open(pathToFile, 'r', encoding='UTF-8') as player1File:
        for item in player1File:
            lst = item.rstrip().split(":")
            attrib = lst[1]
            if isNum(attrib):
                attrib = num(attrib)
            playerFromFile[lst[0]] = attrib
    return playerFromFile

#########################################################################

namePlayer1 = input("Введите имя игрока 1:")
namePlayer1 = namePlayer1.strip()
namePlayer2 = input("Введите имя игрока 2:")
namePlayer2 = namePlayer2.strip()

player1 = {"name" : namePlayer1, "health" : 100, "damage" : 70, "armor" : 1.2}
player2 = {"name" : namePlayer2, "health" : 100, "damage" : 40, "armor" : 1.2}

print("Begin:", player1)
print("Begin:", player2)

game(player1, player2)

print("Final:", player1)
print("Final:", player2)

# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

filename1 = "Piter.txt"
pathToFile1 = os.path.join(os.path.abspath(os.curdir),filename1)
filename2 = "Vasja.txt"
pathToFile2 = os.path.join(os.path.abspath(os.curdir),filename2)

player1FromFile = loadPlayerFromFile(pathToFile1)
player2FromFile = loadPlayerFromFile(pathToFile2)

print("Begin:", player1FromFile)
print("Begin:", player2FromFile)

game(player1FromFile, player2FromFile)

print("Final:", player1FromFile)
print("Final:", player2FromFile)

