import random
import string

input1 = list(random.randint(1,10) for i in range(1,100))
input2 = list(random.choice(string.ascii_letters) for i in range(1,100))
input=input1+input2
random.shuffle(input)
input=list(map(str,input))

# input = 'a1b2cde3~g45hi6'
def Digit(n):
    result = []
    for i in range(len(n)):
        if int(len(n[:i]))%2 != 0:
            if n[i].isdigit():
                result.append('*')
            else:result.append(n[i])
        else: result.append(n[i])
    print(''.join(result))

print(''.join(input),'\n')
Digit(input)


