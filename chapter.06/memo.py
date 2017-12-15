import sys

option = sys.argv[1]

if option =='-a':
    try :
        f = open('memo.txt','r')
        f.close()
        f = open('memo.txt','a')
        args = sys.argv[2]
        for i in args:
            f.write(i)
            print(i, end='')
        f.write('\n')
        f.close()
    except:
        n=input("1.새로 생성하시겠습니까?:\n2:파일경로를 입력하겠습니다")
        if n =='1':
            f = open('memo.txt', 'w')
            f.close()
            f = open('memo.txt', 'a')
            args = sys.argv[2]
            for i in args:
                f.write(i)
                print(i, end='')
            f.write('\n')
            f.close()
        if n=='2':
            E=input("경로를 입력하세요:")
            f = open(E+'\memo.txt','a')
            f.close()
            args = sys.argv[2]
            for i in args:
                f.write(i+'\n')
                print(i, end='')
            f.write('\n')
            f.close()
if option =='-au':
    try :
        f = open('memo.txt','r')
        f.close()
        f = open('memo.txt','a')
        args = sys.argv[2]
        for i in args:
            f.write(i.upper())
            print(i.upper(), end='')
        f.write('\n')
        f.close()
    except:
        n=input("1.새로 생성하시겠습니까?:\n2:파일경로를 입력하겠습니다")
        if n =='1':
            f=open('memo.txt', 'w')
            f.close()
            f = open('memo.txt', 'a')
            args = sys.argv[2]
            for i in args:
                f.write(i.upper())
                print(i.upper(), end='')
            f.write('\n')
            f.close()
        if n=='2':
            E=input("경로를 입력하세요:")
            f = open(E+'\memo.txt','a')
            f.close()
            args = sys.argv[2]
            for i in args:
                f.write(i.upper())
                print(i.upper(), end='')
            f.write('\n')
            f.close()

if option == '-v':
    try :
        f = open('memo.txt','r')
        while True:
            line = f.readline()
            if not line:break
            print(line)
    except:
        n=input("1.종료하시겠습니까?\n2:파일경로를 입력하겠습니다")
        if n =='1':exit()
        if n=='2':
            E=input("경로를 입력하세요:")
            f = open(E+'\memo.txt', 'r')
            while True:
                line = f.readline()
                if not line: break
                print(line)


    # args = sys.argv[1:]
    # for i in args:
    #     print(i.upper(), end=' ')