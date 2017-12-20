# n_list=[]
# for i in range(0,10001):
#     if i%2 ==1 and i%5 ==1:
#         n_list.append(str(i))

input='''
3
7
9901
'''

def Ones(input):
    input = input.split('\n')[1:-1]
    for i in range(len(input)):
        n = int(input[i])
        j = '1'
        while True:
            if int(j)%n != 0:j+=str(1)
            else:break
        print(len(j))

Ones(input)