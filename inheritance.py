class Student():

    def __init__(self):
        print("my id ")

    def name(self):
        print("my name")

    def city(self):
        print("my city")

class School(Student):
    def __init__(self):
        Student.__init__(self)
        print("my school")
my_school=School()
my_school.city()