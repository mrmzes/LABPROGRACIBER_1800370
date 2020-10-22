#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

import requests

url = input("Enter a website to extract the URL's from: ")

r  = requests.get("http://" +url)

data = r.text

soup = BeautifulSoup(data,'html.parser')
#print (soup.find_all('img'))

for link in soup.find_all('img'):
    if link is not None:
        print(link.get('src'))
