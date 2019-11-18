import sqlite3
import requests
from bs4 import BeautifulSoup

response = requests.get("http://books.toscrape.com/catalogue/category/books/history_32/index.html")
soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article")
for book in books:
    print(book.find("h3").find("a")["title"])

