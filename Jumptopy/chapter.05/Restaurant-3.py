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
        self.number_served = self.number_served + number
        print("서빙한 고객 숫자는 %s명 입니다" %number)
    def increment_number_served(self,number):
        self.number_served = self.number_served+number
        print("오늘 하루동안 서빙한 고객은 %s명 입니다" %self.number_served)
    def __del__(self):
        print("영업을 마칩니다.")


kang = Restaurant()
kang.describe_restaurant()
kang.set_number_served(7)

kang.increment_number_served(12)