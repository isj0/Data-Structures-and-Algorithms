class Student:

    def set_name(self, name):
        self.name = name        # class attribute

    def get_name(self):
        return self.name
    

a = Student()
a.set_name("Nirvaan")
print(a.get_name())

a.eng_marks = 45        # instance attribute
print(a.eng_marks)


x = Student()
x.set_name("Sunny")
print(x.get_name())