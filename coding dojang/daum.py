s=[1, 2, 7, 8, 13, 15, 17, 20]

a=[s[i+1]-s[i] for i in range(len(s)-1)]
for i in range(len(s)-1):
    if s[i+1]-s[i] ==min(a):
        print((s[i] , s[i+1]))

