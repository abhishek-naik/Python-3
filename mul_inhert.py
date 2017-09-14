class Student:
    def getdata(self, n, r, p):
        self.name = n
        self.rollnumber = r
        self.pointer = p
    def putdata(self):
        print("name of the student: %s" %(self.name))
        print("roll number of the student: %d"  %(self.rollnumber))
        print("pointer of the student: %.2f" %(self.pointer))


class ExtendedStudent(Student):
    def getdata(self, n, r, p, a):
        super().getdata(n, r, p)
        self.address = a
    def putdata(self):
        super().putdata()
        print("address: %s" %(self.address))


name = input("Enter name: ")
roll = int(input("Enter roll number: "))
pointer = float(input("Enter pointer: "))
address = input("Enter address: ")

stud1 = ExtendedStudent()
stud1.getdata(name,roll,pointer,address)
stud1.putdata()

