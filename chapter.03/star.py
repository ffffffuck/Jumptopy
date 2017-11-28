while True:

    a = int(input("홀수를 입력하세요(0<-프로그램종료):"))
    if a % 2 == 0:
        print("홀수를 입력하세요:")
        continue

    for i in range(1,(a+1)):
        for j in range(1,(a+1)-i):
            print(' ',end='')
        for i in range(1,(2*i)):
            print('*', end='')

        print()
    if a == 0 :
        print("마름모 연습프로그램을 이용해 주셔서 감사합니다.")
        break
