import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_ildong_product_names():
    result = []
    num = 1
    for i in range(1,4):
        url = "https://www.ildong.com/kor/product/list.id?page=%d&halt=&prdDisease=&prdCategory=5&searchVal=&searchOption=0" %i
        response = requests.get(url)
        response.raise_for_status()  # 접속 에러 확인

        soup = BeautifulSoup(response.text, 'html.parser')

        products = soup.find_all("dt","fMedum")

        print(f"--- 추출된 제품 목록 (총 {len(products)}개) ---")
        for product in products:
            name = product.string
            product_type = product.find_next_sibling().string.strip()
            print(f"{num}. {name}, {product_type}")
            result.append([num] + [name] + [product_type])
            num += 1
    tbl = pd.DataFrame(result, columns=["num", "product", "product_type"])
    tbl.to_csv('일동제약.csv', encoding='utf8', mode='w', index=False)


if __name__ == "__main__":
    get_ildong_product_names()