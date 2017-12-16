while True:
    print("구구단 프로그램입니다")
    try:
        a = input("숫자를 입력하세요:(-1:종료,all:구구단 전체출력)")
        if a == 'all':
            for i in range(2, 10):
                print('<', i, '단', '>')
                for j in range(1, 10):
                    result = i * j
                    print(i, '*', j, '=', result)
                print()
        elif int(a) == -1:
            print('프로그램을 종료합니다')
            break
        elif int(a) < -1:
            raise ValueError
        else:
            print('\n''<', int(a), '단', '>')
            for i in range(int(a), 10):
                if i <= int(a):
                    for j in range(1, 10):
                        result = i * j
                        print(i, '*', j, '=', result)
                    print()
    except:
        print("양수를 입력해주세요")
