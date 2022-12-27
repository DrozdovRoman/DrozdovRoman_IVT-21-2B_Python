from functools import reduce
import requests
import lxml
from bs4 import BeautifulSoup

from sklearn import datasets
import pandas as pd


# Данные введенные вручную 

# temp = [int(element) for element in input().split()]
temp_list = [int(element) for element in "1 2 3 4 5 6".split()]

tempSquared = list(map(lambda temp: temp ** 2, temp_list))
print(tempSquared,"\n")

tempSum = reduce((lambda x,y: x + y), tempSquared)
print(tempSum,"\n")

# Данные полученные при парсинге

url = 'https://www.kinoafisha.info/releases/'
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
film_rating = soup.find_all("div", class_='movieList_item movieItem movieItem-grid grid_cell3')

filmName =[]
film_like = []
film_dislike = []
filmsNumRating = []
for film in film_rating:
    film_name = film.find('a', class_='movieItem_title')
    filmName.append(film_name.text)
    like = int(film.find_all('span',class_='like_num')[0].text)
    dislike = int(film.find_all('span',class_='like_num')[1].text)
    film_like.append(like)
    film_dislike.append(dislike)
    filmsNumRating.append(reduce((lambda like,dislike: like + dislike),[like,dislike]))

filmsLikeRating = list(map((lambda like,dislike: round(like /((like + dislike) / 100)) if (like + dislike > 0) else 0),film_like,film_dislike))

for i in range(3):
    print(f"Название фильма: {filmName[i]}\nСуммарное количество лайков и дизлайков: {filmsNumRating[i]}\nПроцентное соотношение лайков к общему количеству: {filmsLikeRating[i]}\n\n")


iris = datasets.load_iris()
x = dict(map(lambda *args: args, iris.target_names,iris.data[:3]))
y = reduce((lambda x,y: x + y / len(iris.data)), iris.data)
print(x)
print(y)
