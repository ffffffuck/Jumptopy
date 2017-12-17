def jinsu(a, n):
	a= 233
	b=''
	while True:
		b=b+(str(a%n))
		a=a//n
		if a < 1: break
	print(''.join(reversed(b)))
	
jinsu(233,2)