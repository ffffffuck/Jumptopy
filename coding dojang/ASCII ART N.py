
n= int(input("숫자:"))
if n==1:
    print('N')
else:
    print('N'+' '*(n-2)+'N')
    for j in range(n-2):
        print('N'+' '*j+'N'+' '*((n-2)-(j+1))+'N')
    print('N'+' '*(n-2)+'N')




