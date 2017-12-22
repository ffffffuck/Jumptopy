def biggest_prime_factor(n):
    i = 2
    while i*i <= n:
        q,r = divmod(n,i)
        if r == 0:
            n = q
        else:
            i += 1
    return print(n)


biggest_prime_factor(13195)