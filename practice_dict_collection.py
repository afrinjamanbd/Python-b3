my_data = {
    "name" : "Afrin",
    "age" : 80,
    "foo" : True,
    "my_list" : [23, 45, 65, 100],
    True : {
        "nested_data" : 1.5
    }  
}

new_data = {
    "name" : "Synthia",
    "age" : 20,
    "foo" : True,
    "list_val" : [23, 45, 65, 100],
    True : 'Student' 
}

data_3 = {
    "name" : "Synthia",
    "age" : 20,
    "foo" : True,
    "list_val" : [23, 45, 65, 100],
    True : 'Student' 
}

# if my_data['age'] == 10 or my_data['name'] == 'Afrin':
#     print('Hi afrin')

# elif my_data['age'] == 80 or my_data['name'] == 'Synthia':
#     print(my_data[True]["nested_data"])


# from collections import Counter

# my_counter = Counter("Afrin Jaman")

# print(my_counter) 


# from collections import OrderedDict

# od = OrderedDict()


# from collections import ChainMap

# chain_map = ChainMap(my_data, new_data, data_3)

# # print(chain_map)

# from collections import deque 
    
# # Declaring deque 
# queue = deque(['name','age','DOB'])

# queue.popleft()

# print(queue)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

numlist = [23, 12, 4, 5, 89]

newnumlist = [numlist.pop() for y in numlist if y%2 == 0]  

print(numlist)

print(newnumlist)






















