from bs4 import BeautifulSoup
import requests
from pprint import pprint

with open("website.html", "r") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

pprint(soup.title)
pprint(soup.title.string)

pprint(soup.a)
pprint(soup.p)

soup.find_all(name="a")


