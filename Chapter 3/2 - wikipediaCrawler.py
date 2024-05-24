from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re



random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
    bs = BeautifulSoup(html.read(), 'html.parser')
    return bs.find('div',{'id':'bodyContent'}).find_all('a',href=re.compile('^(/wiki/)((?!:).)*$'))

links = getLinks('/wiki/Kevin_Bacon')
