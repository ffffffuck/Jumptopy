print("마름모 연습프로그램")
while True:
    a=int(input("홀수를 입력하세요(0<-종료):"))
    if a % 2 == 0 and a != 0:
        print("잘못 입력했습니다.짝수를 입력하세요.")
        continue
    if a == 0:
        print("마름모 연습 프로그램을 종료합니다. 감사합니다.")
        break
    for i in range(1,2):
        for i in range(1,2):
            print(' ',end='')
        for i in range(1,2):
            print('-'*a,end='')
        print()

    for i in range(1,a+2):
        if i%2 ==1: continue
        for j in range(1,2):
            print('|',end='')
        for j in range(0,(a+2-i)//2):
            print(' ', end='')
        for j in range(1,i):
            print('*', end='')
        for j in range(0, (a+2 - i) // 2):
            print(' ', end='')
        for j in range(1,2):
            print('|',end='')
        print()

    for i in range(1, a):
        if i % 2 == 1: continue
        for j in range(1,2):
            print('|',end='')
        for j in range(1, (i + 2) // 2):
            print(' ', end='')
        for j in range((2*(a-i))//2):
            print('*', end='')
        for j in range(1, (i + 2) // 2):
            print(' ', end='')
        for j in range(1, 2):
            print('|', end='')
        print()

    for i in range(1, 2):
        for i in range(1, 2):
            print(' ', end='')
        for i in range(1, 2):
            print('-' * a, end='')
        print()