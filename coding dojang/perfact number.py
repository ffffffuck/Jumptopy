n=int(input("자연수"))
per = []
for a in range(1,n+1):
    sum = 0
    for i in range(1,a):
        if a%i == 0 :
            sum+=i
    if sum==a:
            per.append(a)
print(per)
#
# 코딩도장 정답
# num= int(input("숫자를 입력하시오 : "))
# print([x for x in range(1, num+1) if x==sum(y for y in range(1, x) if x%y==0)])

#내거 고친거
# n=int(input("자연수"))
# print(list(a for a in range(1,n+1) if a== sum(i for i in range(1,a) if a%i==0)))

