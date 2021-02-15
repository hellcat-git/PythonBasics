class Road:
    def __init__(self, width, length):
        self._width = width
        self._length = length

    def area(self, weight, thickness):
        vol = round(self._width * self._length * weight * thickness / 1000, 2)
        print(f"Для покрытия дороги необходимо: {vol} тонн")


res = Road(5, 250)
res.area(25, 1)
