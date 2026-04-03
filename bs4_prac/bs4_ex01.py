# pip install beautifulsoup4
# https://beautiful-soup-4.readthedocs.io/en/latest/

from bs4 import BeautifulSoup

fp = open('song.xml', 'r')
soup = BeautifulSoup(fp, 'html.parser')

for song in soup.find_all('song'):
    print(song['album'])
    print(song.title.string)
    print(song.length.string)
    print()
