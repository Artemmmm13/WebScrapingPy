import requests
import json
from bs4 import BeautifulSoup

ini_url = 'https://books.toscrape.com/catalogue/category/books_1/index.html'


def parse(url, counter, books):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    book_list = soup.find_all("article", class_='product_pod')
    for book in book_list:
        data = {}
        data['Title: '] = book.h3.a['title']
        data['Price: '] = book.select('div p.price_color')[0].get_text()
        data['Image href: '] = 'https://books.toscrape.com/' + book.img['src'][3:]
        books.append(data)
    try:
        next_page = soup.find("li", class_='next').a['href']
        if next_page:
            next_url = 'https://books.toscrape.com/catalogue/category/books_1/' + next_page
            counter += 1
            if counter <= 50:
                print(f"Scraping page {counter}: {next_url}")
                parse(next_url, counter, books)
    except:
        print("No more pages")
    if counter == 50:
        with open('books.json', 'w') as outfile:
            json.dump(books, outfile, indent=2)


if __name__ == '__main__':
    books = []
    parse(ini_url, 1, books)
