def GuGu(N):
    list = []
    for i in range(1,10):
        a = i*N
        list.append(a)
    return list


N=int(input("숫자 넣으세요"))
print(GuGu(N))