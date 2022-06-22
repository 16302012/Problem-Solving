# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 20:00:00 2022

@author: User
"""

import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(res.text,'html.parser')
#print(soup.find_all('div'))
#print(soup.select('.score')) #select module allows us to access data using CSS selector
links = (soup.select('.athing'))
subtext = (soup.select('.subtext'))
#print(links[0].get('id'))

def sort_news_by_votes(hnlist):
    return sorted(hnlist, key=lambda k:k['votes'], reverse=True)

def create_custom_hn(links,subtext):
    hn = []
    for indx,item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[indx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points',''))
            if points>99:
#            print(points)
#            hn.append(title)
                hn.append({'title':title,'link':href,'votes':points})
    return sort_news_by_votes(hn)
pprint.pprint((create_custom_hn(links, subtext)))
