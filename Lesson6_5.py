class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"Запуск отрисовки. Написали {self.title}"


class Pen(Stationery):

    def draw(self):
        return f"Запустили ручку. Написали {self.title}"


class Pencil(Stationery):

    def draw(self):
        return f"Запустили карандаш. Написали {self.title}."


class Handle(Stationery):

    def draw(self):
        return f"Запустили маркер. Написали {self.title}."


line1 = Stationery('Всем привет!')
print(line1.draw())

line2 = Pen('Хорошего дня!')
print(line2.draw())
