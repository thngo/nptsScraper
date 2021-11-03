import requests
from bs4 import BeautifulSoup
import sys

ticker = 'gme' # can make this input from results of webscraping
print('aaaaaaaaa')
r1 = requests.get('https://www.nasdaq.com/market-activity/stocks/' + ticker) # got stuck  here
print('bbbbbbbbbbbbbbb')
resultPage = r1.content
print(resultPage)
soupSearchRes = BeautifulSoup(resultPage, 'html5lib')
print(soupSearchRes)
# soupSearchResStock = soupSearchRes.find_all('span', class_='symbol-page-header__pricing-price')

# print(soupSearchResStock)


# test = ['https://endpts.com/' + tag.find('a').get('href','') if tag.find('a') else '' for tag in soupSearchResStock]

# test = ['https://endpts.com/' + tag.find('a').get('title','') if tag.find('a') else '' for tag in soupSearchResStock]

# for i in test:
#     print(i)

