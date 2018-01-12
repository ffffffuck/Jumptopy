import urllib.request
from bs4 import BeautifulSoup
from pandas import DataFrame

result = []
level = []
subject =[]
subject2 =[]
subject3 =[]
summary2=[]
summary = []
writer = []

html = urllib.request.urlopen('http://codingdojang.com/list/1?sort=level&sort_order=fw')
soup = BeautifulSoup(html,'html.parser')


levels = soup.find_all('span', attrs={'class':'pull-right label label-warning'})
subjects = soup.find_all('a',attrs={"class":"question-subject"})
summarys = soup.find_all('div', attrs={'class':'question-summary'})
writers = soup.find_all('span', attrs={"class":"question-profile"})
questions = soup.find_all('div',attrs={'class':'question-line'})

for i in levels:
    level.append(list(i.strings)[0])

for i in subjects:
    subject.append(list(i.strings)[0])

for i in subjects:
    summary2.append('http://codingdojang.com/'+list(i.attrs.values())[0])

for i in summarys:
    summary.append(list(i.strings)[0][33:-29])

for i in writers:
    writer.append(list(i.strings)[1])

for i in range(len(levels)):
    result.append([level[i]]+[subject[i]]+[subject3[i]]+[writer[i]])

for i in summary2:
    html2 = urllib.request.urlopen('%s'%i)
    soup2 = BeautifulSoup(html2,'html.parser')

    levels = soup2.find_all('div', attrs={'class':'markdown_area answer-content'})

    for i in levels:
        subject2.append(list(i.strings))

for i in subject2:
    subject3.append(' '.join(i))

print(len(subject3))
dojang_table = DataFrame(result,columns=('레벨','문제','내용','제출자'))
dojang_table.to_csv('코딩도장문제.csv', encoding="cp949",mode='w',index=False)