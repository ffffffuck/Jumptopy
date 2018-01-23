from selenium import webdriver
from bs4 import BeautifulSoup
import mechanicalsoup

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

path ='C:\\Users\\lee\Downloads\\chromedriver'

url ='https://hitomi.la/reader/1174134.html#1'


driver = webdriver.Chrome(path, chrome_options=options)
driver.get(url)
driver.implicitly_wait(3)
html3 = driver.page_source
soup3 = BeautifulSoup(html3, 'lxml')

manga_index_list = []
manga = []
manga_url = ''
aa = soup3.find_all('div',attrs={'class':'img-url'})
bb = soup3.find_all('img',attrs={'onclick':'nextPanel()'})
cc = soup3.find_all('title')
c= list(cc[0].strings)[0].split('|')
manga_name=c[0][:-1]#+c[1]


for i in aa:
    manga_index_list.append(list(i.strings)[0].split('/')[-1])
for i in bb:
    manga_url=list(i.attrs.values())[0]
    a = manga_url.split('/')
    manga_url= '%s/%s/%s/%s/%s/'%(a[0],a[1],a[2],a[3],a[4])

for i in range(len(manga_index_list)):
    manga.append('https:'+manga_url+manga_index_list[i]+'  '+manga_name)

print(manga)


