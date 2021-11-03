import requests
from bs4 import BeautifulSoup
import sys
import re
from goose3 import Goose
from matchNASDAQlist import matchNASDAQlist

ticker = 'OK' # can make this input from results of webscraping

r1 = requests.get('https://www.google.com/search?q=' + ticker + '+company+stock+NASDAQ')
resultPage = r1.content
soupSearchRes = BeautifulSoup(resultPage, 'html5lib')
# print(soupSearchRes)
# soupSearchResStock = soupSearchRes.find_all('h2', class_='epn_headline epn_big')
soup1 = BeautifulSoup(resultPage, 'html5lib')
tickerGroup = soup1.find_all('span', class_='vk_bk')
tickerGroup2 = soup1.find_all('div', class_='oPhL2e')
# print(coverpage_news)
# coverpage_news[1].get_text()
print(tickerGroup)
print(tickerGroup2)
tickerReal = [tag.find('span').get('class','') if tag.find('span') else '' for tag in tickerGroup2]
print(tickerReal)