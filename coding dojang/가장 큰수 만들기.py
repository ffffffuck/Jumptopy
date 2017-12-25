input=input("숫자입력:")

input=input.split(' ')
input=list(map(int, list(''.join(input))))
input.sort()
input.reverse()
input=''.join(map(str,input))

print(input)



