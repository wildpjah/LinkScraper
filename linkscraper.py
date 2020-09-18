#wildpjah
#began project Sep 16, 2020 10:23AM
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import sys
import tkinter
from tkinter import *
from tkinter import messagebox
import os


def getLinks():
    #initializing variables including webpage and html based on user input
    url = urlBox.get()
    page = urlopen(url)
    htmlBytes = page.read()
    html = htmlBytes.decode("utf-8")
    soupPage = BeautifulSoup(html, "html.parser")
    linkList = soupPage.find_all("a")
    newFile = open(os.path.join(fileLocationBox.get(), fileBox.get(), ".txt", "w"))

    #pulling all links from the page
    for tag in linkList:
        try:
            if re.findall("http", tag['href']) != []:   #making sure links are to a webpage
                print(tag['href'], file=newFile)
        except KeyError:
            pass
    

    #success message
    messagebox.showinfo("Success!", "file successfully created")



#creating gui
top = tkinter.Tk()
urlFrame = Frame(top)
urlFrame.pack(fill = X)

fileFrame = Frame(top)
fileFrame.pack(fill = X)

fileLocationFrame = Frame(top)
fileLocationFrame.pack(fill = X)

buttonFrame = Frame(top)
buttonFrame.pack(fill = X)

urlLabel = Label(urlFrame, text="url to scrape:")
urlLabel.pack(side = LEFT)
urlBox = Entry(urlFrame)
urlBox.pack(side = LEFT, fill = BOTH)

fileLabel = Label(fileFrame, text="name of new file:")
fileLabel.pack(side = LEFT)
fileBox = Entry(fileFrame)
fileBox.insert(0, "newFileName")
fileBox.pack(side = LEFT)
txtLabel = Label(fileFrame, text = ".txt")
txtLabel.pack(side = LEFT)

fileLocationLabel = Label(fileLocationFrame, text = "Where would you like the file saved?")
fileLocationLabel.pack(side = LEFT)
#path to documents folder for default file location
docPath = os.path.join(os.path.expanduser("~"), "Documents")
fileLocationBox = Entry(fileLocationFrame, width = 40)
fileLocationBox.insert(0, docPath)
fileLocationBox.pack(side = LEFT)

scrapeButton = Button(buttonFrame, text = "Get Links!", command = getLinks)
scrapeButton.pack()
top.mainloop()