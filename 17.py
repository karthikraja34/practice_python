# Decode A Web Page 

""" Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage. """

import urllib
from bs4 import  BeautifulSoup


page = urllib.urlopen("https://www.nytimes.com/")

soup = BeautifulSoup(page, 'html.parser')
name_box = soup.find_all('h2', attrs={'class': 'story-heading'})

li =[]
for title in name_box:
    value = title.text.strip()
    li.append(value)
# name = name_box.text.strip()
print '\n'.join(li)