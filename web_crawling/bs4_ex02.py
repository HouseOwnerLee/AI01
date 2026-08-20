from bs4 import BeautifulSoup

html = '''
<h1 id="title">한빛출판네트워크</h1>
<div class="top">
    <ul class="menu">
        <li>
            <a href=http://www.hanbit.co.kr/member/login.html class="login">로그인</a>
        </li>
    </ul>
    <ul class="brand">
        <li>
            <a href="http://www.hanbit.co.kr/media/">한빛미디어</a>
        <li>
            <a href="http://www.hanbit.co.kr/academy/">한빛아카데미</a>
        </li>
    </ul>
</div>
'''


soup = BeautifulSoup(html, 'html.parser')

print(soup.prettify())
# print(soup.h1)
# print(soup.div)
# print(soup.ul)
# print(soup.li)
# print(soup.a)

# tag_ul_all = soup.find_all('ul')
# print(tag_ul_all)
# for tag in tag_ul_all:
#     # print(tag.li.a.get_text())
#     print(tag.li.a.string)

# tag_a_all = soup.find_all('a')
# print(tag_a_all)

# tag_a = soup.a
# print(tag_a.attrs)
# print(tag_a['href'])
# print(tag_a['class'])

# tag_ul_2 = soup.find('ul', attrs={'class': 'brand'})
# print(tag_ul_2.prettify())

# title = soup.find(id='title')
# print(title)
# print(title.string)

# > div태그의 하위 요소에서 ul의 속성값이 brand인거에서 하위요소 li
li_list = soup.select("div > ul.brand > li")
print(li_list)
for li in li_list:
    print(li.string)
