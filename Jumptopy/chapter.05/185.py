class Service:
    secret = "영구는 존나 못생겼다"
    def __init__(self,name):
        self.name = name
        print("멤버변수 %s 를 초기화 하였습니다." %name)
    def sum(self,a,b):
        result = a + b
        print("%s님 %s + %s = %s 입니다" %(self.name,a,b,result))
    def __del__(self):
        print("저희 서비스를 이용해 주셔서 감사합니다.")

input()
pey=Service('홍길동')
input()
pey.sum(1,1)
input()
