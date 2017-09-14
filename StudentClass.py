class Student:
    '''
    This is a class which contains details about the students studying
    in out college. it stores the rollnumber first and last name in that order''' 
    def __init__(self, rollNo, firstName, lastName):
        self.firstname = firstName
        self.lastname = lastName
        self.rollNo = rollNo
    def __str__(self):
        'print a name/identifier about the object which gives a certain overview about it'
        return str(self.rollNo) + ":" + self.firstname + " " + self.lastname

s = Student(6, "Pranjal", "Aswani")

print(Student.__doc__)
print(Student.__str__.__doc__)
print(s)
