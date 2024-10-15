class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "_" + last + "@xyz.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    def appy_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount


print(Employee.num_of_emps)
print(Employee.raise_)
emp1 = Employee("Sunny", "J", 500)
emp2 = Employee("Test", "User", 700)

print(Employee.num_of_emps)

