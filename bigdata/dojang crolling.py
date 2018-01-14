from bs4 import BeautifulSoup
from pandas import DataFrame
import requests

maxpage=16
result=[]

for idx in range(1,maxpage+1):
    codoURL='http://codingdojang.com/list/%s?sort=level&sort_order=fw'%str(idx)
    html = requests.get(codoURL).text
    soup = BeautifulSoup(html,'lxml')
    print(codoURL)

    contents = soup.find_all('div',attrs={"class":"col-md-11 col-xs-10"})

    for i in contents:
        name=list(i.strings)[2]
        title=list(i.strings)[4]
        content = []
        answer = []
        uploader =[]
        profile = (i.find_all('span',attrs={"class":"question-profile"}))
        for j in profile:
            uploader.append(list(j.strings)[1])

        con = (i.find_all('a',attrs={"class":"question-subject"}))[0]
        inURL='http://codingdojang.com'+list(con.attrs.values())[0].replace('?answer_mode=hide','#answer-filter-area')
        html2 = requests.get(inURL).text
        soup2 = BeautifulSoup(html2,'lxml')
        in_content = soup2.find_all('div', attrs={'class':'col-md-11'})

        for i in in_content:
            pre_con = i.find_all('div',attrs={"class":"markdown_area answer-content"})
            for i in pre_con:
                content.append(''.join(list(i.strings)))
            pre_ans = i.find_all('div',attrs={"class":"answer-content markdown_area"})
            for i in pre_ans:
                answer.append(''.join(list(i.strings)))

        result.append([name]+[title] +[content[0]]+[uploader[0]]+[answer[0]])

    dojang_table = DataFrame(result,columns=('난이도','문제','문제내용','게시자','해답'))
    dojang_table.to_csv('코딩도장문제.csv', encoding='utf-8-sig',mode='w',index=False)

