import requests
from bs4 import BeautifulSoup as bs
import time

def getNewsTitle(url, t):
    content = requests.get(url).content
    soup = bs(content, 'html.parser')

    dic = dict()
    i = 0
    while(1):
        data_arr = soup.select('.newsnow_txarea > li > div > a')
        for data in data_arr:
            if dic.get(data.text) == None:
                dic[data.text] = i
                i += 1
        time.sleep(t)

if __name__ == "__main__":
    url = "https://news.naver.com/"
    t = 10
    getNewsTitle(url, t)
    