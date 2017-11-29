print("삼각형 연습프로그램")
while True:
    a=int(input("홀수를 입력하세요(0<-종료):"))
    if a % 2 == 0 and a != 0:
        print("잘못 입력했습니다.짝수를 입력하세요.")
        continue
    if a == 0:
        print("삼각형 연습 프로그램을 종료합니다. 감사합니다.")

    for i in range(1,2):
        print(' ', end='')
        print('-'*2*a,end='')
    print()

    for i in range(1,a):
        for i in range