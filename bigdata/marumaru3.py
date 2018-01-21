import requests
from requests import get
from bs4 import BeautifulSoup
import mechanicalsoup           #숨어있는 javascript 소스 처리
import os
import time
import sys
import multiprocessing
from multiprocessing import Pool


def rep(a):       #파일 이름 특수문자 처리
    rep=""
    b = ['\\','/',':','*','?','"','<','>','|',' ']
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

hdr1 ={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)'}
hdr2 ={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win32; x32)'}
hdr3 ={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64)'}
hdr4 ={'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
hdr5 ={'User_Agent': 'AppleWebKit/537.36 (KHTML, like Gecko)'}
hdr = 0

def get_link():       #첫페이지 파싱
    comic = []
    url_list =[]
    sub_list=[]

    URL='http://marumaru.in/c/1'
    html = requests.get(URL,headers=hdr1).text
    soup = BeautifulSoup(html, 'lxml')
    links = soup.find_all('li')

    try:
        for i in links:
            if list(i.a.attrs)[0] =='cid':
                    if rep(a) in rep(list(i.div.strings)[0]):
                        url_list.append(list(i.a.attrs.values())[1])
                        sub_list.append(list(i.div.strings)[0])
    except:pass

    for i in range(len(url_list)):
        print(str(i+1)+' : '+ sub_list[i])

    pick =input("받으실 만화의 번호를 선택하세요:")
    link = url_list[int(pick)-1]
    sub = sub_list[int(pick)-1]

    sel = input("1:전부받기 2:골라받기 3:이어받기 ")
    if sel =='1':
        print("전체를 다운로드 중입니다...")
    else : print("%s의 목록을 불러오는 중입니다.."%sub)

    URL2 ='http://marumaru.in/'+link       #링크들어가서 2번째 페이지 파싱
    html2 = requests.get(URL2,headers=hdr3).text
    soup2 = BeautifulSoup(html2, 'lxml')
    thumnail = soup2.find_all("div",attrs={'id':'vContent'})

    for i in thumnail:
        try:os.mkdir('마루마루')
        except:pass
        try:os.mkdir('마루마루/%s'%rep(sub))
        except:pass
        download(list(i.img.attrs.values())[0],'마루마루/%s/%s.gif'%(rep(sub),rep(sub)))     #썸네일 이미지저장
        aa = i.find_all("a",attrs={"target":"_blank"})    #링크들어가서 이미지 긁어오기

        for j in aa:
            comic.append(sub+list(j.attrs.values())[1]+'  '+list(j.strings)[0])

    if sel =='1':
        comic = comic
    elif sel =='2':
        for i in range(len(comic)):
            print(str(i+1)+" : "+comic[i][comic[i].index('  ')+2:])
        sel1 =input("원하시는 화를 선택하세요")
        print("다운로드 중입니다...")
        comic = [comic[int(sel1)-1]]

    elif sel =='3':
        for i in range(len(comic)):
            print(str(i+1)+" : "+comic[i][comic[i].index('  ')+2:])
        sel1 =input("몇화부터 이어받을지 선택하세요")
        print("다운로드 중입니다...")
        comic = comic[int(sel1)-1:]
    return comic

def get_image(comic):
    comic_URL = comic[comic.index('h'):comic.index('  ')]
    comic_name = comic[comic.index('  ')+2:]
    comic_dir_name = comic[:comic.index('h')]

    page = mechanicalsoup.Browser().get(comic_URL)
    comic_content = page.soup.find_all('img', attrs={"class": "lz-lazyload"})
    count = 0
    for j in comic_content:
        try:os.mkdir('마루마루/%s/%s' % (rep(comic_dir_name),rep(comic_name)))
        except:pass
        co = 'http://wasabisyrup.com' + list(j.attrs.values())[2]
        download(co, '마루마루/%s/%s/%s.jpg' % (rep(comic_dir_name), rep(comic_name), count))
        count+=1

if __name__=='__main__':
    # On Windows calling this function is necessary.
    if sys.platform.startswith('win'):
        multiprocessing.freeze_support()

    while True:
        print("<<< 마루마루 다운로더 ver0.1 >>>")
        a = input("제목을 입력하세요(0입력시 종료:")
        if a == '0':
            break
        else: pass
        print("검색중입니다...")

        start_time = time.time()

        pool = Pool(processes=16)
        pool.map(get_image, get_link())

        print("\n다운로드 완료")
        print("\n--- %s seconds ---\n" % (time.time() - start_time))