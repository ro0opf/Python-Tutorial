import requests
from bs4 import BeautifulSoup

html = requests.get('https://search.naver.com/search.naver?sm=tab_hty.top&where=post&query=ro0opf&oquery=a&tqi=Uc%2BgmspySDlsscImflGssssssid-378122').content
soup = BeautifulSoup(html, 'html.parser') 
		
title_list = [] 

for realtime in soup.find(class_='lst_realtime_srch _tab_area').find_all('li'): 
    tg2 = realtime.find(class_='tit') 
    title_list.append(tg2.text)

for i, t in enumerate(title_list,1): 
    print("{}{} {}".format(i, "위", t))
