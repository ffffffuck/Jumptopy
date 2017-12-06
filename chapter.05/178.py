class Service:
    secret="영구는 배꼽이 두개다"
    def sum(self,a,b):
        result= a + b
        print("%s + %s = %s입니다" %(a,b,result))

pey = Service()

print(pey.sum(1,5))


