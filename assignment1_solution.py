teacher_info = {
    "id": None,
    "name" : "Afrin", #
    "age" : 20, #
    "address": "",
    "contact_info": None,
    "Dept" : "Teacher", #
    "Salary" : 10000, #
    "classes" : [4, 5, 12, 7],
    "subjects" : ["Bangla", "English", "Science"] #
}

student_info = {
    "id": None,
    "name" : "", #
    "age" : None, #
    "address": "",
    "fathers_name" : "Sth", #
    "class" : None, #
    "subjects" : [] #
}

hr_info = { 
    "id": None,
    "name" : "",
    "age" : None,
    "address": "",
    "Dept" : "HR",
    "Salary" : 20000,
}


def record(userType : str,  input_no : int):

    info_list = []

    for j in range(input_no):

        info = {}

        print(f'\nPlease add a {userType}"s info. Kindly enter stop to turminate.')
        key = input(f'Enter first key: ')

        if key != "":

            while(key != "stop"):
                value = input(f'Enter {userType}"s information for this feild ->{key}: ')
                info[key] = value
                key = input(f'Enter another key: ')

        if userType == 'HR' or userType == 'Teacher':
            salary = int(input('Enter salary: '))
            info["Salary"] = salary
            info["Dept"] = userType

        if userType == 'Student' :
            std_class = int(input('Enter class: '))
            fathername = input('Enter Father"s name: ')
            info["Class"] = std_class
            info["Fathers_name"] = fathername
        
        if userType == 'Student' or userType == 'Teacher':
            total_subject_no = int(input('Enter total subject no: '))
            subject_list = []

            for i in range(total_subject_no):
                subject_list.append(input('Enter subject name: '))

            info["Subjects"] = subject_list

        if userType == 'Teacher' : 
            total_class_no = int(input('Enter total class no: '))
            class_list = []

            for i in range(total_class_no):
                class_list.append(input('Enter subject name: '))

            info["Classes"] = class_list       

        info_list.append(info)   

    return info_list




userType = input('Enter the user type: ') 

input_no = int(input(f'How many {userType}s info you want to record? : ')) 

# callig record function
record_list = record(userType, input_no)

print(record_list)