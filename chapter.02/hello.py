while True :
    sex = int(input("성별은(남자는1여자는0):"))
    if sex == 1 or sex == 0 :
        age = int(input("나이는:"))
        if sex ==1 and 100 > age > 30 :
            print("남자 노땅입니다")
        elif sex ==1 and age <= 30:
            print("남자 꼬맹이입니다")
        elif sex ==0 and 100 > age > 30 :
            print("여자 상폐입니다")
        elif sex == 0 and age <= 30:
            print("여자 꼬맹이입니다")
    if sex >= 3:
            print("장난치지마라")
