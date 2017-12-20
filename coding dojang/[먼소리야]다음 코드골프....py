for n in [1,1,2,4,8,48,8,4,2,1,1]:
    s=''.join([(' ','*')[int(x)] for x in bin(n)[2:]])
    print("%6s"%s+"%-s"%s[-2::-1])