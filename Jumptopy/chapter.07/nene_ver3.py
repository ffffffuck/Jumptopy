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


try:os.mkdir('C:\V3_Bigdata')
except:pass

line = time.strftime('%Y-%m-%d %H_%M_%S', time.localtime(time.time()))
s_time=line[14:16] #분단위
try:os.mkdir('C:\V3_Bigdata/Nene_%s_Data' %s_time)
except:pass
nene_table.to_csv(('C:\V3_Bigdata/Nene_%s_Data/' %s_time)+'nene_'+line+'.csv',encoding="cp949", mode='w', index=True)

print("End")