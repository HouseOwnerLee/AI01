from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv

def main():
    query = input('검색할 키워드를 입력하세요: ')
    print("-----------------------------------------------")
    url = 'https://www.naver.com/'
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2)

    search_box = driver.find_element(By.ID, "query")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

    driver.find_element(By.XPATH, '//*[@id="lnb"]/div[1]/div/div[1]/div/div[1]/div[5]/a').click()
    time.sleep(3)

    result = []

    blog_posts = driver.find_elements(By.CLASS_NAME, "sds-comps-full-layout.j0OqL9shijC3k2GDFoLw")
    for i in blog_posts:
        title = i.find_element(By.CLASS_NAME,"sds-comps-text-type-headline1").text
        link = i.find_element(By.CLASS_NAME,"fender-ui_228e3bd1").get_attribute("href")
        print(title)
        print(link)
        result.append({"제목":title, "링크":link})

    with open('naver_%s.csv'%query, 'w',encoding='utf8',newline='') as fp:
        csv_writer = csv.writer(fp)

        csv_writer.writerow(result[0].keys())
        for post in result:
            csv_writer.writerow(post.values())

    driver.close()

if __name__ == '__main__':
    main()