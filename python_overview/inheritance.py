class Parent:

    def __init__(self):
        self.supper_atribute = True
        print("Parent Class")
    
class Child(Parent):
    
    def __init__(self):
        super().__init__()
        print("Child")
        print(self.supper_atribute)

child = Child()