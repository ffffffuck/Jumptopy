
print("숫자와 숫자사이의 합을 구합니다")
while True:
    num1 = int(input("첫번째 숫자를 넣으세요:")) -1
    num2 = int(input("두번째 숫자를 넣으세요:"))
    sum = 0
    while num1 < num2:
        num1=num1+1
        sum = sum + num1
    print("정답은 %s 입니다. " % sum)
    if num1 > num2: print("잘못 입력했습니다")

