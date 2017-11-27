coffee = 3
while True:
    money = int(input("돈을 넣어주세요 커피값은 300원 입니다:"))
    if money ==300:
        print("커피를 내립니다")
        coffee = coffee - 1
        print("커피 재고는 %s 개입니다" % coffee)
    elif 1000 > money > 300:
        print("300원빼고 거스름돈 %s원 드립니다" %(money - 300))
        print("커피를 내립니다")
        coffee = coffee - 1
        print("커피 재고는 %s 개입니다" % coffee)
    elif money < 300:
        print("돈이 모자랍니다 그지야")
    elif money >= 1000:
        print("동전만 넣어주세요")
    if coffee == 0 :
        print("재고가 없습니다")
        break