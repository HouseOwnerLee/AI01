from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
import warnings

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

fp = open("joins.xml", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

items = soup.find_all('item')
for item in items:
    print(item.title.string)
    print(item.description.string)
    print()
