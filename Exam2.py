class A:
     def __init__(self):
         self.__i = 1
         self.j = 5
 
     def display(self):
         print(self.__i, self.j)


class B(A):
     def __init__(self):
         super().__init__()
         self.__i = 2
         self.j = 7  


c = B()
c.display()