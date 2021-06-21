
import os, re
from library import usecsv
import requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs

# ++++++++++++++++++ 명언 크롤링 ++++++++++++++++++++++++
# url = 'https://quotes.toscrape.com/'
# # html = ur.urlopen(url)
# # print("html.read()[:100]",html.read()[:100])
# # soup = bs(html.read(), 'html.parser')
#
# soup = bs(ur.urlopen(url).read(), 'html.parser')
# # quote = soup.findAll('span')
# quote = soup.findAll('div', {"class" : "quote"})
#
# for i in quote:
#     print(i.text)

# ++++++++++++++++++++기사 크롤링 +++++++++++++++++++++++++
os.chdir(r'/Users/wonbin/PycharmProjects/python-study')
news = ' https://news.daum.net'
soup = bs(ur.urlopen(news).read(), 'html.parser')
# a_tag = soup.findAll('a')

# # Hyperlink reference 추출하는 코드
# for i in quote:
#     print(i.find_all('a')[0].get('href'))

f = open('link.txt', 'w')

for i in soup.find_all('div', {"class" : "item_issue"}):
    f.write(i.find_all('a')[0].get('href')+'\n')

f.close()



# article1 = 'https://news.v.daum.net/v/20210619143509549'
# soup2 = bs(ur.urlopen(article1).read(), 'html.parser')
#
# for i in soup2.find_all('p'):
#     print(i.text)
#
# headline = soup.find_all('div', {"class" : "item_issue"})
#
# for i in headline:
#     print(i.text, '\n')
#     soup3 = bs(ur.urlopen(i.find_all('a')[0].get('href')).read(), 'html.parser')
#
#     for j in soup3.find_all('p'):
#         print(j.text)




