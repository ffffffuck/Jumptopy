import urllib.request
import requests
import random
from bs4 import BeautifulSoup
import os

hdr1 ={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)'}
hdr2 ={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win32; x32)'}
hdr3 ={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64)'}
hdr = 0

maxpage=10
URL=input("갤러리 주소를 입력하세요:")
for idx in range(1,maxpage+1):
    URL = URL+'&page=%s'%str(idx)
    html = requests.get(URL,headers=hdr1).text
    soup = BeautifulSoup(html, 'lxml')
    imagelist = soup.find_all('a',attrs={"class":"icon_pic_n"})
    gall_subject = soup.find_all('meta',attrs={"name":"title"})
    print('%s페이지에서 받는중..'%idx)

    sub= list(gall_subject[0].attrs.values())[1]

    for i in imagelist:
        a= list(i.attrs.values())[0]
        inURL='http://gall.dcinside.com'+a
        if random.randint(1,4) ==1:hdr=hdr1
        elif random.randint(1,4) ==2:hdr=hdr2
        else: hdr=hdr3
        html2 = requests.get(inURL,headers=hdr).text
        soup2 = BeautifulSoup(html2,'lxml')
        image_scorll = soup2.find_all("li",attrs={'class':'icon_pic'})

        for i in image_scorll:
            b= (list(i.a.attrs.values())[0])
            b=b.replace('download.php','viewimage.php')
            image_name=list(i.strings)[0]
            try:os.mkdir("zzal")
            except:pass
            try:os.mkdir("zzal/"+sub)
            except:pass
            urllib.request.urlretrieve(b,'zzal/'+sub+'/'+image_name)
            print('[%s] 받고 있습니다..'%image_name)


