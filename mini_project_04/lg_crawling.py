import requests
from bs4 import BeautifulSoup
import pandas as pd

def lg_crawling():
    result = []
    num = 1
    for i in range(1,7):
        url = 'http://www.lglifegarden.com/product/list.jsp?cid1=L&cid2=%d' %i
        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'html.parser')
        brand = soup.find('a','active')

        li = soup.find('div','list-basic')
        products = li.find_all('span')
        for product in products:
            result.append([num] + [product.string] + [brand.string])
            num += 1
    tbl = pd.DataFrame(result, columns=["num", "product", "brand"])
    tbl.to_csv('lg_생활건강.csv', encoding='utf8', mode='w', index=False)


if __name__ == '__main__':
    lg_crawling()