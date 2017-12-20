input='''
3
195
265
750
'''
input = input.split('\n')[1:-1]
for i in range(len(input)):
    a = int(input[i])
    number=1
    while True:
        if a < 10:
            break
        if a+int(str(a)[::-1]) != int(str(a + int(str(a)[::-1]))[::-1]):
            a= a + int(str(a)[::-1])
            number=number+1
        elif a+int(str(a)[::-1]) == int(str(a + int(str(a)[::-1]))[::-1]):
            print(number,' ', a + int(str(a)[::-1]))
            break
