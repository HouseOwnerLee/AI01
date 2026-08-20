from bs4 import BeautifulSoup
import pandas as pd

# 1. 파일 읽기
file_path = 'jkj_senior.txt'
with open(file_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# 2. BeautifulSoup 객체 생성
soup = BeautifulSoup(html_content, 'html.parser')

# 3. 제품 리스트 추출 (li.product_item)
products = soup.select('li.product_item')

results = []

for product in products:
    # 제품명 추출
    name_tag = product.select_one('p.pd_title')
    name = name_tag.get_text(strip=True) if name_tag else ""

    # 가격 추출
    price_tags = product.select('p.pd_price .num')
    prices = [p.get_text(strip=True).replace(',', '') for p in price_tags if p.get_text(strip=True)]

    # 가격 처리 로직
    if not prices:
        # 가격이 없으면 None (나중에 빈칸으로 출력됨)
        final_price = None
    else:
        # 가격이 있으면 첫 번째 가격을 선택하여 정수로 변환
        try:
            final_price = int(prices[0])
        except ValueError:
            final_price = None

    results.append({
        "제품명": name,
        "가격": final_price
    })

# 4. 데이터프레임 생성
df = pd.DataFrame(results)

# 5. 가격 컬럼을 정수형이면서 빈칸 허용
df['가격'] = pd.to_numeric(df['가격']).astype('Int64')

# 6. 결과 확인
print(f"추출 완료: 총 {len(df)}개 항목")
print(df.head(20))

# 7. CSV 저장 (na_rep="" 옵션을 통해 결측치를 빈칸으로 저장)
df.to_csv("jungkwanjang_final.csv", index=False, encoding="utf-8-sig", na_rep="")

print("\n✅ 파일 저장 완료: jungkwanjang_final.csv (가격 없는 항목은 빈칸 처리됨)")