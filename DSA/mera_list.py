import ctypes

class MeraList:

    def __init__(self):
        self.size = 1
        self.n = 0
        # create a C type array with size = self.size
        self.A = self.__create__array(self.size)

    def __len__(self):
        return self.n
    
    def __str__(self):
        result = ""
        for i in range(self.n):
            result = result + str(self.A[i]) + ","

        return "[" + result[:-1] + "]"
    
    def __getitem__(self, index):
        if 0 <= index < self.n:
            return self.A[index]
        else:
            return "IndexError - Index out of range."
        
    def __delitem__(self, pos):

        if 0 <= pos < self.n:

            for i in range(pos, self.n-1):
                self.A[i] = self.A[i+1]

            self.n = self.n - 1
    
    def append(self, item):
        if self.n == self.size:
            # resize
            self.__resize(self.size*2)

        self.A[self.n] = item
        self.n = self.n + 1

    def pop(self):
        if self.n == 0:
            return "Empty list"

        print(self.A[self.n - 1])    
        self.n = self.n - 1

    def clear(self):
        
        self.n = 0
        self.size = 1

    def find(self, item):

        for i in range(self.n):
            if self.A[i] == item:
                return i
            
        return "Value Error!"

    def insert(self, pos, item):

        if self.n == self.size:
            self.__resize(self.size*2)

        for i in range(self.n, pos, -1):
            self.A[i] = self.A[i - 1]

        self.A[pos] = item
        self.n = self.n + 1

    




    def __resize(self, new_capacity):
        # create a new array with new capacity
        B = self.__create__array(new_capacity)
        self.size = new_capacity
        # copy the content of A to B
        for i in range(self.n):
            B[i] = self.A[i]
        # reaasign A
        self.A = B

    def __create__array(self,capacity):
        # create a C type array with size capacity
        return (capacity * ctypes.py_object)()
    

L = MeraList()

print(type(L))

print(L)

print(len(L))

L.append("Hello")
L.append(3.141)
L.append(True)
L.append(100)

print(L[0])
# L.pop()
print(L)
# L.clear()
print(L.find(100))

L.insert(0, "A")

print(L)

del(L[0])

print(L)
