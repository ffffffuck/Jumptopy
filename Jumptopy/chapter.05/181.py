class Service:
    secret = "영구는 배꼽이 두개다"
    def setname(self,name):
        self.name = name
    def sum(self,a,b):
        result = a + b
        print("%s님 %s + %s = %s 입니다" %(self.name,a,b,result))

pey = Service()
pey.setname('홍길동')


#def 에서 setname 대신 __init__ 하면
# 위에꺼랑
#pey=service('홍길동')이랑 똑같음 ㅇㅋㅇㅋ

pey.sum(1,2)
print(pey.secret)