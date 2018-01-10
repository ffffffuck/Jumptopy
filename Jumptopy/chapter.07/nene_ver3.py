import urllib.request
from pandas import DataFrame
import os
import time

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
    with open("날짜.txt", 'r') as infile:
        lines = list(infile)
    line = lines[-1:]
    pre_line = lines[-2:-1]
    for i in line:
        s_time = i[14:16] #분단위
    for j in pre_line:
        pre_time = j[14:16]
    if int(s_time) != int(pre_time):
        os.mkdir('C:\VI_Bigdata/Nene_%s_Data' % s_time)
    nene_table.to_csv(('C:\VI_Bigdata/Nene_%s_Data/' % s_time) + 'nene_' + time.strftime('%Y-%m-%d %H_%M_%S',time.localtime(time.time())) + '.csv',encoding="cp949", mode='w', index=True)
    with open("날짜.txt", 'a') as infile:
        infile.write(str(time.strftime('%Y-%m-%d %H_%M_%S', time.localtime(time.time()))) + '\n')
except:
    with open("날짜.txt", 'w') as infile:
        infile.write(str(time.strftime('%Y-%m-%d %H_%M_%S', time.localtime(time.time())))+'\n')
    with open("날짜.txt", 'r') as infile:
        lines = list(infile)
    line = lines[-1:]
    for i in line:
        s_time=i[14:16]
        try:os.mkdir('C:\VI_Bigdata/Nene_%s_Data' %s_time)
        except:pass
    nene_table.to_csv(('C:\VI_Bigdata/Nene_%s_Data/' %s_time) + 'nene_' + time.strftime('%Y-%m-%d %H_%M_%S',time.localtime(time.time())) + '.csv',encoding="cp949", mode='w', index=True)
    with open("날짜.txt", 'a') as infile:
        infile.write(str(time.strftime('%Y-%m-%d %H_%M_%S', time.localtime(time.time()))) + '\n')


print("End")