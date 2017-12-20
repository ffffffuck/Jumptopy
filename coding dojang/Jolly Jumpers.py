input='''
4 1 4 2 3
5 1 4 2 -1 6
'''

input= input.split('\n')[1:-1]

def Jolly(n):
    for j in range(len(input)):
        n= input[j].split()
        for i in range(len(n) - 1):
            b = abs(int(n[i + 1]) - int(n[i]))
        if b in range(1,len(n)) :
            print("Jolly")
        else:
            print("Not Jolly")

Jolly(input)


