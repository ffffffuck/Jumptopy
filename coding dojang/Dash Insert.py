input = input("숫자넣어")
result = ""
for i in range(len(input) - 1):
    if int(input[i]) % 2 == 0 and int(input[i + 1]) % 2 == 0:
        result += input[i] + '*'
    elif int(input[i]) % 2 == 1 and int(input[i + 1]) % 2 == 1:
        result += input[i] + '-'
    else:
        result += input[i]
result += input[-1]
print(result)



# i = list(map(int,' '.join(input()).split()))
# answer = [str(i[0])]
# for x in range(len(i)-1):
#     if i[x]%2==0 and i[x+1]%2==0:
#         answer.append('*')
#     if i[x]%2==1 and i[x+1]%2==1:
#         answer.append('-')
#     answer.append(str(i[x+1]))
# print(''.join(answer))