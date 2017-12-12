def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def dev(a,b):
    result = a/b
    return result
def sum(a,b):
    return a+b

while True:
    i = int(input("계산기 모드를 선택하세요.\n1.덧셈\n2.뺄셈\n3.곱셈\n4.나눗셈\n5.프로그램종료"))
    if i == 1 :z=sum
    elif i == 2 :z=sub
    elif i == 3 :z=mul
    elif i == 4 :z=dev
    elif i == 5 :
        print("프로그램을 종료합니다")
        break
    try:
        n = input("숫자 두개를 입력하세요:").split()
        try:
            a = int(n[0])
            b = int(n[1])
        except:
            try:n[0] = int(n[0])
            except:print("죄송합니다 첫번째 입력이 [%s] 입니다 숫자를 입력하세요" %n[0])
            try:n[1] = int(n[1])
            except:print("죄송합니다 두번째 입력이 [%s] 입니다 숫자를 입력하세요" %n[1])
        else:
            if i == 4 and int(n[1]) == 0:
                print("죄송합니다 두번째 입력에서 0을 입력하셨습니다 분모는 0이 되어서는 안됩니다")
            else:
                print("결과는 [%s] 입니다" %z(a,b))
                print()
    except:
        print("옳은값을 입력하세요")


