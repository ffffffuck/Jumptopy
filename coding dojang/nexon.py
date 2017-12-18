def d(n):
    sum=n
    for i in str(n):
        sum=sum+int(i)
    return sum
print(sum(set(range(1,5000))-(set([d(i)for i in range(1,5000)]))))

print(sum(set(range(1,5000))-{x + sum([int(a) for a in str(x)]) for x in range(1, 5000)}))

