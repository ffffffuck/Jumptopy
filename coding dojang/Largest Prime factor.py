def larg(n):
    i=2
    while i < n:
        if n%i == 0:
            n=n//i
        i+=1
    print(n)

larg(3473673465)

