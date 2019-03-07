import requests
from bs4 import BeautifulSoup as bs
import time
import multiprocessing as mp
import os
import urllib.request
 
def _get(keyword):
    html = requests.get('https://search.naver.com/search.naver?where=image&sm=tab_jum&query=' + keyword).content
    soup = bs(html, 'html.parser')

    #proc = os.getpid()
    data = soup.find(class_='img_area _item')
    imageUrl = data.find(class_='_img').get('data-source')

    saveImage(keyword, imageUrl)
    #print("{}".format(proc))
    return

def saveImage(keyword, imageUrl):
    outpath = "./images/"
    outfile = keyword + ".png"

    if not os.path.isdir(outpath):
        os.makedirs(outpath)

    urllib.request.urlretrieve(imageUrl, outpath+outfile)
    return

if __name__ == '__main__':
    start_time = time.time()

    pool = mp.Pool(mp.cpu_count())
    while(True):
        keyword = input('Input Keyword : (if you want to close, enter \'exit\' please) \n')
        if keyword == 'exit':
            break
        else:
            pool.apply_async(_get(keyword))
  
    pool.close()
    pool.join()

    print("--- %s seconds ---" % (time.time() - start_time))
