import urllib.request
from bs4 import BeautifulSoup
from pandas import DataFrame

result = []

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html,'html.parser')


tags = soup.findAll('div', attrs={'class':'tit3'})
changes = soup.findAll('td', attrs={'class':'ac'})

ranks =[]
tags1 = []
change1 = []
for rank in range(1,len(tags)+1):
    ranks.append(rank)

for tag in tags:
    tr_tag = list(tag.strings)[1:-1][0]
    print(tr_tag)
    tags1.append(tr_tag)

for change in changes:
    tr_change = list(change.strings)[0]
    change1.append(tr_change)

for i in range(len(tags)):
    result.append([ranks[i]]+[tags1[i]+[change1[i]]])





# movie_table = DataFrame(result,columns=('순위','영화명','변동폭'))
# movie_table.to_csv("Movie_Rank.csv",encoding='cp949',mode='w',index=False)