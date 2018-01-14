import requests
from requests import get
from bs4 import BeautifulSoup
from multiprocessing import Pool
import mechanicalsoup
import os

def download(url, file_name):
    with open(file_name, "wb") as file:
        response = get(url)
        file.write(response.content)

hdr1 ={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)'}
hdr2 ={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win32; x32)'}
hdr3 ={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64)'}
hdr = 0

def get_image():
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
    URL2 ='http://marumaru.in/'+links[b]
    html2 = requests.get(URL2,headers=hdr2).text
    soup2 = BeautifulSoup(html2, 'lxml')

    thumnail = soup2.find_all("div",attrs={'id':'vContent'})
    for i in thumnail:
        try:os.mkdir('마루마루')
        except:pass
        try:os.mkdir('마루마루/%s'%a)
        except:pass
        download(list(i.img.attrs.values())[0],'마루마루/%s/%s.gif'%(a,a))

        aa = i.find_all("a",attrs={"target":"_blank"})
        for j in aa:
            comic_URL=list(j.attrs.values())[1]
            comic_name=list(j.strings)[0]
            page = mechanicalsoup.Browser().get(comic_URL)

            count = 0
            comic_content = page.soup.find_all('img', attrs={"class": "lz-lazyload"})
            for i in comic_content:
                try:os.mkdir('마루마루/%s/%s' % (a, comic_name))
                except:pass
                co = 'http://wasabisyrup.com' + list(i.attrs.values())[2]
                download(co,'마루마루/%s/%s/%s.jpg'%(a, comic_name,count))
                count+=1


if __name__=='__main__':
    pool = Pool(processes=4)  # 4개의 프로세스를 사용합니다.
    pool.map(get_image())

