from time import sleep

class TrafficLight:
    def __init__(self):
        self.__color = 'red'

    def running(self):
        while True:
            print('red')
            sleep(7)
            print('yellow')
            sleep(2)
            print('green')
            sleep(7)

a = TrafficLight()
a.running()