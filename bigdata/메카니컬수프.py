from bs4 import BeautifulSoup
import mechanicalsoup
import requests



hdr2 ={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win32; x32)'}

br = mechanicalsoup.Browser()
hurl = "http://wasabisyrup.com/archives/M-5AUJJkxt8"
page = br.get(hurl)

link = page.soup.find_all('img',attrs={"class":"lz-lazyload"})

for i in link:
    print(list(i.attrs.values())[2])

