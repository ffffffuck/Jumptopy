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

try:os.mkdir('C:\V4_Bigdata')
except:pass

div_range = 100
n=0

try:
    with open("index3.txt", 'r') as infile:
        line = infile.readline()
except:
    with open("index3.txt", 'w') as infile:
        infile.write(str(1))
    with open("index3.txt", 'r') as infile:
        line = infile.readline()

try:os.mkdir('C:\V4_Bigdata/Nene_Data[%d]' % int(line))
except:pass
for i in range(div_range,len(nene_table),div_range):
    nene_table[n:i].to_csv(('C:\V4_Bigdata/Nene_data[%d]/'%int(line))+'nene['+str(n+1)+'-'+str(int(i))+']'+'.csv',encoding="cp949",mode='w',index=True)
    n = int(i)
nene_table[i:].to_csv(('C:\V4_Bigdata/Nene_data[%d]/'%int(line))+'nene['+str(i+1)+'-'+'end]'+'.csv',encoding="cp949",mode='w',index=True)
with open("index3.txt", 'w') as infile:
        infile.write(str(int(line)+ 1))

print("End")
