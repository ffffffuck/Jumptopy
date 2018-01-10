import urllib.request
from pandas import DataFrame
import os
import glob
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

n=0
try:
    with open("순서2.txt", 'r') as infile:
        lines = list(infile)
    line = lines[-1:]
    for i in line:
        try:os.mkdir('C:\VI_Bigdata/Nene_Data[%d]' % int(i))
        except:pass
        for j in range(100, len(nene_table), 100):
            nene_table[n:j].to_csv('C:\VI_Bigdata/Nene_data[%d]/'%int(i) + 'nene[' + str(n + 1) + '-' + str(int(j)) + ']' + '.csv',encoding="cp949", mode='w', index=True)
            n = int(j)
        nene_table[1101:].to_csv('C:\VI_Bigdata/Nene_data[%d]/'%int(i) +'nene[' + str(1101) + '-'']' + '.csv', encoding="cp949", mode='w', index=True)
        with open("순서2.txt", 'a') as infile:
            infile.write(str(int(i)+ 1)+'\n')
except:
    with open("순서2.txt", 'w') as infile:
        infile.write(str(1)+'\n')
    with open("순서2.txt", 'r') as infile:
        lines = list(infile)
    line = lines[-1:]
    for i in line:
        try:os.mkdir('C:\VI_Bigdata/Nene_Data[%d]' % int(i))
        except:pass
        for j in range(100, len(nene_table), 100):
            nene_table[n:j].to_csv(('C:\VI_Bigdata/Nene_data[%d]/'%int(i)) + 'nene[' + str(n + 1) + '-' + str(int(j)) + ']' + '.csv',encoding="cp949", mode='w', index=True)
            n = int(j)
        nene_table[1101:].to_csv(('C:\VI_Bigdata/Nene_data[%d]/'%int(i)) +'nene[' + str(1101) + '-'']' + '.csv', encoding="cp949", mode='w', index=True)
