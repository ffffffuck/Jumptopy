class Calculator:
    n=0
    def __init__(self,N):
        self.N = N
    def sum(self):
        n=0
        for i in self.N:
            n +=i
        return n
    def avg(self):
        n=0
        for a in self.N:
            self.n=self.n+a
            result = self.n//len(self.N)
        return result


if __name__== "__main__":
    cal1=Calculator([1,2,3,4,5])
    print(cal1.sum())
    print(cal1.avg())

    cal2=Calculator([6,7,8,9,10])
    print(cal2.sum())
    print(cal2.avg())



