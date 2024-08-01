import time
import requests
from bs4 import BeautifulSoup


def ExtractData():

    url = "https://www.icheckmovies.com/lists/imdbs+top+250/"
    # Adding headers to prevent the website from blocking the scraper
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    try:
        response = requests.get(url, headers=headers)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return


    soup = BeautifulSoup(response.text, "html.parser")
    
    movies_dict = dict()
    titles = extractTitles(soup)
    genres = extractGenres(soup)


    movie_index = 0
    for genre in genres:
        movies_dict[titles[movie_index]] = genre
        movie_index += 1


    # for movie in movies_dict.keys():
    #     print(f"{movie}:{', '.join(movies_dict[movie])}")
    
    return movies_dict


def extractTitles(soup):
    movie_tags = list(soup.find_all("a", href=lambda x: x and x.startswith("/movies/")))
    titles = list()

    # Checking to see if count is dividable by 4 because every 4 tags belong to one movie
    count = 0
    for tag in movie_tags:
        if (count % 4 == 0):
            titles.append(tag["title"].replace("View detailed information on ", " "))
        count += 1

    return titles

def extractGenres(soup):
    genres = list()

    ul = soup.find_all("ul", class_="tagList clearfix")
    for genre_list in ul:
        list_items = genre_list.find_all("li")
        genre = list()
        for list_item in list_items:
            genre_link = list_item.find("a", href=lambda x:x and x.startswith("/lists/imdbs+top+250/?tags=genre"))
            if genre_link:
                genre.append(genre_link.text)
        genres.append(genre)
    
    return genres