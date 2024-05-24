from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup



def getTitle(url):
    #making an url request and handling error in case server is down
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        #parsing the html page
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    #handling non existence attribute
    except AttributeError as e:
        return None
    return title


title = getTitle('http://www.pythonscraping.com/pages/page1.html')
if title == None:
    print('Title could not be found')
else:
    print(title)