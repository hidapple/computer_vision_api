from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://books.rakuten.co.jp/search/dt?mt=0&o=0&cy=0&h=100&g=001013001&e=0&v=2&spv=2&s=1&sv=30"
html = urlopen(url)
soup = BeautifulSoup(html, "html.parser")

items = soup.find_all(class_='rbcomp__item-list__item__image')
with open('images/path.txt', 'w') as f:
    for item in items:
        img = item.find('img')['src']
        if img.find('noimage') == -1:
            f.write("https:" + img + "\n")

