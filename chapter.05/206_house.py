class Housepak:
    lastname= '박'
    def __init__(self,name):
        self.fullname = self.lastname + name
    def travel(self, where):
        self.travel = where
        print("%s, %s 여행을 가다." %(self.fullname, where))
    def love(self, other):
        self.love = other
        print("%s는 %s와 사랑에 빠졌다." %(self.fullname, other.fullname))
    def __add__(self, other):
        print("%s는 %s와 결혼했다." %(self.fullname, other.fullname))


class HouseKim(Housepak):
    lastname= '김'
    def travel(self,where,day):
        self.time = day
        print("%s, %s여행 %s일 가네." %(self.fullname,where,day))


pey= Housepak('보검')
pey.travel('보라카이')
juliet = HouseKim('선아')
juliet.travel('부산','3')
pey.love(juliet)
pey + juliet