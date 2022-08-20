class Car:
     def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
     def go(self):
        print("{} поїхала".format(self.name))
     def stop(self):
        print("{} зупинилася".format(self.name))
     def turn(self, direction):
        print("{} повернула {}".format(self.name, direction))      



car1 = Car("100 км/год", "червоний", "Car1", False)
car2 = Car("60 км/год", "синій", "Car2", False)
car3 = Car("100 км/год", "білий", "Car3", True)

car1.turn("вправо")
car2.stop()
car3.go()