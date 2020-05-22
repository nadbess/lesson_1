class Car:
    def __init__(self):
        self.speed = 90
        self.color = 'red'
        self.is_police = False

    def go(self):
        print('Car goes directly')
    def stop(self):
        print('Car has stopped')
    def turn(direction):
        print('Car has turned')
    def show_speed(self):
        print(self.speed)

class TownCar(Car):
    def __init__(self):
        self.speed = 60
        self.color = 'blue'
        self.is_police = True

class WorkCar(Car):
    def __init__(self):
        self.speed = 40

mazda = Car()
mazda.stop()
mazda.turn()
mazda.show_speed()

police = TownCar()
police.show_speed()

vehicle = WorkCar()
vehicle.show_speed()
vehicle.go()