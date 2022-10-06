import requests
from bs4 import BeautifulSoup


def important_awsome(test):
    return int(test)


if __name__ == '__main__':
    x = requests.get('https://w3schools.com')
    print(x.text)
    soup = BeautifulSoup(x.text)
    print(soup.prettify())
