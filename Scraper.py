import time
import requests
from bs4 import BeautifulSoup

url = "https://www.icheckmovies.com/lists/imdbs+top+250/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

movie_tags = list(soup.find_all("a", href=lambda x: x and x.startswith("/movies/")))

titles = list()
movies_dict = dict()

count1 = 0
for tag in movie_tags:
    if (count1 % 4 == 0):
        titles.append(tag["title"].replace("View detailed information on ", " "))
    count1 += 1



ul = soup.find_all("ul", class_="tagList clearfix")
count2 = 0
for genre_list in ul:
    list_items = genre_list.find_all("li")
    genres = list()
    for list_item in list_items:
        genre_link = list_item.find("a", href=lambda x:x and x.startswith("/lists/imdbs+top+250/?tags=genre"))
        if genre_link:
            genres.append(genre_link.text)
    movies_dict[titles[count2]] = genres
    count2 += 1


for movie in movies_dict.keys():
    print(f"{movie}:{', '.join(movies_dict[movie])}")