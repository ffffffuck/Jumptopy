#히토미 크롤러
import os
import sys
import requests
import time
import multiprocessing
import zipfile
import shutil
from multiprocessing import Pool
from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver


hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

path = 'C:\\Python_exercise\\Jumptopy\\bigdata\\new\\chromedriver'


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

def zip(src_path, dest_file):
    with zipfile.ZipFile(dest_file, 'w') as zf:
        rootpath = src_path
        for (path, dir, files) in os.walk(src_path):
            for file in files:
                fullpath = os.path.join(path, file)
                relpath = os.path.relpath(fullpath, rootpath)
                zf.write(fullpath, relpath, zipfile.ZIP_DEFLATED)
        zf.close()


def get_link():
    m_list = []
    image_list = []
    print("<<< 히토미 크롤러 ver0.3 >>>")
    select = input("1:작가명으로 검색 2:품번으로 받기\n입력:")
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

        try:
            for i in range(1,int(index)+1):
                URL ='https://hitomi.la/artist/%s-korean-%s.html'%(artist_,str(i))
                html = requests.get(URL,headers=hdr).text
                soup = BeautifulSoup(html,'lxml')
                aa =soup.find_all('h1')

                for i in aa:
                    sub = i.text
                    link = list(i.a.attrs.values())[0]
                    link= link.replace('galleries','reader')
                    m_list.append('https://hitomi.la'+link+'  '+rep(sub))
        except:
            print("정확한 작가명을 입력하세요.")
            return get_link()

        for i in range(len(m_list)):
            print(str(i+1)+' : '+m_list[i][m_list[i].index('  ')+2:])
        pick = input("받으실 쩡의 번호를 입력하세요:")

        link_name = m_list[int(pick)-1]
        image_link = link_name[:link_name.index('  ')]
        print('다운로드 준비중입니다...')


        if getattr(sys,'frozen',False):
            # executed as a bundled exe, the driver is in the extracted folder
            chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
            driver = webdriver.Chrome(chromedriver_path, chrome_options=options)
        else:driver = webdriver.Chrome(path, chrome_options=options)

        driver.get(image_link)
        driver.implicitly_wait(3)
        html3 = driver.page_source
        soup3 = BeautifulSoup(html3, 'lxml')

        manga_index_list = []
        manga_url = ''
        aa = soup3.find_all('div', attrs={'class': 'img-url'})
        bb = soup3.find_all('img', attrs={'onclick': 'nextPanel()'})
        cc = soup3.find_all('title')
        c = list(cc[0].strings)[0].split('|')
        manga_name = c[0][:-1]  # +c[1]

        for i in aa:
            manga_index_list.append(list(i.strings)[0].split('/')[-1])
        for i in bb:
            manga_url = list(i.attrs.values())[0]
            a = manga_url.split('/')
            manga_url = '%s/%s/%s/%s/%s/' % (a[0],a[1],a[2],a[3],a[4])

        driver.quit()

        for i in range(len(manga_index_list)):
            image_list.append('https:' + manga_url + manga_index_list[i] + '  ' + rep(manga_name)+'   '+artist)

        return image_list


    elif select == '2':
        link = input("품번을 입력하세요:")
        print("다운로드 준비중입니다..")
        artist = ''
        p_link = 'https://hitomi.la/galleries/%s.html#1-'% link
        html2 = requests.get(p_link).text
        soup2 = BeautifulSoup(html2, 'lxml')
        i_link = soup2.find_all('ul',attrs={'class':'comma-list'})
        for i in i_link:
            artist+=list(i.strings)[1]
            break

        url = 'https://hitomi.la/reader/%s.html#1'% link

        if getattr(sys,'frozen',False):
            # executed as a bundled exe, the driver is in the extracted folder
            chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
            driver = webdriver.Chrome(chromedriver_path, chrome_options=options)
        else:driver = webdriver.Chrome(path, chrome_options=options)

        driver.get(url)
        driver.implicitly_wait(3)
        html3 = driver.page_source
        soup3 = BeautifulSoup(html3, 'lxml')

        manga_index_list = []
        manga_url = ''
        aa = soup3.find_all('div', attrs={'class': 'img-url'})
        bb = soup3.find_all('img', attrs={'onclick': 'nextPanel()'})
        cc = soup3.find_all('title')
        c = list(cc[0].strings)[0].split('|')
        manga_name = c[0][:-1]

        for i in aa:
            manga_index_list.append(list(i.strings)[0].split('/')[-1])
        for i in bb:
            manga_url = list(i.attrs.values())[0]
            a = manga_url.split('/')
            manga_url = '%s/%s/%s/%s/%s/' % (a[0], a[1], a[2], a[3], a[4])

        for i in range(len(manga_index_list)):
            image_list.append('https:' + manga_url + manga_index_list[i] + '  ' + rep(manga_name)+'   '+artist)

        return image_list
    else:
        print("제대로 입력하세요:")
        return get_link()

def get_image(image_list):

    i_link = image_list[:image_list.index('  ')]
    i_dir_name = image_list[image_list.index(' ')+2:image_list.index('   ')]
    i_artist = image_list[image_list.index('   ')+3:]
    i_name = i_link.split('/')[-1]

    try:os.mkdir("c:/hitomi")
    except:pass
    try:os.mkdir("c:/hitomi/[%s]%s"%(i_artist,i_dir_name))
    except:pass
    print('%s폴더에 %s를 받는중...'%(i_dir_name,i_name))
    download(i_link, "c:/hitomi/[%s]%s/%s"%(i_artist,i_dir_name,str(i_name)))
    try: os.mkdir("hitomi")
    except:pass
    t = i_artist, i_dir_name
    return t

if __name__=='__main__':
    # On Windows calling this function is necessary.
    while True:
        if sys.platform.startswith('win'):
            multiprocessing.freeze_support()

        start_time = time.time()

        pool = Pool(processes=16)
        try:
            t = pool.map(get_image, get_link())[0]
        except:
            print("정확한 품번을 입력하세요.")
            continue

        i_artist = t[0]
        i_dir_name = t[1]
        zip("c:/hitomi/[%s]%s/" % (i_artist, i_dir_name), 'c:/hitomi/[%s]%s.zip' % (i_artist, i_dir_name))
        shutil.move('c://hitomi//[%s]%s.zip'%(i_artist,i_dir_name),'hitomi')
        shutil.rmtree('c://hitomi')
        print("\n다운로드 완료")
        #
        print("\n--- %s seconds ---\n" % (time.time() - start_time))