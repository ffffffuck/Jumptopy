def replace(n):
    a=''
    for i in n:
        if i.isupper():i = '_'+i.lower()
        elif i.isdigit():i = '_' + i
        a=a+i
    print(a)

replace('codingDojang')