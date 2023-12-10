from random import randint
ab  = 10

def add():
    print('a' + 'b')

add()


def addstr(a, b):
    print(a+b)

addstr('Hi! ', 'How are you?')



def numfunc():
    return randint(0, 10)

print(numfunc())



def randnum(x, y):
    x = x - 1 
    print('Recieved random number')
    return randint(x, y)

print(randnum(20, 200))



