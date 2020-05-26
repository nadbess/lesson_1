class Cell():
    def __init__(self, subcell):
        self.subcell = subcell
    def __add__(self, other):
        return Cell(self.subcell + other.subcell)
    def __sub__(self, other):
        return Cell(self.subcell - other.subcell)
    def __mul__(self, other):
        return Cell(self.subcell * other.subcell)
    def __truediv__(self, other):
        return Cell(self.subcell // other.subcell)
    def make_order(self, in_row):
        rows = self.subcell // in_row
        i = 0
        while i < rows:
            print('*' * in_row)
            i += 1
        print('*' * (self.subcell % in_row), '\n')


a = Cell(14)
b = Cell(25)
c = Cell(17)

a.make_order(5)
b.make_order(6)
c.make_order(4)