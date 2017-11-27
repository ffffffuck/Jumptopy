while True:
    a = int(input("홀수를 입력하세요:"))
    if a == 0:
        print("마름모 연습프로그램을 이용해주셔서 감사합니다.")
    if a % 2 == 0: continue
    elif a > 0 :
        for i in range(1,a+1):
            for j in range(1,(a+1)-i):
                print(' ', end='')
            for j in range(1,i*2,1):
                print('*', end='')

            print()