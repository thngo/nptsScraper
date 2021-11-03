import csv
import re

def matchNASDAQlist(strInput):

    # with open('commonWords.csv', newline='',encoding="utf-8-sig") as blackList:
    #blackListReader = csv.reader(blackList, delimiter='\n')
    blackListReader = open('commonWords.txt', 'r').readlines()

    for item in blackListReader:
        #print(repr(item))
        #print(item.index("the"))
            # print('aaaaaaa')
        if strInput == item.strip():
            return None

    with open('nasdaqlisted.txt', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='|', quotechar='"')
        for row in csvreader:
            # print('TICKER: {}\tNAME: {}'.format(row[1], row[2])) # row[1] is the ticker. row[2] is the company name
            # in nasdaqlisted.txt, row[0] is the ticker, row[1] is the company name
            fullstring = row[1] # get company names
            ticker = row[0]
            companyName = re.split("-", fullstring)
            # print(companyName[0])
            # companyNameParts = re.split("/s", companyName[0])
            # companyNameParts = re.split("/s", fullstring)
            companyNameParts = fullstring.split()
            
            for item in companyNameParts[0:3]: # assuming company names is contained in the first 3 words
                if strInput == item:
                    return ticker, fullstring

            # if strInput in fullstring:
            #     # print("Found!")
            #     print(row[2])
            #     # print(row[1])
            #     return(row[1])
        