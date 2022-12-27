from Artist import Artist
import random
from ConcertHall import ConcertHall

class Event(ConcertHall):
    __countFans = 0
    def __init__(self,nameHall = "Undefined", adressHall = "Undefined", countSeats = 0, countFans = 0):
        super().__init__(nameHall, adressHall, countSeats)
        self.countFans = countFans

    def __str__(self):
        return (f"Информация о мероприятии:\n"+
        f"Количество гостей: {self.countFans}\n")

    def toJson(self):
        return {
            "nameHall": self.nameHall,
            "adressHall": self.adressHall,
            "countSeats" : self.countSeats,
            "countFans" : self.countFans
        }

    def MakeEvent(self):
        print("Начало концерта ")
        self.PerfomanceArtist()

    @property
    def countFans(self):
        return self.__countFans

    @countFans.setter
    def countFans(self,countFans):
        self.__countFans = countFans    