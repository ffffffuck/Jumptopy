coffee = 3
while True:
    money = int(input("돈을 넣어주세요:"))
    if money == 300:
        coffee-=1
        print("커피를 줍니다")
    elif money >300:
        coffee-=1
        print("거스름돈 %s를 줍니다" %(money-300))
        print("커피를 줍니다")
    else:
        print("남은 커피의 양은 %s개 입니다" %coffee)
        print("돈이 모자랍니다")
    if coffee == 0 :
        print("완판 되었습니다")
        break