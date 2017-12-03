while True:
        a= int(input("입력받을 갯수를 정하세요:"))
        b=[]
        for i in range(a):
            i = int(input("정수를 입력하세요:"))
            b.append(i)
        print("합:", sum(b))
        print("평균:", sum(b)//a)
        del a,b,i