import requests

from bs4 import BeautifulSoup as BS

import csv
from datetime import datetime
from multiprocessing import Pool


page = 1
while True:
    r = requests.get("https://meshok.me/catalog/kresla_ekonom/?PAGEN_1=2" + str(page))
    html = BS(r.content, 'html.parser')
    items =html.select(".products-list > .product-wrap")

    if(len(items)):
        for el in items:
           title = el.select('.static > a')
           price = el.select('.static > .price-container > .price')

           print(title[0].text)
           print(price[0].text)
        page += 1
    else:
        break