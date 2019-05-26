#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.   

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""

import random

class NumberGenerator:
    def __init__(self, start, end):
        self._start = start
        self._end = end
        self._used_values=[]

    def Reset(self):
        self._used_values = []

    def __iter__(self):
        return self

    def __next__(self):
        generated_number = random.randint(self._start, self._end)
        while generated_number in self._used_values:
            if len(self._used_values) == self._end:
                raise StopIteration
            generated_number = random.randint(self._start, self._end)
        self._used_values.append(generated_number)
        return generated_number

class Keg: #бочонок
    def __init__(self, keg_start=1, keg_end=90):
        self._numberGenerator = NumberGenerator(keg_start, keg_end)
        self._curr_keg =0

    def __iter__(self):
        return self

    def __next__(self):
        self._curr_keg = self._numberGenerator.__next__()
        return self._curr_keg

    def printKeg(self):
        print("Выпал номер бочонка: ",self._curr_keg)

class Card:
    def __init__(self, max_value=90, line_count=3, cell_count=9, filled_cell_count=5):
        self._valueGenerator = NumberGenerator(1, max_value)
        self._cellNumberGenerator = NumberGenerator(0, cell_count - 1)
        self._matrix = [[0 for _ in range(0,cell_count)] for _ in range(0,line_count)]
        self._createCardMatrix(line_count, filled_cell_count)
        print(self._matrix)

    def _createCardMatrix(self, line_count, filled_cell_count):
        for line_number in range(0,line_count):
            self._cellNumberGenerator.Reset()
            value_array = []
            cell_number_array = []
            for _ in range(0, filled_cell_count):
                value_array.append(self._valueGenerator.__next__())
                cell_number_array.append(self._cellNumberGenerator.__next__())
            value_array.sort()
            cell_number_array.sort()
            for idx, cell_number in enumerate(cell_number_array):
                self._matrix[line_number][cell_number] = value_array[idx]

    def crossOut(self, keg, iscrossout = True):
        found = False
        matrix_copy = self._matrix.copy()
        for line_number, line in enumerate(matrix_copy):
            for cell_number, value in enumerate(line):
                if(value == keg):
                    if iscrossout:
                        self._matrix[line_number][cell_number] ="-"
                    found = True
                    return found
        return found

    def continuePlay(self, keg):
        found = self.crossOut(keg, False)
        return not found

    def printMatrix(self):
        print("Получилась карта: ", self._matrix)

    def isAllValuesCrossedOut(self):
        is_all_values_crossedOut = True
        for line_number, line in enumerate(self._matrix):
            for cell_number, value in enumerate(line):
                if str(self._matrix[line_number][cell_number]) != "-" and self._matrix[line_number][cell_number] != 0:
                    is_all_values_crossedOut = False
                    break
        return is_all_values_crossedOut



class Player:
    def __init__(self):
        self._card = Card()

    def get_card(self):
        return self._card;

    def move(self, next_keg): #ход
        print("карта игрока до хода:")
        self.get_card().printMatrix()
        keg =next_keg.__next__()
        next_keg.printKeg()
        answer = input("Зачеркнуть цифру? (y/n)")
        while answer != "y" and answer != "n":
            answer = input("введите корректное значение: y/n")
        if answer == "y":
            result = self._card.crossOut(keg)
        else:
            result = self._card.continuePlay(keg)
        print("карта игрока после хода:")
        self.get_card().printMatrix()
        if result == False:
            print("Player проиграл")
        return result

class Computer:
    def __init__(self):
        self._card = Card()

    def get_card(self):
        return self._card;

    def move(self, next_keg):  # ход  всегда зачеркивает
        print("карта компьютера до хода:")
        self.get_card().printMatrix()
        keg = next_keg.__next__()
        next_keg.printKeg()
        result = self._card.crossOut(keg)
        print("карта компьютера после хода:")
        self.get_card().printMatrix()
        if result == False:
            print("Computer проиграл")
        return result

class Game:
    def __init__(self, player, computer):
        self._player = player
        self._computer = computer
        self._is_game_over = False
        self._keg = Keg()

    def _all_values_cards_crossedOut(self):
        isPlayerWin = self._player.get_card().isAllValuesCrossedOut()
        isCompWin = self._computer.get_card().isAllValuesCrossedOut()
        return isPlayerWin or isCompWin



    def start(self):
        while not self._is_game_over and not self._all_values_cards_crossedOut():
            self._is_game_over = not self._player.move(self._keg)
            if self._is_game_over == True:
                break
            self._is_game_over = not self._computer.move(self._keg)
    ##############################################################################

player = Player()
computer = Computer()
game = Game(player,computer)
game.start()




