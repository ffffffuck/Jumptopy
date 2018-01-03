input = input('입력:')
result=''
n=1
for i in range(len(input)-1) :
    if input[i] != input[i+1]:
        result+=input[i]+str(n)
        n=1
    else:n=n+1
result+=input[-1]+str(n)
print(result)