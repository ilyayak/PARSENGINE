import requests

from bs4 import BeautifulSoup

import csv
from datetime import datetime
from multiprocessing import Pool


page = 1
while True:
    r = requests.get("https://meshok.me/catalog/kresla_ekonom/?PAGEN_1=1" + str(page))
    html = BS(r.content, 'html.parser')
    items =html.select(".products-list > .product-wrap")

    if(len(items)):
        for el in items:
           title = el.select('.static > a')
           price = el.select('.static > .price-container > .price')
           print(title[0].text)
           print(price[0].text)
    data = {'name': name,
            'price':price}
        page += 1
    else:
        break

def write_csv(data):
    with open('coinmarketcap.csv','a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'],
                         data['price']))
        print(data['name'], 'parsed')

def get_html(url):
    r = requests.get(url)
    return r.text

def get_all_links(html):
     html = BS(r.content, 'html.parser')
     items =html.select(".products-list > .product-wrap")

    tds = soup.find('table', class_='').find_all('div',class_='cmc-table__column-name')

    links=[]

    for td in tds:
        a = td.find('a').get('href')
        link = 'https://coinmarketcap.com'+ a
        links.append(link)
    return links


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        name = soup.find('h2', class_='h1').text.strip()
    except:
        name = '1'
    try:
        price = soup.find('div', id='priceValue').find_all('span').text.strip()
    except:
        price = '1'

    data = {'name': name,
            'price':price}
    return data



def make_all(url):
    html = get_html(url)
    data = get_page_data(html)
    write_csv(data)


def main():
    start = datetime.now()
    url = 'https://coinmarketcap.com/all/views/all/'
    all_links = get_all_links(get_html(url))


    with Pool(40)as p:
        p.map(make_all,all_links)
    end = datetime.now()
    total = end - start
    print(str(total))

#     for index,url in enumerate(all_links):
#         html=get_html(url)
#         data=get_page_data(html)
#         write_csv(data)
#     end = datetime.now()
#     total = end - start
#     print(str(total))

if __name__ == '__main__':
    main()