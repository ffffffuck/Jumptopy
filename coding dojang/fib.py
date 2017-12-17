a = 0
b = 1
n=0
while b <4000000:
    a = a+b	
    b,a = a,b
    if a%2==0:
	       n+=a
    print(n)

	