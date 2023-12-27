# def func(*args,**kargs):
#     for i in args:
#         print(i)
#     print("\n\n\n")
#     for i,j in kargs.items():
#         print(i,j)
        
# func(20, 30, 40, x=3, y=1, z=20)


# # function as variable
# def simple(text):
#     return text +' Hello'

# abc = simple

# print(abc("say"))


# # function as param
# def square(x):
#     return x*x

# def cube(x):
#     return x*x*x

# def new_func(func, alist):
#     result = []
#     for i in alist:
#         a = func(i)
#         result.append(a)
#     return result

# my_result1 = new_func(square,[1,2,3])
# my_result2 = new_func(cube,[1,2,3])

# print(my_result1)
# print(my_result2)



# def printing():
#     return "Text"

# def printing2():
#     return "Hello world"

# def func2(my_fuc, p):
#     print(p)
#     return my_fuc()


# xyz = func2(printing,"ok")
# pqs = func2(printing2,"None ")
# print(xyz)
# print(pqs)



# def fruit(msg):

#     def apple():
#         return msg +" in apple function"

#     return apple

# new_fruit = fruit("We are")

# print(new_fruit())


# def html_tag(tag):
#     def wrapper_func(msg):
#         print('<{0}>{1}</{0}>'.format(tag,msg))
#     return wrapper_func

# print_h1 = html_tag("h1")
# print_h1('THis is my header 1')
# print_h1('THis is my new header 1')

# print_h1 = html_tag("p")
# print_h1('THis is my paragraph 1')
# print_h1('THis is my new paragraph')


def decorator_func(sample_func):
    def wrapper_func(*args,**kargs):
        if args[0] == "admin" and args[1] == "1234":
            return sample_func(*args,**kargs)
        elif args[0] == "admin" and args[1] == "1234" and kargs["ishead"] == True:
            return secret_code(*args,**kargs)
        else:
            print("NOT AUTHORIZED")
    return wrapper_func


@decorator_func
def sample_func_as_arg(user, password):
    print("hello adsmin, you are authorized now")


# sample_func_as_arg("admin", "1234")

@decorator_func
def secret_code(user, password, ishead = False):
    return "2345"

print(secret_code("admin", "1234", ishead = False))
