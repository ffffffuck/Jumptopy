class Restaurant:
    def __init__(self):
        self.restaurant_name = '설사'
        self.cuisine_type = '카레'
    def describe_restaurant(self):
        print("저희 레스토랑의 명칭은 [%s]이고 [%s] 전문점 입니다" %(self.restaurant_name, self.cuisine_type))
    def open_restaurant(self):
        print("저희 [%s]레스토랑 오픈했습니다 어서오세요" %(self.restaurant_name))



#ver1
kang = Restaurant()
kang.describe_restaurant()
kang.open_restaurant()


#ver2
ggyu = Restaurant()
ggyu.describe_restaurant()
ggyu.open_restaurant()

man = Restaurant()
man.describe_restaurant()
man.open_restaurant()

gga = Restaurant()
gga.describe_restaurant()
gga.open_restaurant()