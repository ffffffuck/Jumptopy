#히토미 크롤러
import os
import sys
import requests
import time
import multiprocessing
import urllib.request
from multiprocessing import Pool
from requests import get
from bs4 import BeautifulSoup

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

hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def get_link():
    m_list = []
    image_list = []
    select = input("1:작가명으로 검색 2:품번으로")
    if select == '1':
        artist = input("작가명을 입력하세요:")
        artist_=''
        for i in artist :
            if i == ' ':
                i='%20'
                artist_+=i
            else:artist_+=i

        index=''
        print("작품 목록 로딩중...")
        URL ='https://hitomi.la/artist/%s-korean-1.html'%(artist_)
        html = requests.get(URL,headers=hdr).text
        soup = BeautifulSoup(html, 'lxml')
        aa = soup.find_all('script')
        for i in aa:
            try:
                if 'paging' in list(i.strings)[0]:
                    a = list(i.strings)[0].split(',')[-1]
                    index+=a[1:a.index(')')]
            except:pass

        for i in range(1,int(index)+1):
            URL ='https://hitomi.la/artist/%s-korean-%s.html'%(artist_,str(i))
            html = requests.get(URL).text
            soup = BeautifulSoup(html,'lxml')
            aa =soup.find_all('h1')

            for i in aa:
                sub = list(i.strings)[0]
                link = list(i.a.attrs.values())[0]
                link= link.replace('galleries','reader')
                m_list.append('https://hitomi.la'+link+'  '+rep(sub))


        for i in range(len(m_list)):
            print(str(i+1)+' : '+m_list[i][m_list[i].index('  ')+2:])
        pick = input("받으실 쩡의 번호를 입력하세요:")
        link_name = m_list[int(pick)-1]
        image_link = link_name[:link_name.index('  ')]
        image_name = link_name[link_name.index('  ')+2:]

        html2 = requests.get(image_link).text
        soup2 = BeautifulSoup(html2, 'lxml')
        down_link = soup2.find_all('div',attrs={'class':'img-url'})

        for i in down_link:
            image ='https://0a.hitomi.la'+list(i.strings)[0][13:]
            image_list.append(image+'  '+image_name+'   '+artist)
        return image_list


    elif select == '2':
        link = input("품번을 입력하세요:")
        artist = ''
        title = ''
        p_link = 'https://hitomi.la/galleries/%s.html#1-'% link
        html2 = requests.get(p_link).text
        soup2 = BeautifulSoup(html2, 'lxml')
        i_link = soup2.find_all('ul',attrs={'class':'comma-list'})
        for i in i_link:
            artist+=list(i.strings)[1]
            break
        p_link2 = 'https://hitomi.la/reader/%s.html#1-'% link
        html3 = requests.get(p_link2).text
        soup3 = BeautifulSoup(html3, 'lxml')
        down_link = soup3.find_all('div', attrs={'class': 'img-url'})
        aa = soup3.find_all('title')
        for i in aa:
            title+=list(i.strings)[0][:-11]
        for i in down_link:
            image = 'https://0a.hitomi.la'+list(i.strings)[0][13:]
            image_list.append(image + '  ' + rep(title) + '   ' + artist)
        return image_list


def get_image(image_list):
    i_link = image_list[:image_list.index('  ')]
    i_dir_name = image_list[image_list.index(' ')+2:image_list.index('   ')]
    i_artist = image_list[image_list.index('   ')+3:]
    i_name = i_link.split('/')[-1]
    if os.path.isdir("히토미"):pass
    else: os.mkdir("히토미")
    if os.path.isdir("히토미/[%s]%s"%(i_artist,i_dir_name)):pass
    else:os.mkdir("히토미/[%s]%s"%(i_artist,i_dir_name))
    print('%s폴더에 %s를 받는중...'%(i_dir_name,i_name))
    urllib.request.urlretrieve(i_link, "히토미/[%s]%s/%s"%(i_artist,i_dir_name,str(i_name)))


if __name__=='__main__':
    # On Windows calling this function is necessary.
    while True:
        if sys.platform.startswith('win'):
            multiprocessing.freeze_support()

        start_time = time.time()

        pool = Pool(processes=4)
        pool.map(get_image, get_link())
        print("\n다운로드 완료")

        print("\n--- %s seconds ---\n" % (time.time() - start_time))