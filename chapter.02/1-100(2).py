sum = 0
while True:
    a=int(input("첫번재는:"))
    b=int(input("두번째는:"))
    for i in range(a,b+1):
        sum += i
    print("정답은 %s 입니다. " % sum)
    if a>b:
        print("다시 입력하세요.")