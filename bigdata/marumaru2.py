import requests
from requests import get
from bs4 import BeautifulSoup
from multiprocessing import Pool #숨어있는 javascript 소스 처리
import mechanicalsoup
import os

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
    sub=[]
    links=[]
    a = input("제목을 입력하세요")

    URL='http://marumaru.in/c/1'
    html = requests.get(URL,headers=hdr1).text
    soup = BeautifulSoup(html, 'lxml')
    link = soup.find_all('li')

    try:
        for i in link:
            if list(i.a.attrs)[0] =='cid':
                links.append(list(i.a.attrs.values())[1])
                sub.append(list(i.div.strings)[0])
    except:pass

    b = sub.index(a)
    URL2 ='http://marumaru.in/'+links[b]        #링크들어가서 2번째 페이지 파싱
    html2 = requests.get(URL2,headers=hdr2).text
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
            comic_URL=list(j.attrs.values())[1]
            comic_name=list(j.strings)[0]      #해당 화수

            count = 0
            page = mechanicalsoup.Browser().get(comic_URL)
            comic_content = page.soup.find_all('img', attrs={"class": "lz-lazyload"})
            for i in comic_content:
                try:os.mkdir('마루마루/%s/%s' % (rep(a), rep(comic_name)))
                except:pass
                co = 'http://wasabisyrup.com' + list(i.attrs.values())[2]
                download(co,'마루마루/%s/%s/%s.jpg'%(rep(a), rep(comic_name),count))
                count+=1


if __name__=='__main__':
    pool = Pool(processes=4)  # 4개의 프로세스를 사용합니다.
    pool.map(get_image())

