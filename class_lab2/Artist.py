class Artist():
    __realName = "Undefined"
    __nickName = "Undefined"
    __age = 1
    __funsNumber = 0
    __popularSongs = ["Undefined" for i in range(5)]

    def __init__(self,realName = "Undefined", nickName = "Undefined", age = 1, funsNumber = 0, popularSongs = ["Undefined" for i in range(5)]):
        self.realName = realName
        self.nickName = nickName
        self.age = age
        self.funsNumber = funsNumber
        self.popularSongs = popularSongs

    def __str__(self):
        return("Информация об артисте:\n"+
        f"Реальное имя артиста: {self.realName}\n" +
        f"Псевдоним артиста: {self.nickName}\n" +
        f"Возраст: {self.age}\n"+
        f"Популярные песни: \n"+
        f"1|{self.popularSongs[0]} \n"
        f"2|{self.popularSongs[1]} \n"
        f"3|{self.popularSongs[2]} \n"
        f"4|{self.popularSongs[3]} \n"
        f"5|{self.popularSongs[4]} \n"
        f"Количество фанатов: {self.funsNumber}\n")

    def CostConcert(self, cityPopulation):
        print(f"Стоимость концерта в данном городе составляет { self.funsNumber/ 143000000 * 100 * cityPopulation * 300}")

    def PerfomanceArtist(self):
        print (f"Артист {self.__nickName}: ")
        for element in self.__popularSongs:
            if (element != "Undefined"):
                print(f"поет песню {element}")


    @property
    def realName(self):
        return self.__realName
    @property
    def nickName(self):
        return self.__nickName
    @property
    def age(self):
        return self.__age
    @property
    def popularSongs(self):
        return self.__popularSongs
    @property
    def funsNumber(self):
        return self.__funsNumber

    @realName.setter
    def realName(self,realName):
        if isinstance(realName, str):
            self.__realName = realName
        else:
            print("Ошибка при записи имени.")

    @nickName.setter
    def nickName(self,nickName):
        if isinstance(nickName, str):
            self.__nickName = nickName
        else:
            print("Ошибка при записи псевдонима.")

    @age.setter
    def age(self,age):
        if 0 < age < 100:
            self.__age = age
        else:
            print("Ошибка при записи возраста.")

    @popularSongs.setter
    def popularSongs(self,popularSongs):
        if isinstance(popularSongs, list):
            if len(popularSongs) == 5:
                self.__popularSongs = popularSongs
            else:
                print("Ошибка при записи популярных песен")

    @funsNumber.setter
    def funsNumber(self,funsNumber):
        if -1 < funsNumber:
            self.__funsNumber = funsNumber
        else:
            print("Ошибка при записи количества фанатов.")

