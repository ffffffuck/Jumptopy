class Service:
    secret = "영구는 존나 못생겼다"
    def setname(self,name):
        self.name = name
    def sum(self,a,b):
        result = a + b
        print("%s님 %s + %s = %s 입니다" %(self.name,a,b,result))

pey = Service()
pey.setname('홍길동')

pey.sum(1,2)
