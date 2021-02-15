class Auto:
    # атрибуты класса
    auto_count = 0
    # конструктор
    # атрибуты объекта
    def __init__(self, name, model, year):
        self.n = name
        self._m = model
        self.__y = year
        Auto.auto_count += 1
        print(name, model, year)
        self.on_start()

    # методы:
    def on_start(self):
        print(f"Go - go car {self._m}")

    def on_stop(self):
        print("Stop")


auto_1 = Auto("Mazda", "CX9", 2020)
auto_1.on_start()
print(auto_1._m)
#auto_1.name = "Mazda"
#print(auto_1.name)

auto_2 = Auto("BMW", "X3", 2021)
auto_2.on_start()
#print(auto_2.auto_count)