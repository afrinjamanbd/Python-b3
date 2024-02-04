# student_names = ['Mohammad', 'Fatima', 'Ahmed', 
#             'Sumaiya', 'Rahman', 'Nusrat', 'Ali', 
#             'Aisha', 'Khan', 'Tasnim', 'mow']

# student_age = [23,27,25,21,30,28,22,26,24,29,28]

# # print all students name, who has m in their name and age below 25

# list_size =  len(student_names)

# # for i in range(list_size):
# #     if 'm' in student_names[i] and student_age[i] < 25:
# #         print(student_names[i])


# ## Lenear search algo
# numbers = [45, 163, 36, 120, 32, 91, 55, 188, 104, 70, 27, 199, 67, 143, 36]

# lenght = len(numbers)

# flag = False

# for i in range(lenght):
#     if numbers[i] == 36:
#         print('found ' , numbers[i], ' in position ', i+1)
#         flag = True
#         # break
# if flag == False:
#         print('not found')
        

# for i in range(2,21):
#     for j in range(1, 11):
#         print(i, " x ", j, ' = ', i*j )



# name = input('please write your name: ')

# while name != '0':

#     if name == 'Afrin':
#         print("Hi Afrin! You are instruction." )
#     elif name == 'Devskill':
#         print('Oh its an org!')
#     else:
#         print('Hi '+ name)

#     name = input('please write your name: ')


# array = [1, 5 ,24, 36, 47, 66, 78, 79, 89, 95]

# target = int(input('Which number to find? : ')) 
 
# low = 0

# high = len(array)

# if array[0] == target:
#     print('found in 1st position')

# elif array[high - 1] == target:
#     print('found in last position')

# else:
#     while(low <= high):

#         mid = int((low+high)/2) #8

#         if array[mid] == target:
#                 print(mid + 1)
#                 break

#         elif array[mid] < target:
#                 low = mid + 1 # 9

#         else :
#                high = mid - 1 # 7

#     if (high < low):
#       ('not found')


my_data = {
    "name": "Afrin",
    "age" : 15,
    "class" : 9,
    "school": {
        "name" : "xyz",
        "address" : None
    },
    "mother" : {
        "name": "My mom",
        "age" : None,
        "mother" : {
            "name": None,
            "age" : 45,
        }
    }
}


def recurse(my_data: dict):
    for k, v in my_data.items():
        if isinstance(v, dict):
            return recurse(v)
        if v == None:
            my_data[k] = "no val"

print(recurse(my_data))



