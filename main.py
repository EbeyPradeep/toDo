import requests
from bs4 import BeautifulSoup


def add_numbers(a, b):
    return {"result": a - b}


if __name__ == '__main__':
    x = requests.get('https://w3schools.com')
    print(x.text)
    soup = BeautifulSoup(x.text)
    print(soup.prettify())
