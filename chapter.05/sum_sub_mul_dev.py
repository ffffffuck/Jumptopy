def sub(a,b):
    return a-b

while True:
    n = input("숫자 두개를 입력하세요:").split()
    if n[0] == '종료':
        print("프로그램 종료합니다")
        exit()
    try:
        a = int(n[0])
        b = int(n[1])
    except:
        try:n[0] = int(n[0])
        except:print("죄송합니다 첫번째 입력이 [%s] 입니다 숫자를 입력하세요" %n[0])
        try:n[1] = int(n[1])
        except:print("죄송합니다 두번째 입력이 [%s] 입니다 숫자를 입력하세요" %n[1])
    else:print(sum(a,b))