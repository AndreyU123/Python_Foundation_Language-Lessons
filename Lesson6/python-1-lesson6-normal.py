# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

import os
import random

class Person:
    def __init__(self, name, health, damage, armor):
        self._name = name
        self._health = health
        self._damage = damage
        self._armor = armor

    def get_name(self):
        return self._name

    def get_health(self):
        return self._health

    def set_health_by_damage(self, damage):
        self._health -= damage
        if self._health < 0:
            self._health = 0

    def get_damage(self):
        return self._damage

    def get_armor(self):
        return self._armor

    def _calculateDamage(self, armor):
        return self._damage // armor

    def attack(self, person2):
        damage = self._calculateDamage(person2.get_armor())
        person2.set_health_by_damage(damage)
        print('{} нанес {} урона {}, у того осталось {} жизней.'.format(self._name, person2.get_name(), damage, person2.get_health()))

    @staticmethod
    def _num(s):
        try:
            return int(s)
        except ValueError:
            return float(s)

    @staticmethod
    def _isNum(value):
        try:
            int(value)
            return True
        except:
            try:
                float(value)
                return True
            except:
                return False

    @staticmethod
    def loadPlayerFromFile(pathToFile):
        dictionary={}
        with open(pathToFile, 'r', encoding='UTF-8') as player1File:
            for item in player1File:
                key,value = item.rstrip().split(":")
                if Person._isNum(value):
                    dictionary[key] = Person._num(value)
                else:
                    dictionary[key] = value
        playerFromFile = Person(dictionary["name"],dictionary["health"],dictionary["damage"],dictionary["armor"])
        return playerFromFile


class Game:
    def __init__(self,player1,player2):
        self._player1 = player1
        self._player2 = player2

    def play_game(self):
        val = random.randint(0,1)
        if val == 0:
            last_attacker = self._player1
        else:
            last_attacker = self._player2
        while (self._player1.get_health() > 0 and self._player2.get_health() > 0):
            if last_attacker == self._player1:
                self._player2.attack(self._player1)
                last_attacker = self._player2
            else:
                self._player1.attack(self._player2)
                last_attacker = self._player1
        


#########################################################################

namePlayer1 = input("Введите имя игрока 1:")
namePlayer1 = namePlayer1.strip()
namePlayer2 = input("Введите имя игрока 2:")
namePlayer2 = namePlayer2.strip()


player1 = Person(namePlayer1, 100, 70,  1.2)
player2 = Person(namePlayer2, 100,  40,  1.2)

print("Begin:", player1.get_name())
print("Next:", player2.get_name())

game1 = Game(player1, player2)
game1.play_game()

print("Final:", player1.get_name(),player1.get_health())
print("Final:", player2.get_name(),player2.get_health())

#############################################################

filename1 = "Piter.txt"
pathToFile1 = os.path.join(os.path.abspath(os.curdir),filename1)
filename2 = "Vasja.txt"
pathToFile2 = os.path.join(os.path.abspath(os.curdir),filename2)

player1FromFile = Person.loadPlayerFromFile(pathToFile1)
player2FromFile = Person.loadPlayerFromFile(pathToFile2)

print("Begin:", player1FromFile.get_name())
print("Next:", player2FromFile.get_name())

game2 = Game(player1FromFile, player2FromFile)
game2.play_game()

print("Final:", player1FromFile.get_name(),player1FromFile.get_health())
print("Final:", player2FromFile.get_name(),player2FromFile.get_health())

# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# мне кажется, не нужны эти классы - все описано в Person, смысл есть создать SuperPerson, который имеет доп. функциональность - скажем летать, но это усложнит задачу.