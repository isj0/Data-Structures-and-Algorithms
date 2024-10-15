# public access modifier
# class ABC:

#     def __init__(self):
#         self.public_attribute = None

#     def public_function():
#         pass

# obj1 = ABC()
# obj1.public_attribute
# obj1.public_function()

# private access modifier
# class ABC:

#     def __init__(self):
#         self.__private_attribute = 10

#     def __private_function():
#         pass

# obj1 = ABC()
# print(obj1.__private_attribute)


# protected modifier
class ABC:

    def __init__(self):
        self._protected_attribute = 10

    def _protected_function():
        pass

obj1 = ABC()
print(obj1.__private_function())