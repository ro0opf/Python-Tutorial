import requests
from bs4 import BeautifulSoup as bs
import time
import multiprocessing as mp
import os
import konlpy
from konlpy.tag import Kkma
 
newsUrl = []

def _get():
    html = requests.get('https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80').content
    soup = bs(html, 'html.parser')

    res = []
    data = soup.find(class_='type01')
    for a in data.find_all('li'):
        try:
            res.append(a.find(class_='_sp_each_url').get('href'))
        except Exception as e:
            print(e)
    return res


def _get_text(url):
    html = requests.get(url).content
    soup = bs(html, 'html.parser')

    data = soup.find(id='articleBodyContents').text
    
    kkma = Kkma()
    nouns = kkma.nouns(data)
    print(nouns)
    return 

if __name__ == '__main__':
    start_time = time.time()

    pool = mp.Pool(mp.cpu_count())
    
    newsUrl = _get()

    for url in newsUrl:
        _get_text(url)
  
    pool.close()
    pool.join()

    print("--- %s seconds ---" % (time.time() - start_time))
