import urllib.request
import threading
import datetime
import time
import json

g_Radiator = False
g_Gas_Valve = False
g_Balcony_Windows = False
g_Door = False
g_AI_mode = False


access_key="PUjPcu22uUk09DaNdDl6mkVTDoMG2QJWGhxwAeQVqybmmJfBDw%2F2kb0ziRxy0smbezEH77TXCv%2BfCYGP7OkDfw%3D%3D"

def get_request_url(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            # print("\n[%s] Url Request Success"%datetime.datetime.now())
            return response.read().decode('utf-8')

    except Exception as e:
        pass
        # print(e)
        # print("\n[%s] Error for URL:%s"%(datetime.datetime.now(),url))

def realtime_weather_info():
    global time1

    end_point='http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData'

    times = datetime.datetime.now()
    if int(times.strftime('%M')) < 45:
        time1 = times+datetime.timedelta(minutes=-30)
    elif int(times.strftime('%M')) >= 45:
        time1 = times
    parameters = "?&_type=json&serviceKey="+access_key
    parameters += '&base_date=' + times.strftime("%Y%m%d")
    parameters += '&base_time='+ time1.strftime('%H%M')
    parameters += '&nx='+ str(89)
    parameters += '&ny='+ str(91)

    url=end_point+parameters
    retData = get_request_url(url)

    if(retData == None):return None
    else:return json.loads(retData)

def main():
    global g_Balcony_Windows
    global jsonResult
    jsonResult = {}
    jsonData = realtime_weather_info()
    if int(datetime.datetime.now().strftime('%M')) < 30:
        hours = time1 + datetime.timedelta(hours=2)
    elif int(datetime.datetime.now().strftime('%M')) >= 30:
        hours = time1 + datetime.timedelta(hours=1)

    after_hour = hours.strftime("%H") + '00'

    for i in jsonData['response']['body']['items']['item']:
        if after_hour == str(i['fcstTime']):
            jsonResult['예측시간'] = str(i['fcstTime'])[:2] + ':' + str(i['fcstTime'])[2:]
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


    print()
    for i in list(jsonResult.items()):
        print(i[0]+':'+str(i[1]))

    with open('기상정보_업데이트_%s.json'%(datetime.datetime.now().strftime('%Y%m%d %H%M%S')),'w',encoding='utf8') as outfile:
        readable_result = json.dumps(jsonResult, indent=4, sort_keys=True,ensure_ascii=False)
        outfile.write(readable_result)
        print('\n저장되었습니다.')

    jsonResult['강수형태'] = '1'
    if int(jsonResult['강수형태']) > 0:
        if g_Balcony_Windows == False:
            g_Balcony_Windows = True
            print("30분 내로 비 겁나 온다네요...문을 닫습니당.")
        else: pass

def main2():
    global g_Balcony_Windows
    global jsonResult
    jsonResult = {}
    jsonData = realtime_weather_info()
    if int(datetime.datetime.now().strftime('%M')) < 30:
        hours = time1 + datetime.timedelta(hours=2)
    elif int(datetime.datetime.now().strftime('%M')) >= 30:
        hours = time1 + datetime.timedelta(hours=1)
    after_hour = hours.strftime("%H") + '00'

    for i in jsonData['response']['body']['items']['item']:

        if after_hour == str(i['fcstTime']):
            if i['category'] == 'LGT':
                jsonResult['낙뢰'] = i['fcstValue']
            elif i['category'] == 'PTY':
                jsonResult['강수형태'] = i['fcstValue']
            elif i['category'] == 'RN1':
                jsonResult['1시간강수량'] = i['fcstValue']
            elif i['category'] == 'SKY':
                jsonResult['하늘상태'] = i['fcstValue']
            elif i['category'] == 'T1H':
                jsonResult['기온'] = i['fcstValue']

        jsonResult['예측시간'] = str(i['fcstTime'])[:2] + ':' + str(i['fcstTime'])[2:]


    with open('기상정보_업데이트_%s.json' % (datetime.datetime.now().strftime('%Y%m%d %H%M%S')), 'w',
              encoding='utf8') as outfile:
        readable_result = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(readable_result)

    jsonResult['강수형태'] = '1'
    if int(jsonResult['강수형태']) > 0:
        if g_Balcony_Windows == False:
            g_Balcony_Windows = True
        else:
            pass

def print_main_menu():
    print("\n1. 장비상태 확인")
    print("2. 장비제어")
    print("3. 인공지능 모드")
    print('4. 종료')

def print_device_status(device_name,devcie_status):
    print("%s 상태: "%device_name, end="")
    if devcie_status == True : print("작동")
    else : print("정지")

def check_device_status():
    print()
    print_device_status('난방기',g_Radiator)
    print_device_status('가스밸브', g_Gas_Valve)
    print_device_status('발코니(베란다) 창문', g_Balcony_Windows)
    print_device_status('출입문 상태', g_Door)


def print_device_menu():
    print("\n상태 변경할 기기를 선택하세요.")
    print("1. 난방기")
    print("2. 가스밸브")
    print("3. 발코니(베란다)창")
    print("4. 출입문")


def control_device():
    global g_Radiator, g_Gas_Valve, g_Balcony_Windows, g_Door

    check_device_status()
    print_device_menu()
    menu_num = int(input("번호를 입력하세요: "))

    if menu_num == 1: g_Radiator = not g_Radiator
    elif menu_num == 2: g_Gas_Valve = not g_Gas_Valve
    elif menu_num == 3: g_Balcony_Windows = not g_Balcony_Windows
    elif menu_num == 4: g_Door = not g_Door

    check_device_status()

def smart_mode():
    global g_AI_mode
    print('1. 인공지능 모드 상태 조회')
    print('2. 인공지능 모드 상태 변경')
    print('3. 실시간 기상정보 update')
    print('4. 강수예보 시뮬레이션')
    menu_num = int(input('메뉴를 선택하세요:'))

    if menu_num ==1:
        print('현재 인공지능 모드: ', end='')
        if g_AI_mode == True: print('작동')
        else : print('정지')

    elif menu_num == 2:
        g_AI_mode = not g_AI_mode
        print('현재 인공지능 모드: ', end='')
        if g_AI_mode == True: print('작동')
        else : print('정지')


    elif menu_num ==3:
        main()


def update_scheduler():
    global g_Balcony_Windows,g_AI_mode,jsonResult
    while True:
        if g_AI_mode == False:
            continue
        else:
            if g_Balcony_Windows == True:
                main2()
                time.sleep(10)
            else: pass


if __name__=='__main__':
    t = threading.Thread(target=update_scheduler)
    t.daemon = True
    t.start()

    print("<스마트 홈네트워크 시뮬레이션 프로그램 ver 1.0>")
    print("                                 - 이창현 -")
    while True:
        print_main_menu()
        menu_num = int(input("\n메뉴를 선택하세요: "))

        if(menu_num == 1):
            check_device_status()
        elif(menu_num ==2):
            control_device()
        elif(menu_num == 3):
            smart_mode()
        else:break