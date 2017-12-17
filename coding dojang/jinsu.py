def jinsu(a, n):
	b = ''
	c = 'ABCDEF'
	while True:
		r = a % n
		if r < 10 :
			b = b + str(r)
		else:
			r = c[r-10]
			b = b + str(r)
		a=a//n
		if a < 1: break
	b=''.join(reversed(b))
	print(b)
	
jinsu(233,16)

