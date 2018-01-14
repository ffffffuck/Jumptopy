import urllib.request
from bs4 import BeautifulSoup
import os
from selenium import webdriver

URL=input("갤러리 주소를 입력하세요")
path = 'C:\\Users\lee\\Downloads\\chromedriver'
driver = webdriver.Chrome(path)
driver.get(URL)
html = driver.page_source
soup = BeautifulSoup(html, 'lxml')


imagelist = soup.find_all('a',attrs={"class":"icon_pic_n"})

for i in imagelist:
    a= list(i.attrs.values())[0]
    inURL='http://gall.dcinside.com'+a
    driver.get(inURL)
    html2 = driver.page_source
    soup2 = BeautifulSoup(html2,'lxml')
    image_scorll = soup2.find_all("li",attrs={'class':'icon_pic'})
    for i in image_scorll:
        b= (list(i.a.attrs.values())[0])
        b=b.replace('download.php','viewimage.php')
        image_name=list(i.strings)[0]
        try:os.mkdir("C:/Users/lee/Desktop/zzal")
        except:pass
        urllib.request.urlretrieve(b,'C:/Users/lee/Desktop/zzal/'+image_name)




 # driver = webdriver.PhantomJS('C:/Users/lee/Downloads/phantomjs-2.1.1-windows/bin/phantomjs')
# driver.implicitly_wait(3)

# driver.get('https://nid.naver.com/nidlogin.login')
#
# driver.find_element_by_name('id').send_keys('chshone')
# driver.find_element_by_name('pw').send_keys('7989adsd')
# driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
# notices = soup.select('div.p_inr > div.p_info > a > span')
#
# for n in notices:
#     print(n.text.strip())

