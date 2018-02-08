from __future__ import unicode_literals
import mechanicalsoup
import sys
import os
import multiprocessing
from multiprocessing import Pool
import re
import youtube_dl

def youtubes():
    url_list = []

    hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    url = 'https://www.youtube.com/watch?v=LYh3yDc4pCM&list=PLBSvleni5is2u66UMpc7nLOK6hh7w5OrQ'
    you = mechanicalsoup.Browser().get(url,headers=hdr)
    aa = you.soup.find_all('li',attrs={'class':'yt-uix-scroller-scroll-unit vve-check'})

    p = re.compile(".+(?=&index)")
    for i in aa :
        mv_list= i.find_all('a')[0].get('href')
        result=p.search(mv_list)
        url_list.append('http://www.youtube.com'+result.group())

    print(url_list)
    return url_list

def download_youtube(url_list):

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'melon_top100/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    folder = "melon_top100/"
    try:os.mkdir(folder)
    except:pass

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url_list])

for i in youtubes():
    try:
        download_youtube(i)
    except:pass


# if __name__=='__main__':
#     while True:
#         if sys.platform.startswith('win'):
#             multiprocessing.freeze_support()
#         pool = Pool(processes=2)
#         pool.map(download_youtube, youtubes())