# 1~1000에서 각 숫자의 개수 구하기
a = str(list(range(1,1001)))
for i in range(10):
    print(i,':', a.count(str(i)))
