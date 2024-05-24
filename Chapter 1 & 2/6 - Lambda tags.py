from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.read(), 'html.parser')

bs.findAll(lambda tag: len(tag.attrs)==2)

print(bs.find_all(lambda tag: tag.get_text() ==
 'Or maybe he\'s only resting?')
)