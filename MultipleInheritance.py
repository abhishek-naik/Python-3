class father:
    def skills(self):
        print("i like gardening")

class mother:
    def skills(self):
        print("i like cooking")
        

class child(father, mother):
    def skills(self):
        father.skills(self)
        mother.skills(self)
        print("i like sports")

s = child()
s.skills()
