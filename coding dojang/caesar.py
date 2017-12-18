def caesar(input,n):
    g=''
    for i in input:
        if i.isalpha():
            if i.isupper():
                g=g+(chr((ord(i)-ord('A') +n)%26 + ord('A')))
            else:
                g = g + (chr((ord(i) - ord('a') + n) % 26 + ord('a')))
        else:
            g=g+i
    print(g)

caesar('fuck you man!',5)