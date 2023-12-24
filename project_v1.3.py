class HR():
    def __init__(self, data) -> None:        
        self.__HR_data = data
        self.hr_name = data["name"]
        
    def salaryCount(self, totalteacher):
        return totalteacher * 10000

    def feesCount(self, totalStudent):
        return totalStudent * 5000
    
    def total_revenew(self, totalteacher, totalStudent):
        return self.salaryCount(totalteacher) - self.feesCount(totalStudent)
      
    def record(self, userType : str,  input_no : int):

        self.info_list = []

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

            self.info_list.append(info)   

        return self.info_list  #[[], [], []]

    def countTotal(self):
        self.totalstudent = len(self.info_list[0])  
        self.totalteacher = len(self.info_list[1])  
        self.totalHR = len(self.info_list[2])  


class Teacher():

    def __init__(self, data) -> None:        
        self.__teacher_data = data
        self.teacher_name = data["name"]
        self.teacher_contact_info = data["contact_info"]
        self.teacher_subjects = data["subjects"]


class Student():
    def __init__(self, data) -> None: 
        self.student_data = data
    # cw, hw, performance check, result
    


class School(HR, Teacher, Student):
    def __init__(self) -> None:
        rules = """Attendance: Students are usually required to attend classes regularly,
          and there may be consequences for unexcused absences.\nPunctuality: 
          Being on time is important, whether it's for classes, exams, or other 
          school-related activities.\n\nUniform/Dress Code: Many schools have a dress 
          code or uniform policy to promote a focused and respectful learning 
          environment.\n\nRespect: Students are expected to treat teachers, staff, 
          and fellow students with respect. This includes refraining from bullying, 
          harassment, or disrespectful language."""
        print(rules)

    def total_revenew(self):
        pass




