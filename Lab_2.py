from sys import path
path.insert(0, "/Users/romandr/Documents/studies/2 course/Python/class_lab2/")
from class_lab2.Artist import Artist
from class_lab2.ConcertHall import ConcertHall
from class_lab2.Event import Event
import json

def main():
    hall = ConcertHall(nameHall="M5", adressHall="Пушкина 120", countSeats=200)
    json.dump(hall.toJson(), open('class.json', 'w'),ensure_ascii=0, indent=3)
    x = json.load(open('class.json'))
    print(x)

    event = Event(nameHall="Большой Клуб", adressHall="Иванова 430", countSeats=500, countFans= 100)
    json.dump(event.toJson(), open('class.json', 'w'),ensure_ascii=0, indent=3)
    x = json.load(open('class.json'))
    print(x)

if __name__ == "__main__":
	main()


