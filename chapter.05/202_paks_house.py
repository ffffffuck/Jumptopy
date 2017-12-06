class Housepak:
    lastname= '박'
    def __init__(self,name):
        self.fullname = self.lastname + name
    def travel(self, where):
        self.travel = where
        print(" %s, %s 여행을 가다." %(self.fullname, where))

pey= Housepak('보검')
pey.travel('보라카이')

class HouseKim(Housepak):
    lastname= '김'
    def travel(self,where,day):
        self.time = day
        print(" %s, %s여행 %s일 가네." %(self.fullname,where,day))


pi = HouseKim('대곤')
pi.travel('마산','3')