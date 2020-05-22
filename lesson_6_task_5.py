class Stationery:
    __title = 'tool'

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Отрисовка ручкой')

class Pencil(Stationery):
    def draw(self):
        print('Отрисовка карандашом')

class Handle(Stationery):
    def draw(self):
        print('Отрисовка маркером')

a = Stationery()
b = Pen()
c = Pencil()
d = Handle()

a.draw()
b.draw()
c.draw()
d.draw()
