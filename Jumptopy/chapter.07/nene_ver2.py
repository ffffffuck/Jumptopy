import urllib.request
from pandas import DataFrame
import os
result = []

import xml.etree.ElementTree as ET
response = urllib.request.urlopen('http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s'%(urllib.parse.quote('전체'),urllib.parse.quote('전체')))

html = response.read().decode('UTF-8')
root = ET.fromstring(html)

for element in root.findall('item'):
    store_name = element.findtext('aname1')
    store_sido = element.findtext('aname2')
    store_gungu = element.findtext('aname3')
    store_address = element.findtext('aname5')

    result.append([store_name]+[store_sido]+[store_gungu]+[store_address])

nene_table = DataFrame(result,columns=('store','sido','gungu','store_address'))


try:os.mkdir('C:\VI_Bigdata')
except:pass

record_limit=3
try:
    with open("순서.txt",'r') as infile:
        lines = list(infile)
    line = lines[-1:]
    for i in line:
        if (int(i)-1)%record_limit ==0:
            try:os.mkdir('C:\VI_Bigdata/Nene_Data[%d]' % (int(((int(i)-1)/record_limit)+1)))
            except:pass
        nene_table.to_csv(('C:\VI_Bigdata/Nene_Data[%d]/nene'%int(((int(i)-1)/record_limit)+1))  + '[' + str(int(i)) + ']' + '.csv', encoding="cp949", mode='w',index=True)
        with open("순서.txt", 'a') as infile:
            infile.write(str(int(i)+ 1)+'\n')
except:
    with open("순서.txt", 'w') as infile:
        infile.write(str(1)+'\n')
    with open("순서.txt", 'r') as infile:
        lines = list(infile)
    line = lines[-1:]
    for i in line:
        if (int(i)-1)%record_limit ==0:
            try:os.mkdir('C:\VI_Bigdata/Nene_Data[%d]' % (int(((int(i)-1)/record_limit)+1)))
            except:pass
        nene_table.to_csv(('C:\VI_Bigdata/Nene_Data[%d]/nene'%int(((int(i)-1)/record_limit)+1))  + '[' + str(int(i)) + ']' + '.csv', encoding="cp949", mode='w',index=True)
        with open("순서.txt", 'a') as infile:
            infile.write(str(int(i)+ 1)+'\n')


print("End")