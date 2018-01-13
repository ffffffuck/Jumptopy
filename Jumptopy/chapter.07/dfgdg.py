import urllib.request
from bs4 import BeautifulSoup
from pandas import DataFrame
import os

#-*- coding: utf-8 -*-

maxpage=16
result=[]

for idx in range(5,6):
    codoURL='http://codingdojang.com/list/%s?sort=level&sort_order=fw'%str(idx)
    html = urllib.request.urlopen(codoURL)
    soup = BeautifulSoup(html.read(),'lxml')
    print(codoURL)

    contents = soup.find_all('div',attrs={"class":"col-md-11 col-xs-10"})

    for i in contents:
        name=list(i.strings)[2]
        title=list(i.strings)[4]
        uploader=list(i.strings)[-8]
        content = []
        answer = []

        con = i.find_all('a',attrs={"class":"question-subject"})
        aa=list(con[0].attrs.values())[0].replace('?answer_mode=hide','#answer-filter-area')
        html2 = urllib.request.urlopen('http://codingdojang.com'+aa)
        soup2 = BeautifulSoup(html2.read(),'lxml')
        in_content = soup2.find_all('div', attrs={'class': 'col-md-11'})

        for i in in_content:
            pre_con = i.find_all('div',attrs={"class":"markdown_area answer-content"})
            for i in pre_con:
                content.append(''.join(list(i.strings)))
            pre_ans = i.find_all('div',attrs={"class":"answer-content markdown_area"})
            for i in pre_ans:
                answer.append(''.join(list(i.strings)))


        result.append([name] + [title] +[content[0]]+[uploader]+[answer[0]])
dojang_table = DataFrame(result,columns=('난이도','문제','문제내용','게시자','해답'))
dojang_table.to_csv('코딩도장문제1.csv', encoding='cp949',mode='w',index=False)

# infile = open('코딩도장문제1.csv','r', encoding='utf-8')
# outfile = open('코딩도장문제.csv','w', encoding='cp949')
#
# for line in infile:
#     line = line.replace('\u2217', ' ')
#     line = line.replace('\u22ef', ' ')
#     line = line.replace('\u2266', ' ')
#     line = line.replace('\xa0', ' ')
#     line = line.replace('\xec', ' ')
#     line = line.replace('\x8c', ' ')
#     line = line.replace('\x8d', ' ')
#     line = line.replace('\x9d', ' ')
#     line = line.replace('\x9e', ' ')
#     line = line.replace('\x9c', ' ')
#     line = line.replace('\x82', ' ')
#     line = line.replace('\xeb', ' ')
#     line = line.replace('\x80', ' ')
#     line = line.replace('\x97', ' ')
#     line = line.replace('\x98', ' ')
#     line = line.replace('\xea', ' ')
#     line = line.replace('\xa5', ' ')
#     outfile.write(line)

# infile.close()
# outfile.close()

# os.remove("코딩도장문제1.csv")

