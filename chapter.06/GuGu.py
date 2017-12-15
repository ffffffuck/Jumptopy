def GuGu(N):
    list = []

    for i in range(1,10):
        try:N<0
        except:print("양수만 집어 넣으세요")
        a = i*N
        list.append(a)
        return list


N=int(input("숫자 넣으세요"))
print(GuGu(N))