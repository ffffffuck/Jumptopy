def search_visitor(name):
    f=open("visitors_book.txt", 'r')
    data=f.read()
    if name in data:
        print("%s님 다시 방문해주셔서 감사합니다. 즐거운 시간되세요." %name)
    else:
        b=input("생년월일을 입력하세요:")
        f = open("visitors_book.txt", 'a')
        f.write(name+' '+b+'\n')
        print('%s님 첫방문을 환영합니다.' %name)
        f.close()
        return

while True:
    name= input("이름을 입력하세요:")
    search_visitor(name)