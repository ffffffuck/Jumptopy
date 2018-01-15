import requests
from requests import get
from bs4 import BeautifulSoup
import mechanicalsoup           #숨어있는 javascript 소스 처리
import os
# from multiprocessing import Pool


def rep(a):       #파일 이름 특수문자 처리
    rep=""
    for c in a:
        if c.isalnum():
            rep+=c
    return rep

def download(url, file_name):             # 파일 저장 함수
    with open(file_name, "wb") as file:
        response = get(url)
        file.write(response.content)

hdr1 ={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)'}
hdr2 ={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win32; x32)'}
hdr3 ={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64)'}
hdr = 0

def get_image(): #첫페이지 파싱
    comic_URL1=[]
    comic_URL2=[]
    comic_name1=[]
    comic_name2=[]

    a = input("제목을 입력하세요")
    sel = input("1:전부받기 2:골라받기 3:이어받기")

    if sel =='1':
        print("전체를 다운로드 중입니다...")
    else : print("목록을 불러오는 중입니다..")

    URL='http://marumaru.in/c/1'
    html = requests.get(URL,headers=hdr1).text
    soup = BeautifulSoup(html, 'lxml')
    link = soup.find_all('li')

    try:
        for i in link:
            if list(i.a.attrs)[0] =='cid':
                    if a == list(i.div.strings)[0]:
                        links = list(i.a.attrs.values())[1]
                        sub = list(i.div.strings)[0]
                        print(links)
                        print(sub)
    except:pass
    URL2 ='http://marumaru.in/'+links       #링크들어가서 2번째 페이지 파싱
    html2 = requests.get(URL2,headers=hdr3).text
    soup2 = BeautifulSoup(html2, 'lxml')

    thumnail = soup2.find_all("div",attrs={'id':'vContent'})
    for i in thumnail:
        try:os.mkdir('마루마루')
        except:pass
        try:os.mkdir('마루마루/%s'%rep(a))
        except:pass
        download(list(i.img.attrs.values())[0],'마루마루/%s/%s.gif'%(rep(a),rep(a)))     #썸네일 이미지저장

        aa = i.find_all("a",attrs={"target":"_blank"})      #링크들어가서 이미지 긁어오기
        for j in aa:
            comic_URL1.append(list(j.attrs.values())[1])
            comic_name1.append(list(j.strings)[0])

    if sel =='1':
        for i in range(len(comic_name1)):
            comic_URL2 = comic_URL1
            comic_name2 = comic_name1

    elif sel =='2':
        for i in range(len(comic_name1)):
            print(str(i+1)+":"+comic_name1[i])
        sel1 =input("원하시는 화를 선택하세요")
        print("다운로드 중입니다...")
        comic_URL2.append(comic_URL1[int(sel1)-1])
        comic_name2.append(comic_name1[int(sel1)-1])


    elif sel =='3':
        for i in range(len(comic_name1)):
            print(str(i+1)+":"+comic_name1[i])
        sel1 =input("몇화부터 이어받을지 선택하세요")
        print("다운로드 중입니다...")
        comic_URL2.append(comic_URL1[int(sel1)-1:])
        comic_name2.append(comic_name1[int(sel1)-1:])

    for i in range(len(comic_URL2)):   #이미지 긁어오기
        count = 0
        page = mechanicalsoup.Browser().get(comic_URL2[0])
        comic_content = page.soup.find_all('img', attrs={"class": "lz-lazyload"})
        for j in comic_content:
            try:os.mkdir('마루마루/%s/%s' % (rep(a),rep(comic_name2[i])))
            except:pass
            co = 'http://wasabisyrup.com' + list(j.attrs.values())[2]
            download(co, '마루마루/%s/%s/%s.jpg' % (rep(a), rep(comic_name2[i]), count))
            count += 1


get_image()
print("다운로드 끝")