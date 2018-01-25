import json

with open('이명박_naver_news.json', encoding='UTF8') as json_file:
    json_object = json.load(json_file)
    json_string = json.dumps(json_object)
    data = json.loads(json_string)


link = []
for i in range(len(data)):
    if len(data[i]['org_link'].split('/')) > 2 :
        link.append(data[i]['org_link'].split('/')[2])

link = sorted(link)

index = []
link2 = []

for i in range(len(link)-1):
    if link[i] != link[i+1]:
        link2.append(link[i]+'  '+str(link.count(link[i])))
link2.append(link[-1]+'  '+str(link.count(link[-1])))

for i in link2:
    print(i[i.index('  ')+2:])
