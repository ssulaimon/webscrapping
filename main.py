import requests
from bs4 import BeautifulSoup
import datetime

# Connecting to end point for movies
endPoint = requests.get("https://www.thenetnaija.net/videos/movies").text
## converting html to lxml
parseLxml = BeautifulSoup(endPoint, "lxml")
cards = parseLxml.find_all("article", class_="file-one shadow")


for item in cards:
    movieName = item.h2.a.text
    downloadLink = item.h2.a["href"]
    ## create a text file adding the movies
    with open("./movie.txt", "a") as f:
        f.writelines(f"Movie name: {movieName}\nDownload link: {downloadLink}\n \n")
