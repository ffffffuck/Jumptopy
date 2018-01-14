from pandas import DataFrame
from bs4 import BeautifulSoup
import requests

result=[]

URL='http://www.naver.com'
html = requests.get(URL).text
soup = BeautifulSoup(html,'lxml')
live_ranking = soup.find_all('a',attrs={'data-clk':"lve.keyword"})

for i in live_ranking:
    rank= list(i.strings)[1]
    search= list(i.strings)[3]

    result.append([rank]+[search])

naver_table = DataFrame(result,columns=('순위','검색어'))
naver_table.to_csv('네이버실시간.csv', encoding='utf-8-sig',mode='w',index=False)

