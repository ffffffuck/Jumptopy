import re

# input = 'cat'
def cigar(input,n):
    g=''
    # a='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    c=re.compile('[A-Z]+')
    a=re.findall('[A-Z]+',input)

    # a=a*2
    for j in range(len(input)):
        for i in a:
            if input[j] == a[i]:
                try: g=g+a[i+n]
                except:pass
    print(g)

cigar('XYZ', 5)

