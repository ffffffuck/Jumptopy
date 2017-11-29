print("마름모 연습 프로그램")
while True:
    a = int(input("홀수를 입력하세요.\n(0<-프로그램종료):"))
    if a % 2 == 0 and a != 0:
        print("올바른 수를 입력해주세요.")
        continue
    if a == 0:
        print("마름모 연습프로그램을 이용해 주셔서 감사합니다.")
        break

    for i in range(1,2):
        for i in range(1,2):
            print(' ',end='')
        for i in range(1,2):
            print('-'*((2*a)-1))

    for i in range(1,a):
        for j in range(1,2):
            print('|',end='')
        for j in range(1,(a+1)-i):
            print(' ',end='')
        for j in range(1,(2*i)):
            print('*', end='')
        for j in range(1,(a+1)-i):
            print(' ', end='')
        for j in range(1,2):
            print('|', end='')
        print()

    for i in range(1,2):
        for j in range(1,2):
            print('|', end='')
        for i in range(1,2*a):
            print('*', end='')
        for j in range(1, 2):
            print('|', end='')
        print()

    for q in range(1,a):
        for w in range(1,2):
            print('|', end='')
        for w in range(1, q + 1):
            print(' ', end='')
        for w in range(1,(2*a)-(2*q)):
            print('*', end='')
        for w in range(1,q + 1):
            print(' ', end='')
        for w in range(1,2):
            print('|', end='')
        print()

    for i in range(1,2):
        for i in range(1,2):
            print(' ', end='')
        for i in range(1,2):
            print('-' * ((2 * a) - 1))