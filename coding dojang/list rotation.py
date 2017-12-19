a=input("입력:").split(' ')

rot_num=int(a[0])
A=a[1:]
rot_num=rot_num%len(A)
D=[]
for i in range(len(A)):
    index_n= A.index(A[i])-(rot_num)
    if index_n >= len(A):
        index_n = index_n - len(A)
    D.append(index_n)
if rot_num == 0:
    print(' '.join(A))
for x in D :
    print(A[int(x)],' ',end='')
