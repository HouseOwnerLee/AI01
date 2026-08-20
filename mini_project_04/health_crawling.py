import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. 대상 URL 설정


try:
    result = []
    num = 1
    for i in range(1,6):
        url = "https://www.yuhan.co.kr/Products/List/?cid=179&p=%d" %i
        response = requests.get(url)
        response.raise_for_status()  # 접속 오류 시 예외 발생
        # 3. HTML 파싱
        soup = BeautifulSoup(response.text, 'html.parser')
        # 4. 제품명 추출
        product_names = soup.find_all('span', 'tit')

        print(f"--- 총 {len(product_names)}개의 제품을 찾았습니다 ---")

        for product in product_names:
            # 텍스트 앞뒤 공백 제거
            name = product.get_text(strip=True)
            product_type = product.find_next_sibling().string
            result.append([num] + [name] + [product_type])
            num += 1

    tbl = pd.DataFrame(result, columns=["num", "product", "type"])
    tbl.to_csv('유한양행.csv', encoding='utf8', mode='w', index=False)

except Exception as e:
    print(f"크롤링 중 오류가 발생했습니다: {e}")





