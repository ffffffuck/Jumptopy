print("삼각형 연습 프로그램")
while True:
    a = int(input("홀수를 입력하세요.\n(0<-프로그램종료):"))
    if a % 2 == 0 and a != 0:
        print("올바른 수를 입력해주세요.")
        continue
    if a == 0:
        print("삼각형 연습 프로그램을 이용해 주셔서 감사합니다.")
        break

    for i in range(1,a+1):
        for j in range(1,a+1-i):
            print(' ',end='')
        for j in range(1,(2*i)):
            print('*', end='')
        print()
