import json

with open('jtbcnews_facebook_2018-01-24_2018-01-25.json', encoding='UTF8') as json_file:
    json_object = json.load(json_file)
    json_string = json.dumps(json_object)
    data = json.loads(json_string)

data['data'] = sorted(data['data'], key=lambda i: i['shares']['count'], reverse=True)

for i in range(len(data['data'])):
    try:
        print()
        print("제목: "+data['data'][i]['name'])
        print('링크: ' + data['data'][i]['link'])
        print("공유수: "+str(data['data'][i]['shares']['count']))
    except:pass
