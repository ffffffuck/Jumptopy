class Housepak:
    lastname= '박'
    def setname(self,name):
        self.fullname = self.lastname + name
    def travel(self, where):
        self.travel = where
        print(" %s, %s 여행을 가다" %(self.fullname, where))


pey = Housepak()
pey.setname('보검')
pey.travel('보라카이')
