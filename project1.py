teacher_info = {
    "name" : "Afrin",
    "age" : 20,
    "classes" : [4,5, 12, 7],
    "subjects" : ["Bangla", "English", "Science"]
}

students_no = int(input('How many students info you want to record? : '))

student_info_list = []

for i in range(students_no):

    student_info = {
        "name" : "",
        "age" : None,
        "class" : None,
        "subjects" : []
    }

    print('\nPlease add a student info')
    name = input('Enter student name: ')
    age = int(input('Enter age: '))
    std_class = int(input('Enter class: '))
    total_subject_no = int(input('Enter total subject no: '))
    subject_list = []

    for i in range(total_subject_no):
        subject_list.append(input('Enter subject name: '))

    student_info["name"] = name
    student_info["age"] = age
    student_info["class"] = std_class
    student_info["subjects"] = subject_list

    student_info_list.append(student_info)   

print(student_info_list)


