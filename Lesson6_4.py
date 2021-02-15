from random import randint


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        return f"Текущая скорость {self.speed}"

    def go(self):
        return f"The {self.color} {self.name}"

    def stop(self):
        return f"The {self.color} {self.name} has stopped"

    def turn(self):
        sides = ['left', 'right', 'u-turn']
        return f"The {self.color} {self.name} made {sides[randint(0, 2)]} turn"


class TownCar(Car):

    def show_speed(self):
        s = self.speed
        if s > 60:
            return "Произошло превышение скорости!"
        else:
            return f"Текущая скорость {s}"


class WorkCar(Car):

    def show_speed(self):
        s = self.speed
        if s > 40:
            return "Произошло превышение скорости!"
        else:
            return f"Текущая скорость {s}"


class PoliceCar(Car):

    def show_info(self):
        pass


auto = TownCar(90, 'red', 'BMW', False)
print(auto.turn())
print(auto.show_speed())

auto = PoliceCar(130, 'blue', 'Niva', True)
print(auto.turn())
print(auto.show_speed())