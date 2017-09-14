class Student:
    def __init__(self, n, r, p):
        self.name = n
        self.rollnumber = r
        self.pointer = p
    def display(self):
        print("name of the student: %s" %(self.name))
        print("roll number of the student: %d"  %(self.rollnumber))
        print("pointer of the student: %.2f" %(self.pointer))


class ExtendedStudent(Student):
    def add_address(self, a):
        self.address = a
    def display(self):
        print("name of the student: %s" %(self.name))
        print("roll number of the student: %d"  %(self.rollnumber))
        print("pointer of the student: %.2f" %(self.pointer))
        print("address: %s" %(self.address))


name = input("Enter name: ")
roll = int(input("Enter roll number: "))
pointer = float(input("Enter pointer: "))
address = input("Enter address: ")
stud1 = ExtendedStudent(name, roll, pointer)
stud1.add_address(address)
stud1.display()

