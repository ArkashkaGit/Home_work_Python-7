"""
Задание 1.
Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).
В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time
Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
from time import sleep 

class TrafficLight:
    def __init__(self):
        self.__color = "START"
    
    def runing(self):
        print (self.__color)
        sleep(2)
        while True:
            self.__color = "\nRED"
            print(self.__color)
            sleep(7)

            self.__color = "YELLOW"
            print(self.__color)
            sleep(2)

            self.__color = "GREEN"
            print(self.__color)
            sleep(10)

TrafficLight().runing()
