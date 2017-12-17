n= input('범위, 첫번째수,두번째수를 입력하세요.(종료:프로그램 종료):').split()
d = list(filter(lambda i: i % int(n[1])==0, range(1,int(n[0])+1)))
e = list(filter(lambda i: i % int(n[2])==0, range(1,int(n[0])+1)))

print("0부터 %d이하의 범위를 선택하셨습니다. 이 중에서" %int(n[0]))
print("%s의 배수는 %s입니다." %(int(n[1]), ','.join([str(i) for i in d])))
print("%s의 배수는 %s 입니다." %(int(n[2]),','.join([str(i) for i in e])))
print("%s와 %s의 배수는 %s 입니다."%(int(n[1]),int(n[2]),','.join([str(i) for i in list(set(d+e))])))
print("따라서 0부터 %s이하의 범위에서 %s와 %s의 배수의 총합은 %s 입니다."%(int(n[0]),int(n[1]),int(n[2]), sum(list(set(d+e)))))


# n= input('범위, 첫번째수,두번째수를 입력하세요.(종료:프로그램 종료):').split()
# d=[]
# e=[]
# for i in range(1,int(n[0])+1):
#     if i%int(n[1])==0 :d.append(i)
#     if i%int(n[2])==0 :e.append(i)
#
# print("0부터 %s이하의 범위를 선택하셨습니다. 이 중에서" %int(n[0]))
# print("%s의 배수는 %s입니다." %(int(n[1]), ','.join([str(i) for i in d])))
# print("%s의 배수는 %s 입니다." %(int(n[2]),','.join([str(i) for i in e])))
# print("%s와 %s의 배수는 %s 입니다."%(int(n[1]),int(n[2]),','.join([str(i) for i in list(set(d+e))])))
# print("따라서 0부터 %s이하의 범위에서 %s와 %s의 배수의 총합은 %s 입니다."%(int(n[0]),int(n[1]),int(n[2]), sum(list(set(d+e)))))
