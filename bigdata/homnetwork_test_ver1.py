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
g_humidifier = False
g_dehumidifier = False

access_key="PUjPcu22uUk09DaNdDl6mkVTDoMG2QJWGhxwAeQVqybmmJfBDw%2F2kb0ziRxy0smbezEH77TXCv%2BfCYGP7OkDfw%3D%3D"
# access_key="i4zXtlcTwh041E8W0qOyGPnIggToM4lqBePqd5ZR8v4uJQ6WcXACinkJgll%2Fk0PYSSinPNRJL%2B07OvnTXPcHaA%3D%3D"

def get_request_url(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            return response.read().decode('utf-8')
    except Exception as e:
        pass

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
    parameters += '&numOfRows='+str(100)

    url=end_point+parameters
    retData = get_request_url(url)

    if(retData == None):return None
    else:return json.loads(retData)

def main():
    global g_Balcony_Windows,g_humidifier,g_dehumidifier
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
            elif i['category'] == 'REH':
                jsonResult['습도'] = i['fcstValue']

    print()
    for i in list(jsonResult.items()):
        print(i[0]+':'+str(i[1]))

    with open('기상정보_업데이트_%s.json'%(datetime.datetime.now().strftime('%Y%m%d %H%M%S')),'w',encoding='utf8') as outfile:
        readable_result = json.dumps(jsonData, indent=4, sort_keys=True,ensure_ascii=False)
        outfile.write(readable_result)
        print('\n[기상정보_업데이트_%s.json]'%(datetime.datetime.now().strftime('%Y%m%d %H%M%S'))+' 저장되었습니다.')
        print('예보 업데이트를 완료했습니다.')

    if int(jsonResult['강수형태']) > 0:
        if g_Balcony_Windows == False:
            g_Balcony_Windows = True
            print("\n<< 현재상태[%s] 30분 내로 비 겁나 온다네요...문을 닫습니당 >>"%jsonResult['강수형태'])
        else: pass
    elif int(jsonResult['강수형태']) ==0:
        if g_Balcony_Windows == True:
            g_Balcony_Windows = False

    if int(jsonResult['습도']) < 45:
        if g_humidifier == False:
            g_humidifier = True
            print("\n<< 현재습도[%s%%] 습도가 낮네요... 가습기를 켭니다 >>"%jsonResult['습도'])
        if g_dehumidifier == True:
            g_dehumidifier = False

    elif int(jsonResult['습도']) > 55 :
        if g_dehumidifier == True:
            g_dehumidifier = False
            print('\n<< 현재습도[%s%%] 습도가 높습니다 제습기를 켭니다 >>'%jsonResult['습도'])
        if g_humidifier == True:
            g_humidifier = False

    elif 45 <= int(jsonResult['습도']) <= 55:
        print('\n<< 현재습도[%s%%] 쾌적 합니다 >>' % jsonResult['습도'])

def main2():
    global g_Balcony_Windows,g_humidifier,g_dehumidifier
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
            elif i['category'] == 'REH':
                jsonResult['습도'] = i['fcstValue']

        jsonResult['예측시간'] = str(i['fcstTime'])[:2] + ':' + str(i['fcstTime'])[2:]


    with open('기상정보_업데이트_%s.json' % (datetime.datetime.now().strftime('%Y%m%d %H%M%S')), 'w',
            encoding='utf8') as outfile:
        readable_result = json.dumps(jsonData, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(readable_result)

def read_forcast():
    global  jsonResult,g_Balcony_Windows,g_humidifier,g_dehumidifier

    if int(jsonResult['강수형태']) > 0:
        if g_Balcony_Windows == False:
            g_Balcony_Windows = True
        else:pass
    if int(jsonResult['강수형태']) == 0:
        if g_Balcony_Windows == True:
            g_Balcony_Windows = False
        else:pass
    #가습
    if int(jsonResult['습도']) < 55:
        if g_humidifier == False:
            g_humidifier = True
        if g_dehumidifier == True:
            g_dehumidifier = False

    elif int(jsonResult['습도']) > 45:
        if g_dehumidifier == False:
            g_dehumidifier = True
        if g_humidifier == True:
            g_humidifier = False

def simulation(x):
    global g_Balcony_Windows,g_humidifier,g_dehumidifier

    jsonData = realtime_weather_info()
    if int(datetime.datetime.now().strftime('%M')) < 30:
        hours = time1 + datetime.timedelta(hours=2)
    elif int(datetime.datetime.now().strftime('%M')) >= 30:
        hours = time1 + datetime.timedelta(hours=1)

    after_hour = hours.strftime("%H") + '00'

    jsonResult = {}
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
            elif i['category'] == 'REH':
                jsonResult['습도'] = i['fcstValue']


            if x == '1':jsonResult['강수형태'] = '1'
            elif x =='2':jsonResult['습도'] = '26'
            elif x =='3':jsonResult['습도'] = '70'
            elif x =='4':
                g_Balcony_Windows = True
                g_humidifier = True
                g_dehumidifier = True

                jsonResult['습도'] = '50'
                jsonResult['강수형태'] = '0'

    check_device_status()
    print()
    for i in list(jsonResult.items()):
        print(i[0] + ':' + str(i[1]))

    with open('기상정보_시뮬레이션.json', 'w',encoding='utf8') as outfile:
        readable_result = json.dumps(jsonData, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(readable_result)
        print('\n가상정보_시뮬레이션.json 이 저장되었습니다.')
        print('\n시뮬레이션 환경이 조성되었습니다.')

    if x == '1':
        if int(jsonResult['강수형태']) > 0:
            print("\n<< 현재상태[%s] 30분 내로 비 겁나 온다네요...발코니 창을 닫겠습니다 >>" % jsonResult['강수형태'])
            if g_Balcony_Windows == False:
                g_Balcony_Windows = True
            else:
                pass
                print('<< 날씨가 맑네요 계속 열고 있겠습니다 >>')

        elif int(jsonResult['강수형태']) == 0:
            if g_Balcony_Windows == True:
                g_Balcony_Windows = False
            else:pass

    elif x =='2':
        if int(jsonResult['습도']) < 45:
            print("\n<< 현재습도[%s%%] 습도가 낮네요... 가습기를 켭니다 >>" % jsonResult['습도'])
            if g_humidifier == False:
                g_humidifier = True
            else:pass
        elif int(jsonResult['습도']) > 55:
            if g_humidifier == True:
                g_humidifier = False
        elif 45 <= int(jsonResult['습도']) <=55 :
            print('\n<< 현재습도[%s%%] 쾌적 합니다 >>' % jsonResult['습도'])

    elif x =='3':
        if int(jsonResult['습도']) > 55:
            print("\n<< 현재습도[%s%%] 습도가 높네요... 제습기를 켭니다 >>" % jsonResult['습도'])
            if g_dehumidifier == False:
                g_dehumidifier = True
            else:pass
        elif int(jsonResult['습도']) < 55:
            if g_dehumidifier == True:
                g_dehumidifier = False
        elif 45 <= int(jsonResult['습도']) <=55 :
            print('\n<< 현재습도[%s%%] 쾌적 합니다 >>' % jsonResult['습도'])

    elif x =='4':
        if 45 <= int(jsonResult['습도']) <=55 :
            print('\n<< 현재습도[%s%%] 쾌적 합니다 모든 관련제품을 끕니다 >>' % jsonResult['습도'])
            if g_Balcony_Windows == True:
                g_Balcony_Windows = False
            if g_dehumidifier == True:
                g_dehumidifier = False
            if g_humidifier == True:
                g_humidifier = False
    else:
        print('\n옳은값을 입력하세요')


def print_main_menu():
    print("\n1. 장비상태 확인")
    print("2. 장비제어")
    print("3. 스마트모드")
    print('4. 시뮬레이션모드')
    print('5. 종료')

def print_device_status(device_name,devcie_status):
    print("%s 상태: "%device_name, end="")
    if devcie_status == True : print("작동")
    else : print("정지")

def print_device_status2(device_name,device_status):
    print("%s 상태: "% device_name,end='')
    if device_status == True: print('열림')
    else : print('잠김')

def check_device_status():
    print()
    print_device_status('난방기',g_Radiator)
    print_device_status2('가스밸브', g_Gas_Valve)
    print_device_status2('발코니(베란다) 창문', g_Balcony_Windows)
    print_device_status2('출입문 상태', g_Door)
    print_device_status('가습기', g_humidifier)
    print_device_status('제습기',g_dehumidifier)


def print_device_menu():
    print("\n상태 변경할 기기를 선택하세요.")
    print("\n1. 난방기")
    print("2. 가스밸브")
    print("3. 발코니(베란다)창")
    print("4. 출입문")
    print('5. 가습기')
    print('6. 제습기\n')


def control_device():
    global g_Radiator, g_Gas_Valve, g_Balcony_Windows, g_Door,g_humidifier,g_dehumidifier

    check_device_status()
    print_device_menu()
    try:
        menu_num = int(input("번호를 입력하세요: "))
    except:
        print('옳은값을 입력하세요')
        return control_device()

    if menu_num == 1: g_Radiator = not g_Radiator
    elif menu_num == 2: g_Gas_Valve = not g_Gas_Valve
    elif menu_num == 3: g_Balcony_Windows = not g_Balcony_Windows
    elif menu_num == 4: g_Door = not g_Door
    elif menu_num == 5: g_humidifier = not g_humidifier
    elif menu_num == 6: g_dehumidifier = not g_dehumidifier
    else:
        print('\n옳은값을 입력하세요.')
        return control_device()

    check_device_status()

def smart_mode():
    global g_AI_mode
    print('\n1. 인공지능 모드 상태 조회')
    print('2. 인공지능 모드 상태 변경')
    print('3. 실시간 기상정보 update\n')
    try:
        menu_num = int(input('메뉴를 선택하세요:'))
    except:
        print("\n옳은 값을 입력하세요.")
        return smart_mode()

    if menu_num ==1:
        print('\n현재 인공지능 모드: ', end='')
        if g_AI_mode == True: print('작동') # HK Commnet] 장비에 맞는 메세지를 출력할것
        else : print('정지')

    elif menu_num == 2:
        g_AI_mode = not g_AI_mode
        print('\n현재 인공지능 모드: ', end='')
        if g_AI_mode == True: print('작동')
        else : print('정지')

    elif menu_num ==3:
        main()
    else:
        print('\n옳은 값을 입력하세요')
        return smart_mode()

def update_scheduler():
    global g_Balcony_Windows,g_AI_mode,jsonResult
    stop1 = True
    stop2 = True

    while True:
        if g_AI_mode == False:
            continue
        else:
            if stop1 == True:
                main2()
                stop1 = False
            else: pass
            read_forcast()
            if datetime.datetime.now().strftime("%M%S") == '4501':
                if stop2 == True: # 셈플프로그램 만들어서 확인할 것. 불필요한 조건으로 보임
                    stop2 = False
                    main2()
                    read_forcast()
                    time.sleep(3598)
            else: pass


if __name__=='__main__':

    t = threading.Thread(target=update_scheduler)
    t.daemon = True
    t.start()

    print("<스마트 홈네트워크 시뮬레이션 프로그램 ver 1.0>")
    print("                                 - 이창현 -")
    while True:
        print_main_menu()
        try:
            menu_num = int(input("\n메뉴를 선택하세요: "))
        except:
            print('\n옳은값을 입력하세요.')
            continue

        if(menu_num == 1):
            check_device_status()
        elif(menu_num ==2):
            control_device()
        elif(menu_num == 3):
            smart_mode()
        elif(menu_num ==4):
            print("\n1. 비오는날 시뮬레이션(발코니창 제어)\n2. 건조한날 시뮬레이션(가습기 제어)"
                  "\n3. 습한날 시뮬레이션(제습기 제어)\n4. 상쾌한날 시뮬레이션(제습기/가습기 제어)\n\n입력 : ",end='')
            simulation(input())
        elif(menu_num ==5):
            break
        else:
            print("옳은값을 입력하세요.")