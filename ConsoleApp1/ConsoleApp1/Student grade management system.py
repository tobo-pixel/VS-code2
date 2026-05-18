class Student:
    def __init__(self,lastname,firstname,middlename,matric_no,department, student_email):
        self.__lastname = lastname
        self.__firstname = firstname
        self.__middlename = middlename
        self.__name = lastname + " " + firstname + " " + middlename
        self.__matric_no = matric_no
        self.department = department
        self.__student_email = student_email
        self.__courses = {}
        self.session = "2024/25"
    def cgpa(self):
        weighed_gp = 0
        units = 0
        for course,grade in self.courses:
            if grade[1] >= 70:
                weighed_gp += 5*grade[0]
                units += grade[0]
            elif grade[1] >= 60:
                weighed_gp += 4*grade[0]
                units += grade[0]
            elif grade[1] >= 50:
                weighed_gp += 3*grade[0]
                units += grade[0]
            elif grade[1] >= 45:
                weighed_gp += 2*grade[0]
                units += grade[0]
            elif grade[1] >= 40:
                weighed_gp += 1*grade[0]
                units += grade[0]
            else:
                weighed_gp += 0
                units += grade[0]
        cgpa = weighed_gp/units
        cgpa = round(cgpa,2)
    def generate_transcript(self):
        def get_gp():
            if grade[1] >= 70:
                gp = 5
            elif grade[1] >= 60:
                gp = 4
            elif grade[1] >= 50:
                gp = 3
            elif grade[1] >= 45:
                gp = 2
            elif grade[1] >= 40:
                gp = 1
            else:
                gp = 0
            return gp
        print("COURSE\tSESSION\tUNITS\tMARKS\tGP\tWGP\tREMARKS")
        for course,grade in self.courses:
            print(f"{course}\t{self.session}\t{grade[0]}\t{grade[1]}\t{get_gp}\t{get_gp*grade[0]}\t{"PASSED" if grade[1]>=45 else "FAILED"}")
class Course:
    def __init__(self,course_code,course_description,department):
        self.course_code = course_code
        self.course_description = course_description
        self.department = department
        

        

        