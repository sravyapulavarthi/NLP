"""
Type the below command in the console of the Page Inspector to get a list of all the urls in a webpage (FactSite).

Use MS Excel to clean modify and remove duplicate links from the file.

urls = $$('a'); for (url in urls) console.log ( urls[url].href );

"""

from urllib.request import Request, urlopen
import urllib.request
from bs4 import BeautifulSoup
import csv
import requests
import re


def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext


def remove_ads(my_str):
    ret = ''
    skip1c = 0
    skip2c = 0
    for i in my_str:
        if i == '[':
            skip1c += 1
        elif i == '(':
            skip2c += 1
        elif i == ']' and skip1c > 0:
            skip1c -= 1
        elif i == ')'and skip2c > 0:
            skip2c -= 1
        elif skip1c == 0 and skip2c == 0:
            ret += i
    return ret


if __name__=='__main__':
    file = open("factsite.csv", "r")
    factsite = csv.reader(file)
    for each in factsite:
        try:
            print("Executing " + each[0])
            req = Request(each[1], headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                page = response.read()
                soup = BeautifulSoup(page, 'html.parser')
                data = soup.find('ol'.encode("utf-8", "ignore"))
                #print(data)
                inter_data = cleanhtml(str(data))
                no_ads = remove_ads(inter_data)
                final_data = no_ads.replace(".push;", "")
                output = open(each[0] + ".txt", 'w')
                output.write(final_data)
                output.close()
        except UnicodeEncodeError:
            print("Unicode Error occurred for " + each[0] + " {}" )
            continue

quit()