
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page,"html.parser")
article_tag = soup.find(name="a")
print(article_tag)
