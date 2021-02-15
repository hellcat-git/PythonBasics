class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self._income = {"wage": wage, "bonus": bonus}
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):
    def get_full_name(self):
        return f"Full name is: {self.name} {self.surname}, {self.position}"

    def get_total_income(self):
        return f"The full income is: {self._income.get('wage')+self._income.get('bonus')}"

    def get_full_info(self):
        print(f"{Position.get_full_name(self)}. {Position.get_total_income(self)}")


info = Position("Anna", "Shmit", "manager", 120, 50)
info.get_full_info()

