teacher_info = {
    "name" : "Afrin", #
    "age" : 20, #
    "Dept" : "Teacher", #
    "Salary" : 10000, #
    "classes" : [4, 5, 12, 7],
    "subjects" : ["Bangla", "English", "Science"] #
}

student_info = {
    "name" : "", #
    "age" : None, #
    "fathers_name" : "Sth", #
    "class" : None, #
    "subjects" : [] #
}

hr_info = { 
    "name" : "",
    "age" : None,
    "Dept" : "HR",
    "Salary" : 20000,
}


def record(personType : str,  input_no : int):

    info_list = []

    for i in range(input_no):

        info = {}

        print(f'\nPlease add a {personType}"s info')
        firstkey = input(f'Enter key: ')
        name = input(f'Enter {personType}"s {firstkey}: ')
        age = int(input('Enter age: '))

        info[firstkey] = name # Name
        info["Age"] = age 

        if personType == 'HR' or personType == 'Teacher':
            salary = int(input('Enter salary: '))
            info["Salary"] = salary
            info["Dept"] = personType

        if personType == 'Student' :
            std_class = int(input('Enter class: '))
            fathername = int(input('Enter Father"s name: '))
            info["Class"] = std_class
            info["Fathers_name"] = fathername
        
        if personType == 'Student' or personType == 'Teacher':
            total_subject_no = int(input('Enter total subject no: '))
            subject_list = []

            for i in range(total_subject_no):
                subject_list.append(input('Enter subject name: '))

            info["Subjects"] = subject_list

        if personType == 'Teacher' : 
            total_class_no = int(input('Enter total class no: '))
            class_list = []

            for i in range(total_class_no):
                class_list.append(input('Enter subject name: '))

            info["Classes"] = class_list       

        info_list.append(info)   

    return info_list


personType = input('Enter the person type: ') 

input_no = int(input(f'How many {personType}s info you want to record? : ')) 

record_list = record(personType, input_no)

print(record_list)