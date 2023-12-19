try:
    myInput = int(input("Please enter a number: "))
    a = 0 / myInput
except ValueError as e:
    print("ValueError: ", str(e))
except ZeroDivisionError as e:
    print("ZeroDivisionError: ", str(e))
except Exception as e:
    print(str(e))
else:
    print(a)
finally:
    print("DOne with try except topic")



def strf():
    return "H i"

x = "Hi"

try:
    assert x == strf(), "Assert Error"
    print(x)
except AssertionError as a :
    print(a)
