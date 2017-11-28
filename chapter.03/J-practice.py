while True:
    a = int(input("나이를 입력하세요:"))
    if a <=3:
        print("요금은 무료 입니다.")
    elif 4<= a <= 13:
        print("요금은 2000원 입니다.")
    elif 14 <= a <=18:
        print("요금은 3000원 입니다.")
    elif 19<= a <=65:
        print("요금은 5000원 입니다.")
    else:
        print("요금은 무료 입니다.")
