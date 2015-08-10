# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import requests
import os
from Tkinter import *
from bs4 import BeautifulSoup as bs


def printtext():
    global e
    global m
    global n
    url = e.get()
    div = m.get()
    clas = n.get()
    r = requests.get(url)
    soup = bs(r.content)
    n_data = soup.find_all(div,{"class":clas})
    for data in n_data:
        with open(os.path.expanduser("~/Desktop/WebScrap.txt"), "a") as text_file:
            text_file.write("%r" %data.text)
            
root = Tk()
root.title('Web Scrapper')

label_1 = Label(root, text = "Enter URL")
label_1.grid(row = 0,sticky=W)
label_2 = Label(root, text = "Enter Tag")
label_2.grid(row = 1,sticky=W)
label_3 = Label(root, text = "Enter Tag-Class")
label_3.grid(row = 2,sticky=W)
label_3 = Label(root, text = "Check WebScrap.txt on Desktop")
label_3.grid(row = 4,column = 1)


e = Entry(root)
e.grid(row=0,column=1)
m = Entry(root)
m.grid(row=1,column=1)
n = Entry(root)
n.grid(row=2,column=1)

b = Button(root,text='submit',command=printtext)
b.grid(row=3,column=1)

root.mainloop()

# <codecell>


