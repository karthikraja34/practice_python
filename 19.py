# Decode A Web Page Two 

""" 
Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

The article is long, so it is split up between 4 pages. Your task is to print out the text to the screen so that you can read the full article without having to click any buttons.

(Hint: The post here describes in detail how to use the BeautifulSoup and requests libraries through the solution of the exercise posted here.)

This will just print the full text of the article to the screen. It will not make it easy to read, so next exercise we will learn how to write this text to a .txt file.


"""
import urllib
from bs4 import BeautifulSoup

page = urllib.urlopen("http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture")

soup = BeautifulSoup(page,"html.parser")
content = soup.find_all('section',attrs={'class':'content-section'})


li =[]
for title in content:
    value = title.text.strip()
    li.append(value)
# name = name_box.text.strip()
res = '\n'.join(li).encode('utf-8').strip()

fp = file("19.txt","w")
fp.write(res)
fp.close()
# print content

