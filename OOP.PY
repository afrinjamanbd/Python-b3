class A():

    p = 3
    q = 6
    r = 12

    def __init__(self, x, y, z):      
        self.x = x
        self.y = y
        self.z = z
        print(self.x)
        print(A.p) 

    def add(self):
        return self.x + self.y
    
    def noSelf():
        print('Working')

         
# obj_a1 = A(2, 3, 4)
# a = obj_a1.add()
# print(type(a))


# obj_a2 = A('hI ', "welcome", "Here")
# print(obj_a2.add())



class B(A):
    
    a = 20
    b = 30
    c = 40

    def __init__(self, b1, b2):
        # super().__init__(30, B.b , B.c)
        self.bOne = b1
        self.bTwo = b2

    
    def printing(self, exttraText):
        print(exttraText + self.bOne)
        print(exttraText + self.bTwo)
        print(B.p)
        print(self.add())

    def add(self):
        return "adding "
    


class C(B):
    def __init__(self):
        self.x = 30
        self.y = 50
        print('Class C Calling ')

    def add(self):
        print('Class C add')



obj_c1 = C()
obj_c1.add()

obj_b1 = B("Afrin", "Devskill")

# obj_b1.printing("How are you, ")