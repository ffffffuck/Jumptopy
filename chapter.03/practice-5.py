t=5     # 연간 티켓
f=3     # 1주년 무료 티켓
n=0     # 입장한 사람
while True:
    a = int(input("나이를 입력하세요:"))
    n= n + 1
    if n in range(4,24,4)and t>0:
        t=t-1
        print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인 티켓 [%s장]" %t)
        continue
    if n in range(7,28,4)and f>0:
        f=f-1
        print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료 티켓 [%s장]" %f)
        continue
    elif a in range(0,4):
        print("귀하는 유아등급이며 요금은 무료 입니다.\n즐거운 시간 되십시오,")
    elif a in range(4,14):
        print("귀하는 어린이등급이며 요금은 2000원 입니다.")
        i=int(input("요금 유형을 선택하세요\n(1:현금,2:공원 전용 신용 카드):"))
        if i == 1:
            b = int(input("요금을 입력하세요:"))
            if b == 2000:
                print("감사합니다. 티켓을 발행합니다.")
            elif b < 2000:
                print("%s원이 모자랍니다. 입력하신 %s원을 반환합니다" % ((2000 - b),b))
            else:
                print("감사합니다. 티켓을 발행하고 거스름돈 %s원을 반환합니다." % (b - 2000))
        if i == 2:
            print("%s원이 결제되었습니다. 감사합니다."%int(2000*(0.9)))
    elif a in range(14,19):
        print("귀하는 청소년등급이며 요금은 3000원 입니다.")
        i=int(input("요금 유형을 선택하세요\n(1:현금,2:공원 전용 신용 카드):"))
        if i == 1:
            b = int(input("요금을 입력하세요:"))
            if b == 3000:
                print("감사합니다. 티켓을 발행합니다.")
            elif b < 3000:
                print("%s원이 모자랍니다. 입력하신 %s원을 반환합니다." % ((3000 - b),b))
            else:
                print("감사합니다. 티켓을 발행하고 거스름돈 %s원을 반환합니다." % (b - 3000))
        if i == 2:
            print("%s원이 결제되었습니다. 감사합니다."%int(3000*(0.9)))
    elif a in range(19, 66):
        print("귀하는 성인등급이며 요금은 5000원 입니다.")
        i=int(input("요금 유형을 선택하세요\n(1:현금,2:공원 전용 신용 카드):"))
        if i == 1:
            b = int(input("요금을 입력하세요:"))
            if b == 5000:
                print("감사합니다 티켓을 발행합니다.")
            elif b < 5000:
                print("%s원이 모자랍니다. 입력하신 %s원을 반환합니다." % ((5000 - b),b))
            else:
                print("감사합니다. 티켓을 발행하고 거스름돈 %s원을 반환합니다." % (b - 5000))
        if i == 2 and a < 60:
            print("%s원이 결제 되었습니다. 감사합니다."%int(5000*(0.9)))
        if i == 2 and a >= 60:
            print("5%% 추가할인 되어 %s원이 결제 되었습니다. 감사합니다." %int(5000*(0.9)*(0.95)))
    elif a > 65 :
        print("귀하는 노인등급이며 요금은 무료 입니다.\n즐거운 시간 되십시오.")