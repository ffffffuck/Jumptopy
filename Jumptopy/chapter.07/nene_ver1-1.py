import urllib.request
from pandas import DataFrame
import glob
import os

result = []

import xml.etree.ElementTree as ET

response = urllib.request.urlopen(
    'http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s' % (
    urllib.parse.quote('전체'), urllib.parse.quote('전체')))

html = response.read().decode('UTF-8')
root = ET.fromstring(html)

for element in root.findall('item'):
    store_name = element.findtext('aname1')
    store_sido = element.findtext('aname2')
    store_gungu = element.findtext('aname3')
    store_address = element.findtext('aname5')

    result.append([store_name] + [store_sido] + [store_gungu] + [store_address])

nene_table = DataFrame(result, columns=('store', 'sido', 'gungu', 'store_address'))


try:os.mkdir('C:\VI_Bigdata')
except:pass
dir_list = glob.glob('C:\VI_Bigdata/nene*')
if len(dir_list) > 1:pass
else:nene_table.to_csv('C:\VI_Bigdata/nene'+'['+str(1)+']'+'.csv',encoding="cp949",mode='w',index=True)
nene0 = dir_list[-1:]
for nene in nene0:
    number = nene[nene.index('[')+1:nene.index(']')]
    nene_table.to_csv('C:\VI_Bigdata/nene'+'['+str(int(number)+1)+']'+'.csv',encoding="cp949",mode='w',index=True)

print("End")