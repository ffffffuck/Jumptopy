while True:
    m=int(input("총건수:"))
    n=int(input("한페이지게시물수:"))
    a = m/n
    if m%n == 0:
        print("%d장 출력합니다" %(a))
    else:
        print("%d장 출력합니다" %(a+1))
