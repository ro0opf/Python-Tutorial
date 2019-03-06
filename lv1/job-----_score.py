import requests
from bs4 import BeautifulSoup as bs
import time
import multiprocessing as mp
import os


def _get(index, title_list, score_list):
    html = requests.get('https://www.jobplanet.co.kr/companies/' + str(index)).content
    soup = bs(html, 'html.parser')

    proc = os.getpid()
    for data in soup.find_all(class_='company_info_wrap'):
        title = data.find(class_='tit')
        score = data.find(class_='icon text_info')
        title_list.append(title.text)
        score_list.append(score.text)
    
    print('{0}'.format(proc))
    return

if __name__ == '__main__':
    start_time = time.time()
    
    title_list = []
    score_list = []

    for i in range(1,30):
        _get(i,title_list, score_list)

    count = 1
    for t in title_list:
        print("{}{} {} {}".format(count, "위", t, score_list[count-1]))
        count += 1

    print("--- %s seconds ---" % (time.time() - start_time))