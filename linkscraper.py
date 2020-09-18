#wildpjah
#began project Sep 16, 2020 10:23AM
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import sys



#initializing variables including webpage and html based on user input
url = input("what url would you like to scrape for links?")
page = urlopen(url)
htmlBytes = page.read()
html = htmlBytes.decode("utf-8")
soupPage = BeautifulSoup(html, "html.parser")
linkList = soupPage.find_all("a")
newFile = open(input("what would you like the new file to be called? Please include .txt: "), "w")

#pulling all links from the page
for tag in linkList:
    try:
        if re.findall("http", tag['href']) != []:   #making sure links are to a webpage
            print(tag['href'], file=newFile)
    except KeyError:
        pass
