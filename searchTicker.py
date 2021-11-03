import requests
from bs4 import BeautifulSoup
import sys
ticker = 'GME' # can make this input from results of webscraping

r1 = requests.get('https://www.nasdaq.com/market-activity/stocks/' + ticker)
resultPage = r1.content
soupSearchRes = BeautifulSoup(resultPage, 'html5lib')
print(soupSearchRes)
soupSearchResStock = soupSearchRes.find_all('h2', class_='epn_headline epn_big')

print(soupSearchResStock)


# test = ['https://endpts.com/' + tag.find('a').get('href','') if tag.find('a') else '' for tag in soupSearchResStock]

# test = ['https://endpts.com/' + tag.find('a').get('title','') if tag.find('a') else '' for tag in soupSearchResStock]

# for i in test:
#     print(i)

