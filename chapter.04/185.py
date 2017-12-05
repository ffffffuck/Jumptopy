class Service:
    secret = "영구는 존나 못생겼다"
    def __init__(self,name):
        self.name = name
    def sum(self,a,b):
        result = a + b
        print("%s님 %s + %s = %s 입니다" %(self.name,a,b,result))

pey=Service('홍길동')

pey.sum(1,1)
