class Worker:
    name = 'Ivan'
    surname = 'Ivanov'
    position = 'student'
    _income = {"wage": 1200, "bonus": 300}

class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)
    def get_total_income(self):
        print(sum(self._income.values()))

first_worker = Position()
first_worker.get_full_name()
first_worker.get_total_income()
