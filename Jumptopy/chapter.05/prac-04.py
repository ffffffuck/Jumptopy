
while True:
    N=input("세 개의 양수를 입력하세요(종료-1):").split()
    # if len(N) == 3 :
    #     a = int(N[0])
    #     b = int(N[1])
    #     c = int(N[2])
    if N[0] == '-1':
        print("프로그램 종료합니다")
        break
    a = int(N[0])
    b = int(N[1])
    c = int(N[2])
    # if len(N) <= 2 and int(N[0]) == -1:
    #     print('프로그램을 종료합니다')
    #     break
    if c % a == 0 and c % b == 0:
        print('%s는 %s와 %s의 공배수 입니다' % (c, a, b))
    if c % a >= 1 or c % b >= 1:
        print("%s는 %s와 %s의 공배수가 아닙니다" % (c, a, b))