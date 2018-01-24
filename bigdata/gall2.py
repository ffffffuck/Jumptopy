import requests
import urllib.request
from requests import get
import random
import time
from bs4 import BeautifulSoup
import os
from multiprocessing import Pool
import sys

hdr1 ={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)'}
hdr2 ={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win32; x32)'}
hdr3 ={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64)'}
hdr = 0


def rep(a):       #파일 이름 특수문자 처리
    rep=""
    b = ['\\','/',':','*','?','"','<','>','|',' ','\n','\t']
    for c in a:
        if c in b :
            c=''
            rep+=c
        else: rep+=c
    return rep

def download(url, file_name):             # 파일 저장 함수
    with open(file_name, "wb") as file:
        response = get(url)
        file.write(response.content)


def get_link():
    maxpage = 10
    URL = input("갤러리 주소를 입력하세요:")
    a = input("1. 일반 2. 개념글")
    imagelists=[]
    for idx in range(1,maxpage+1):
        if a == '1' :
            URL = URL+'&page=%s'%str(idx)
            icon = "icon_pic_n"
        elif a == '2':
            URL = URL +'&page=%s&exception_mode=recommend'%str(idx)
            icon = 'icon_pic_b'
        html = requests.get(URL,headers=hdr1).text
        soup = BeautifulSoup(html, 'lxml')
        imagelist = soup.find_all('a',attrs={"class":icon})

        g_time = time.strftime("%Y%m%d", time.localtime(time.time()))

        for i in imagelist:
            a= list(imagelist.attrs.values())[0]
            inURL='http://gall.dcinside.com'+a
            if random.randint(1,4) ==1:hdr=hdr1
            elif random.randint(1,4) ==2:hdr=hdr2
            else: hdr=hdr3
            html2 = requests.get(inURL,headers=hdr).text
            soup2 = BeautifulSoup(html2,'lxml')

            tit = soup2.find_all('a',attrs={'class':'fc_5b'})
            sub = list(tit[0].strings)[1]+' '+list(tit[0].strings)[2]
            image_scorll = soup2.find_all("li",attrs={'class':'icon_pic'})

            for i in image_scorll:
                b= (list(i.a.attrs.values())[0])
                b=b.replace('download.php','viewimage.php')
                image_name=list(i.strings)[0]
                if os.path.isdir("zzal"):
                    pass
                else: os.mkdir("zzal")
                if os.path.isdir("zzal/"+g_time+'_'+rep(sub)):
                    pass
                else:os.mkdir("zzal/"+g_time+'_'+rep(sub))
                urllib.request.urlretrieve(b,'zzal/'+g_time+'_'+rep(sub)+'/'+image_name)
                print('[%s] 받고 있습니다..'%image_name)




if __name__=='__main__':
    start_time = time.time()
    # for i in get_link():
    #     get_image(i)
    pool = Pool(processes=4)
    pool.map(get_image, get_link())

    print("--- %s seconds ---" % (time.time() - start_time))
    print("다운로드 끝")

