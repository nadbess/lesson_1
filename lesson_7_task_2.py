class Vetements():
    def __init__(self, name):
        self.name = name

class Coat(Vetements):
    def get_consumption(self, V):
        self.consumption = V / 6.5 + 0.5
        print(self.consumption)

class Costume(Vetements):
    def get_consumption(self, H):
        self.consumption = 2 * H + 0.3
        print(self.consumption)

a = Coat('пальто')
b = Costume('костюм')
a.get_consumption(10)
b.get_consumption(5)
