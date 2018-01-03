class Restaurant:
    number_served=0
    def __init__(self):
        self.restaurant_name = '설사'
        self.cuisine_type = '카레'
    def describe_restaurant(self):
        print("저희 레스토랑의 명칭은 [%s]이고 [%s] 전문점 입니다" %(self.restaurant_name, self.cuisine_type))
    def open_restaurant(self):
        print("저희 [%s]레스토랑 오픈했습니다 어서오세요" %(self.restaurant_name))
    def set_number_served(self,number):
        self.number_served = number
        print("서빙한 고객 숫자는 %s명 입니다" %number)
    def increment_number_served(self,number):
        self.number_served = self.number_served + number
        print("오늘 하루동안 서빙한 고객은 %s명 입니다" %self.number_served)
    def custumor__served_log(self):
        f= open("고객현황로그.txt", 'r')
        line = f.readlines()
        f = open("고객현황로그.txt",'a')
        f.write('\n'+str(self.number_served+int(line[-1])))
        f.close()

class GGobong(Restaurant):
    number=0
    def __init__(self):
        self.restaurant_name = '변비'
        self.cuisine_type = '초콜렛'
    def jjoggoreddo(self):
        self.gana = 10000
        print("변비 초콜렛 판매가격은 %s원입니다" %self.gana)
    def set_number_served(self):
        while True:
            self.number = int(input("몇명 오셨습니까?[0입력 영업종료]:"))
            self.number_served += self.number
            print("서빙한 고객 숫자는 %s명 입니다" %self.number)
            if self.number == 0 :
                break
    def increment_number_served(self):
        self.number_served += self.number
        print("오늘 하루동안 방문한 고객은 %s명 입니다" %self.number_served)
    def custumor__served_log(self):
        f = open("수익.txt", 'r')
        money = f.readlines()
        f = open("수익.txt", 'a')
        f.write('\n'+str(self.gana*self.number_served + int(money[-1])))
        print("하루동안의 수익은 %s원입니다" %(self.gana*self.number_served))
        f= open("영업일자2.txt", 'r')
        day = f.readlines()
        f= open("영업일자2.txt", 'a')
        f.write('\n'+str(1+int(day[-1])))
        f= open("고객현황로그2.txt", 'r')
        line = f.readlines()
        f = open("고객현황로그2.txt", 'a')
        f.write('\n' + str(self.number_served + int(line[-1])))
        f = open("영업일자2.txt", 'r')
        day = f.readlines()
        print("오늘은 영업 %s일째 입니다." %day[-1])
        f = open("고객현황로그2.txt", 'r')
        line = f.readlines()
        print("지금까지 방문한 총 고객숫자는 %s명 입니다" % line[-1])
        f = open("수익.txt", 'r')
        line = f.readlines()
        print("지금까지의 총수익은 %s원 입니다" % line[-1])
        f.close()


kang = Restaurant()
kang.describe_restaurant()
#kang.set_number_served(0)
kang.increment_number_served(50)
kang.custumor__served_log()

print()

ddong = GGobong()
ddong.describe_restaurant()
ddong.jjoggoreddo()
ddong.set_number_served()
ddong.increment_number_served()
ddong.custumor__served_log()



