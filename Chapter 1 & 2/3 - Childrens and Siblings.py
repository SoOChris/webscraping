from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.read(), 'html.parser')

#Dealing with childrens and siblings:

#for sibling in bs.find('table',{'id':'giftList'}).tr.next_siblings:
 #   print(sibling.getText())

#in this example it will get all the rows of the table except for the one representing the header, because a tag cannot be its own sibling

for child in bs.find('table', {'id':'giftList'}).children:
   print(child.getText())

#it will iterate all the child elements

