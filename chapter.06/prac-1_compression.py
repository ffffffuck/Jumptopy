alp = ""
n=[]
N = list(input("입력하세요"))
for i in range(len(N)):
        if N[i-1] != N[i]:
            n.append(i)



print(N)
print(n)
for i in range(len(n)):
    n[1]-n[0]