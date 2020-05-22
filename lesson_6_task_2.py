class Road:
    def __init__(self):
        self._length = 5000
        self._width = 20
        self._thickness = 5

    def get_weight(self):
        __unit_weight = 25
        self.weight = self._length * self._width * __unit_weight * self._thickness/1000
        return self.weight

a = Road()
print(a.get_weight())
