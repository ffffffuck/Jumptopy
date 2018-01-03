
grade = {"유아":"무료","어린이":"2000원","청소년":"3000원","성인":"5000원","노인":"무료"}
i=list(grade.items())

while True:
    a = int(input("나이를 입력하세요:"))
    if a in range(0,4):
        print("귀하는 %s등급이며 요금은 %s입니다." %(i[0][0],i[0][1]))
    elif a in range(4,14):
        print("귀하는 %s등급이며 요금은 %s입니다." %(i[1][0],i[1][1]))
    elif a in range(14,19):
        print("귀하는 %s등급이며 요금은 %s입니다." %(i[2][0],i[2][1]))
    elif a in range(19,65):
        print("귀하는 %s등급이며 요금은 %s입니다." %(i[3][0],i[3][1]))
    else:
        print("귀하는 %s등급이며 요금은 %s입니다." %(i[4][0],i[4][1]))