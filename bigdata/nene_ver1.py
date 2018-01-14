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

try:os.mkdir('C:\V1_Bigdata')
except:pass

try:
    with open("index.txt",'r') as infile:
        line = infile.readline()
except:
    with open("index.txt", 'w') as infile:
        infile.write(str(1))
    with open("index.txt",'r') as infile:
        line = infile.readline()

nene_table.to_csv('C:\V1_Bigdata/nene'+'['+str(int(line))+']'+'.csv',encoding="cp949", mode='w',index=True)
with open("index.txt", 'w') as infile:
        infile.write(str(int(line)+ 1))

print("End")