import datetime
class ConcertHall:
    __nameHall = "Undefined"
    __adressHall = "Undefined"
    __countSeats = 0

    def __init__(self, nameHall = "Undefined", adressHall = "Undefined", countSeats = 0):
        self.nameHall = nameHall
        self.adressHall = adressHall
        self.countSeats = countSeats

    def __str__(self):
        return("Информация о клубе:\n"+
        f"Название клуба: {self.nameHall}\n" +
        f"Адресс клуба: {self.adressHall}\n" +
        f"Количество мест в клубе: {self.countSeats}\n")

    def toJson(self):
        return {
            "nameHall": self.nameHall,
            "adressHall": self.adressHall,
            "countSeats" : self.countSeats
        }

    @property
    def nameHall(self):
        return self.__nameHall

    @property
    def adressHall(self):
        return self.__adressHall

    @property
    def countSeats(self):
        return self.__countSeats

    def LetFans(self):
        print("Запустить фанатов в концертный зал")

    @nameHall.setter
    def nameHall(self, nameHall):
        if isinstance(nameHall, str):
            self.__nameHall = nameHall
        else:
            print("Ошибка при записи названия клуба.")

    @adressHall.setter
    def adressHall(self, adressHall):
        if isinstance(adressHall, str):
            self.__adressHall = adressHall
        else:
            print("Ошибка при записи адреса клуба.")

    @countSeats.setter
    def countSeats(self,countSeats):
        if -1 < countSeats:
            self.__countSeats = countSeats
        else:
            print("Ошибка при записи вместимости клуба.")