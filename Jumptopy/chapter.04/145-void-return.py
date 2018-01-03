def sum(a, b):
    print("%d, %d의 합은 %d 입니다" % (a,b, a+b))

sum(3,4)

a= sum(1,2)

def say():
    print('Hi')

def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum +i
    return sum

