g_Radiator = False
g_Gas_valve = False
g_balcony_Window = False
g_Door = False

def print_main_menu():
    print("\n1. 장비상태 확인")
    print('2. 장비제어')
    print('3. 프로그램 종료')


def check_status(device,device_name):
    print(device_name +'상태 : ',end='')
    if (device == True): print('작동')
    elif (device == False) : print('정지')

def check_device_status():
    check_status(g_Radiator,'난방기')
    check_status(g_Gas_valve,'가스밸브')
    check_status(g_balcony_Window,'발코니(베란다) 창')
    check_status(g_Door,'출입문')

def print_device_menu():
    print('\n상태 변경할 기기를 선택하세요')
    print('1. 난방기')
    print('2. 가스밸브')
    print('3. 발코니(베란다) 창')
    print('4. 출입문')

def control_device():
    global g_Radiator,g_Gas_valve,g_balcony_Window,g_Door

    check_device_status()
    print_device_menu()
    menu_num = int(input("번호를 입력 하세요 : "))

    if menu_num == 1:g_Radiator = not g_Radiator
    elif menu_num == 2: g_Gas_valve = not g_Gas_valve
    elif menu_num == 3: g_balcony_Window =  not g_balcony_Window
    elif menu_num == 4: g_Door = not g_Door

    check_device_status()


while True:
    print_main_menu()
    menu_num = int(input("메뉴를 선택하세요 : "))

    if(menu_num == 1):
        check_device_status()
    elif(menu_num ==2):
        control_device()
    elif(menu_num == 3):
        break