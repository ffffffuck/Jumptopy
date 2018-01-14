from pandas import DataFrame
from bs4 import BeautifulSoup
import requests

result=[]

maxpage=2
for idx in range(1,2):
    MelonURL='http://www.melon.com/chart/index.htm#params%%5Bidx%%5D=%s'%str(idx)
    html = requests.get(MelonURL).text
    soup = BeautifulSoup(html,'lxml')
    sing_song = soup.find_all('tr')

    for i in sing_song:
        a= list(i.strings)
        if a[2] !="\n":
            rank= a[2]+a[3]

            if a[27] =='19금':
                singer = a[33]
                song = a[29]
            else:
                song = a[27]
                singer = a[31]
            if a[8] =='순위 진입':
                rank_wrap = a[8]
                singer = a[29]
                song = a[25]
            else:
                if a[10] == '0':
                    rank_wrap =a[8]
                else:
                    rank_wrap =a[10]+a[8]

            result.append([rank]+[rank_wrap]+[song]+[singer])

melon_table = DataFrame(result,columns=('순위','순위변동','노래제목','가수'))
melon_table.to_csv('멜론실시간순위.csv',encoding='utf-8-sig',mode='w',index=False)