import requests
from secret import *
from bs4 import BeautifulSoup
import sys
import re
from goose3 import Goose
from matchNASDAQlist import matchNASDAQlist
from dotenv import load_dotenv
load_dotenv()
import os # this is if I want to call the variables in .env
# from iexfinance.refdata import get_symbols
from iexfinance.stocks import Stock as IEXStock


r1 = requests.get('https://endpts.com/')
coverpage = r1.content
# print(r1)
# print(coverpage)
soup1 = BeautifulSoup(coverpage, 'html5lib')
coverpage_news = soup1.find_all('h2', class_='epn_headline epn_big')
# print(coverpage_news)
coverpage_news[1].get_text()
print("-----------------------")

links2news = [tag.find('a').get('href','') if tag.find('a') else '' for tag in coverpage_news]
headlines = [tag.find('a').get('title','') if tag.find('a') else '' for tag in coverpage_news]

for i in links2news:
    print(i)
print('===============================')

# search company names within the body of the news article
tickerList = [] # 9948 companies in NASDAQ list, contains company tickers for today's top news
companyNameList = []
companyContext = []
priceList = []

for iNews in range(len(links2news)):
    print('------------------------------------------')
    extractor = Goose()
    
    # response = requests.get(links2news[iNews])
    # article = extractor.extract(raw_html=response.content)
    
    article = extractor.extract(url=links2news[iNews])
    
    text = article.cleaned_text
    text = text.replace('\xad', '')
    # words = re.split("\s", text)
    words = text.split()
    
    # for indWords in words: # for index in range(words):
    for index, indWords in enumerate(words):
        # matchNASDAQlist find the company ticker & match
        tickerTuple  = matchNASDAQlist(indWords)
        if tickerTuple == None:
            # print(indWords + ' IS BAD')
            continue
        ticker, tickerFullName = tickerTuple

        if isinstance(ticker, str):
            if ticker not in tickerList:
                # print(repr(tickerList))
                # print(tickerFullName)
                companyNameList.append(tickerFullName)
                tickerList.append(ticker)
                companyContext.append(words[index-2] + ' ' + words[index-1] + ' ' + indWords + ' ' + words[index+1]+ ' ' + words[index+2])

                try:
                    price = IEXStock(ticker, token=IEX_token).get_price()
                    priceList.append(price)
                except Exception as ex:
                    # print(ticker + 'NOT REAL')
                    print(ex)
                    priceList.append(None)

print(tickerList)
print(companyNameList)
print(companyContext)
print(priceList)
    
    # ticker  = matchNASDAQlist(words[1])
    # if isinstance(ticker, str):
    #     print(words[1])
    #     print(type(ticker))

    # TAKE THE TICKER LIST AND FIND STOCK PRICE
