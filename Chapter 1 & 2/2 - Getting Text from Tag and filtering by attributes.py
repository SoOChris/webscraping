from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), 'html.parser')

#filtering by attributes and tags
nameList = bs.findAll('span', {'class':'green'})
for name in nameList:
    print(name.getText())