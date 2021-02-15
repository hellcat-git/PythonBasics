import colorama
from colorama import Fore, Style
from time import sleep
circle = u'\u25CF'


class TrafficLight:
    __color = Fore.LIGHTBLACK_EX

    def running(self):

        gray = self.__color
        r = Fore.LIGHTRED_EX
        y = Fore.LIGHTYELLOW_EX
        g = Fore.LIGHTGREEN_EX

        while True:
            print(f"\r{r}\u25CF {gray}\u25CF {gray}\u25CF", end='')
            sleep(7)
            print(f"\r{gray}\u25CF {y}\u25CF {gray}\u25CF", end='')
            sleep(2)
            print(f"\r{gray}\u25CF {gray}\u25CF {g}\u25CF", end='')
            sleep(7)


traffic_light = TrafficLight()
traffic_light.running()
