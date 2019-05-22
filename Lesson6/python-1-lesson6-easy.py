# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

moving_speed = 100

class Car:
    def __init__(self,  speed=0, color="black", name="car", direction = 1,is_police=False):
        self._speed = speed
        self._color = color
        self._name = name
        self._is_police = is_police
        self._direction = direction

    def get_speed(self):
        return self._speed

    def get_color(self):
        return self._color

    def get_name(self):
        return self._name

    def get_is_police(self):
        return self._is_police

    def go(self):
        if self._speed == 0:
            self._speed = moving_speed * self._direction #имитируем движение - 2-e скорости: 0 - в покое и 100 - движение - что то типа передач
            print(f"car {self._name} is going")

    def stop(self):
        if self._speed != 0:
            self._speed = 0
            print(f"car {self._name} is stoped")

    def turn(self, direction):
        try:
            if self._speed != 0:
                raise ValueError("Speed is not 0!")
            if direction != 1 and direction != -1:
                raise ValueError("direction m.b. 1 or -1")
            self._direction = direction
            print(f"direction is turned for {self._name} on {self._direction}")
        except ValueError as err1:
            print(err1.args)
        except TypeError as err2:
            print(err2.args)

class TownCar(Car):
    def __init__(self, speed, color, name, direction):
        super().__init__(speed, color, name, direction)

class SportCar(Car):
    def __init__(self, speed, color, name, direction):
        super().__init__(speed, color, name, direction)

class WorkCar(Car):
    def __init__(self, speed, color, name, direction):
        super().__init__(speed, color, name, direction)

class PoliceCar(Car):
    def __init__(self, speed, color, name, direction):
        super().__init__(speed, color, name, direction,True)


townCar = TownCar(0,"white","Volkswagen",1)
policeCar = PoliceCar(0,"black","Ferrari",1)

print(townCar.get_color())
print(townCar.get_is_police())

print(policeCar.get_color())
print(policeCar.get_is_police())

townCar.go()
print(townCar.get_speed())
townCar.stop()
print(townCar.get_speed())
townCar.turn(-1)

policeCar.turn(-1)
policeCar.go()
print(policeCar.get_speed())
policeCar.stop()
print(policeCar.get_speed())


