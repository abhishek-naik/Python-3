class myclass:
    def add(self,num1,num2):
        num3=num1+num2
        return num3

    def sub(self,num1,num2):
        num3=num1-num2
        return num3

    def mul(self,num1,num2):
        num3=num1*num2
        return num3

    def div(self,num1,num2):
        num3=num1/num2
        return num3

m1=myclass()
print(m1.add(4,5))
print(m1.sub(4,5))
print(m1.mul(4,5))
print(m1.div(4,5))
