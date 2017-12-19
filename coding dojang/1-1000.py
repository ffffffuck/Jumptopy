# 1~1000에서 각 숫자의 개수 구하기
# a = str(list(range(1,1001)))
# print(a)
# for i in range(10):
#     print(i,':', a.count(str(i)))

input = 1000
g=[]
for i in range(1,input+1):
    g.append((i))
g=str(g)
print(g)
for j in range(10):
    print(g.count(str(i)))