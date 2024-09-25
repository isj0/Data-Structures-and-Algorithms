# Python Object-Oriented Programming Basics

class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@email.com"

emp_1 = Employee("John", "Doe", 50000)
emp_2 = Employee("User", "Test", 60000)

# print(emp_1)
# print(emp_2)

# emp_1.first = "John"
# emp_1.last = "Doe"
# emp_1.email = "contact@email.com"
# emp_1.pay = 50000

# emp_2.first = "Test"
# emp_2.last = "User"
# emp_2.email = "user@email.com"
# emp_2.pay = 70000

print(emp_1.email)
print(emp_2.email)