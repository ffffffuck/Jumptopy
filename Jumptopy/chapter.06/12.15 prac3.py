def getTotalPage(m,n):
    p = int(m/n)
    if m % n == 0:
        print("게시물 총건수:%s, 한페이지에 보여줄 게시물 수 : %s, 총페이지수: %s" % (m, n, p))
    else:
        print("게시물 총건수:%s, 한페이지에 보여줄 게시물 수 : %s, 총페이지수: %s" % (m, n, p + 1))

f = open("condition.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    line = line.split()
    for i in line:
        m = line[0]
        n = line[1]
    try:
        m=int(m)
        n=int(n)
        getTotalPage(m,n)
    except: pass






