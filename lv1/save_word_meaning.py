#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup as bs
import time
import codecs

def getWordMeaning(url, keyword, my_file):
    params = {'query' : keyword}
    content = requests.get(url, params=params).content
    soup = bs(content, 'html.parser')
    meaning = soup.select_one('p[style="margin-left:1px;"]')
    if meaning is None:
        my_file.write("{}의 의미는 존재하지 않습니다.\n\n".format(keyword))
        return

    my_file.write("{}의 의미는 다음과 같습니다.\n".format(keyword))
    my_file.write(meaning.text)
    my_file.write("\n")

if __name__ == "__main__":
    url = "https://endic.naver.com/search.nhn?sLn=kr&searchOption=all"

    my_file = codecs.open('meaning.txt', 'w', 'utf-8')
    while(True):
        keyword = input("검색할 영어 단어를 입력해주세요 : (종료는 -1)")
        if keyword == '-1':
            break
        getWordMeaning(url, keyword, my_file)
    my_file.close()