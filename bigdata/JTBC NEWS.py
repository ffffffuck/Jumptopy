import urllib.request
import requests
import json


app_id = '192646954653095'
app_secret = 'fe1057533c45163533e85716ebf75348'
page_name = 'jtbcnews'

def get_jtbc_news_page_ID():

    access_token = app_id +'|'+app_secret

    base = "https://graph.facebook.com/v2.8"
    node = '/'+page_name
    parameters="/?access_token=%s"%access_token

    url = base+node+parameters

    req = urllib.request.Request(url)
    print("url:"+url)

    try:
        response = urllib.request.urlopen(req)

        if response.getcode() == 200:
            data =json.loads(response.read().decode('utf-8'))
            page_id = data['id']
            print("%s Facebook Numeric ID: %s"%(page_name,page_id))

    except Exception as e:
        print(e)

    return page_id


page_id = get_jtbc_news_page_ID()
from_date = "2018-01-24"
to_date ='2018-01-25'
num_statuses = '100'
access_token = app_id+'|'+ app_secret

base = "https://graph.facebook.com/v2.8"
node = '/%s/posts'%page_id
fields = "/?fields=id,message,link,name,type,shares,reactions,"+\
    "created_time,comments.limit(0).smmary(true)"+\
    ".limit(0).summary(true)"
duration = "&since=%s&until=%s"%(from_date, to_date)
parameters = "&limit=%s&access_token=%s"%(num_statuses,access_token)
url = base+node+fields+duration+parameters
print("The request url for jtbcv news: "+url)
req = urllib.request.Request(url)

try:
    response = urllib.request.urlopen(req)
    if response.getcode() == 200:
        data = json.loads(response.read().decode('utf-8'))
        # print(data)

        with open('%s_facebook_%s_%s.json'%(page_name,from_date,to_date),'w',encoding='utf-8')as outfile:
            readable_result = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(readable_result)


except Exception as e :
    print(e)