# Write To A File

""" Take the code from the How To Decode A Website exercise (if you didn't do it or just want to play with some different code, use the code from the solution), and instead of printing the results to a screen, write the results to a txt file. In your code, just make up a name for the file you are saving to. """

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

""" Ask the user to specify the name of the output file that will be saved. """
name = raw_input("Enter the name of file : ")

fp = file(name,"w")
fp.write(res)
fp.close()