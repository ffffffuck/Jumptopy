import urllib.request
import datetime
import time
import json

access_key="PUjPcu22uUk09DaNdDl6mkVTDoMG2QJWGhxwAeQVqybmmJfBDw%2F2kb0ziRxy0smbezEH77TXCv%2BfCYGP7OkDfw%3D%3D"

def get_request_url(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success"%datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL:%s"%(datetime.datetime.now(),url))

def realtime_weather_info():
    global time1

    end_point='http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData'

    times = datetime.datetime.now()
    time1 = times+datetime.timedelta(hours=-1)
    parameters = "?&_type=json&serviceKey="+access_key
    parameters += '&base_date=' + times.strftime("%Y%m%d")
    parameters += '&base_time='+ time1.strftime('%H')+'45'
    parameters += '&nx='+ str(89)
    parameters += '&ny='+ str(91)

    url=end_point+parameters
    print(url)
    retData = get_request_url(url)

    if(retData == None):return None
    else:return json.loads(retData)

def main():
    jsonResult = {}
    jsonData = realtime_weather_info()
    hours = time1 + datetime.timedelta(hours=1)
    after_hour = hours.strftime("%H") + '00'


    for i in jsonData['response']['body']['items']['item']:
        if after_hour == str(i['fcstTime']):
            if i['category'] =='LGT':
                jsonResult['낙뢰'] =i['fcstValue']
            elif i['category'] == 'PTY':
                jsonResult['강수형태'] = i['fcstValue']
            elif i['category'  ] == 'RN1':
                jsonResult['1시간강수량'] = i['fcstValue']
            elif i['category'] =='SKY':
                jsonResult['하늘상태'] = i['fcstValue']
            elif i['category'] == 'T1H':
                jsonResult['기온'] = i['fcstValue']

        jsonResult['예측시간'] = str(i['fcstTime'])[:2] +':'+str(i['fcstTime'])[2:]

    for i in list(jsonResult.items()):
        print(i[0]+' : '+str(i[1]))
    #
    with open('기상정보 업데이트_%s.json'%(datetime.datetime.now().strftime('%Y%m%d %H')),'w',encoding='utf8') as outfile:
        readable_result = json.dumps(jsonResult, indent=4, sort_keys=True,ensure_ascii=False)
        outfile.write(readable_result)
        print('\n저장되었습니다.')




if __name__ =='__main__':
    # while True:
        main()
        # time.sleep(10)
