import os, re, codecs, datetime, requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs
from library import usecsv


class ArticleCollector:
    def __init__(self):
        os.chdir(r'/Users/wonbin/PycharmProjects/python-study')
        self.news = ' https://news.daum.net'
        self.f = open(str(datetime.date.today()) + 'article.txt', 'w')
        self.soup = bs(ur.urlopen(self.news).read(), 'html.parser')

        self.headline_article_collector()

    def headline_article_collector(self):
        print("headline_article_collector 함수에 들어왔습니다")
        for i in self.soup.find_all('div', {"class": "item_issue"}):
            try:
                self.f.write(i.text + '\n')
                self.f.write(i.find_all('a')[0].get('href') + '\n')
                soup2 = bs(ur.urlopen(i.find_all('a')[0].get('href')).read(), 'html.parser')

                for j in soup2.find_all('p'):
                    self.f.write(j.text)

            except Exception as e:
                print(e)
                pass
        print("headline_article_collector 완료!!!!")
        print("headline_article_collector 함수를 종료합니다.")
        print("최종파일이름 " + self.f.name + "에 저장했다!!!")
        self.f.close()


if __name__ == '__main__':
    c = ArticleCollector()
