result = []
candidates = list(range(3,100000))
base = 2
product = base
while candidates:
    while product < 100000:
        if product in candidates:
            candidates.remove(product)
        product = product+base
    result.append(base)
    base = candidates[0]
    product = base
    del candidates[0]
result.append(base)
print(len(result))

#
def get_prime_num(limit):
    current = 2
    num_list = [x for x in range(2, limit+1)]
    tmp_list = []
    while current**2 <= limit:
        num_list = list(filter(lambda x: x % current, num_list))
        tmp_list.append(current)
        current = num_list[0]
    return tmp_list + num_list
print(len(get_prime_num(10000000)))
