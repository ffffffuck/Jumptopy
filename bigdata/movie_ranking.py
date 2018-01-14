import urllib.request
from bs4 import BeautifulSoup
from pandas import DataFrame

result = []
tags1 = []
change1 = []
updown1 = []
html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html,'html.parser')

tags = soup.find_all('div', attrs={'class':'tit3'})
changes = soup.find_all('td', attrs={'class':'range ac'})
updowns = soup.find_all('img', attrs={'class':'arrow'})

for tag in tags:
    tr_tag = list(tag.strings)[1]
    tags1.append(tr_tag)

for change in changes:
    tr_change = list(change.strings)[0]
    change1.append(tr_change)

for updown in updowns:
    a = list(updown.attrs.values())[1]
    if a == 'na':
        updown1.append('...')
    elif a == 'up':
        updown1.append('↑')
    elif a =='down':
        updown1.append('↓')


for i in range(len(tags)):
    result.append([i+1]+[tags1[i]]+[updown1[i]+change1[i]])

movie_table = DataFrame(result,columns=('순위','영화명','변동폭'))
movie_table.to_csv("Movie_Rank.csv",encoding='cp949',mode='w',index=False)