import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html,"html.parser")

top_movies = soup.find_all("h3",class_="title")

movies_title = [movie.getText() for movie in top_movies]

movies_title_reverse = movies_title[::-1]

with open("movie.txt",mode="w",encoding="utf-8") as file:
    for movie in movies_title_reverse:
        file.write(f"{movie}\n")
