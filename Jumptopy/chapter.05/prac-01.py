
print("입장권 판매 합니다 어서 오세용")
while True:
    a = int(input('나이를 입력하세요(0을 입력하면 판매종료):'))

    if 1 <= a < 3 :
        print("유아 입니다 입장료는 무료입니다")
    if 3<= a <= 12:
        print("어린이입니다 가격은 10달러 입니다")
    if a >12 :
        print("성인입니다 가격은 15달러 입니다")
    if a == 0 :
        print("티켓 교부를 종료합니다")
        break