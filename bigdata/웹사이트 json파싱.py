import json
import requests



url = 'https://ltn.hitomi.la/galleries1.json'

rrr = requests.get(url).text



aa= json.loads(rrr)

with open("hitomi1.json", 'w', encoding='utf8') as outfile:
    readable_result = json.dumps(aa, indent=4, sort_keys=True, ensure_ascii=False)
    outfile.write(readable_result)
#
# print(data)