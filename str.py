class Student:
    def __init__(self,rollNo,firstName,lastName):
        self.rollNo = rollNo
        self.firstname = firstName
        self.lastname = lastName
    def __str__(self):
        s_rollNo = str(self.rollNo)
        return s_rollNo+":"+self.firstname+" "+self.lastname
s= Student(34,"Abc","Jhntff")
print(s)
            
