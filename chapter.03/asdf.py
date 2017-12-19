def f(s):
    t = s.split()
    go = int(t[0])
    src = t[1:]
    result = [None] * len(src)
    for i in range(len(src)):
        result[(i+go) %len(src)] = src[i]
    return " ".join(result)

print(f("8 10 20 30 40 50"))
print(f("-8 A B C D E F G"))