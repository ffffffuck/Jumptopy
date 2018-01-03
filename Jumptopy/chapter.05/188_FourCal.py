class FourCal:
    def setdata(self,first,second):
        self.first = first
        self.second = second
    def sum(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first // self.second
        return result


a=FourCal()
a.setdata(8,4)

print(a.sum())
print(a.mul())
print(a.sub())
print(a.div())

#