class Employee:
    raise_amount = 1.04

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

Employee.set_raise_amount(1.02)
e1 = Employee("p", 50000)
e2 = Employee("a", 40000)

e1.set_raise_amount(1.05)
print(e1.raise_amount)
print(e2.raise_amount)


