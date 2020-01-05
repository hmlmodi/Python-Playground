class Student():
    def __init__(self):
        print("my id ")
    def name(self):
        print("my name")
    def city(self):
        print("my city")

#my_student = Student()
#my_student.city()

class School(Student):
    def __init__(self):
        School.__init__(self)
        print("my school")

my_newname=School()
School.city()