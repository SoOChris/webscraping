#in this code we use reges to get links from a wikipedia page that are articles related to the currently article

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html.read(), 'html.parser')

links = bs.findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))
for link in links:
    if 'href' in link.attrs:
        print(link.attrs['href'])
