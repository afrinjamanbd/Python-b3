from abc import ABC,abstractclassmethod
import json

class Rules(ABC):

    @abstractclassmethod
    def individualRules(self):
        pass


class School():
    def __init__(self, val) -> None:
        self.val = val
        self.info_list = [[],[],[]]

    def __record(self, userType : str,  input_no : int):

            for j in range(input_no):

                info = {}

                print(f'\nPlease add a {userType}"s info. Kindly enter "stop" to turminate.')
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

                if userType == "Student":
                    file = open('data.json')
                    previos_data = json.load(file)
                    previos_data[0]["student"].append(info)
                    file1 = open('data.json', 'w')
                    new_data = str(previos_data).replace("'",'"')
                    file1.write(new_data)


                elif userType == "Teacher":
                    file = open('data.json')
                    previos_data = json.load(file)
                    previos_data[1]["teacher"].append(info)
                    file1 = open('data.json', 'w')
                    new_data = str(previos_data).replace("'",'"')
                    file1.write(new_data)

                elif userType == "HR":
                    file = open('data.json')
                    previos_data = json.load(file)
                    previos_data[2]["hr"].append(info)
                    file1 = open('data.json', 'w')
                    new_data = str(previos_data).replace("'",'"')
                    file1.write(new_data)

                else:
                    return False

            return True

    def total_info(self): 
        file = open('data.json')
        data = json.load(file)
        return len(data[0]['student']), len(data[1]['teacher']), len(data[2]['hr'])
    

    def add_record(self):
        userType = input("Enter user type: ")
        userNo = int(input("Enter total user no: "))
        self.__record(userType,userNo)


class HR(School, Rules): 
    def __init__(self, data) -> None:        
        self.__HR_data = data
        self.hr_name = data["name"]
        super().__init__(3)
        self.totalStudent, self.totalTeacher, self.totalHR = self.total_info()
        print(self.totalStudent, self.totalTeacher, self.totalHR)
    
    
    def individualRules(self):
        rules = """
Compliance with Laws and Regulations:

Ensure compliance with local, state, and federal education laws and regulations.
Adhere to school board policies and guidelines.
Student Safety and Well-being:

Prioritize the safety and well-being of students.
Implement and enforce safety protocols, emergency procedures, and health guidelines.
Educational Standards:

Align curriculum and teaching methods with educational standards and objectives.
Monitor and assess academic performance and progress.
"""

    def TeachersalaryCount(self):
        print(self.a)
        return self.totalTeacher * 10000
    
    def HRsalaryCount(self):
        return self.totalHR * 8000
    
    def StudentFeesCount(self):
        return self.totalStudent * 3000
    
    def __total_revenew(self):
        return self.StudentFeesCount() - (self.TeachersalaryCount() + self.HRsalaryCount()) 
       


class Teacher(Rules):

    def __init__(self, data) -> None:        
        self.__teacher_data = data
        self.teacher_name = data["name"]
        self.teacher_contact_info = data["contact_info"]
        self.teacher_subjects = data["subjects"]

    def individualRules(self):
        rules = """
Professional Conduct:

Demonstrate professionalism in interactions with students, parents, colleagues, and administrators.
Uphold ethical standards and maintain the trust of the school community.
Curriculum and Lesson Planning:

Align lesson plans with curriculum standards and educational objectives.
Provide a well-organized and engaging learning experience for students.
Classroom Management:

Establish clear and consistent expectations for behavior in the classroom.
Implement effective classroom management strategies to create a positive learning environment.
"""


class Student(Rules):
    def __init__(self, data) -> None: 
        self.student_data = data

    def individualRules(self):
        rules = """
Treat teachers, staff, and fellow students with courtesy and respect.
Avoid disruptive behavior that interferes with the learning of others.
Punctuality and Attendance:

Arrive on time for classes and other scheduled activities.
Attend classes regularly and notify the school if absent.
Uniform and Dress Code:

Adhere to the school's dress code and uniform policy.
Maintain personal hygiene and grooming standards.
Classroom Behavior:

Follow classroom rules and guidelines set by teachers.
Participate actively in class discussions and activities.
Homework and Assignments:

Complete and submit homework and assignments on time.
Seek help from teachers when needed to understand and complete assignments.
"""
    # cw, hw, performance check, result
    



new_HR = {"name": "Sabrina","salary": 8000}
obj_hr = HR(new_HR)
obj_hr.add_record()
