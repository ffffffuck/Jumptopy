import requests
import csv
from bs4 import BeautifulSoup
from pandas import DataFrame
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random


hdr1 ={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)'}

result =[]
result1 = []
maxpage = 28

for i in range(1,maxpage+1):
    URL = 'http://www.gamtan.co.kr/page/store/shop.php?page=%s&catetype=&key=&keyword=&pstate=&gubun=&code='%str(i)
    page = requests.get(URL,headers=hdr1).text

    soup= BeautifulSoup(page,'lxml')
    gamtan = soup.find_all('tr')

    for i in gamtan[1:]:
        location = list(i.strings)[1]
        jumpo = list(i.strings)[3]
        adress = list(i.strings)[5]

        result.append([location]+[jumpo]+[adress])
        result1.append(location+jumpo+adress)



ae = pd.DataFrame(result1,np.random.randn(407,3),columns=("지역","지점수","비율"))
gamtan_table = DataFrame(result, columns=("지역", "지점수", "비율"))
gamtan_table.to_csv("gamtan_수집데이터.csv", encoding='cp949', mode='w', index=False)

http://ourcstory.tistory.com/145
print(ae)