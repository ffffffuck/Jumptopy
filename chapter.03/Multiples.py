while True:
        X=int(input("X값를 입력하세요(0입력시 프로그램종료):"))
        if X==0 :
                print("프로그램을 종료합니다")
                break
        Y=int(input("Y값를 입력하세요:"))
        for c in range(X*Y,10001,X*Y):
                print(c)
