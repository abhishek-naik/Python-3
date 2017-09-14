class father:
    def skills(self):
        print("I enjoy gardening")

class mother:
    def skills(self):
        print("I love cooking")

class son(father,mother):
    def skills(self):
        father.skills(self)
        mother.skills(self)
        print("I enjoy sports")

s=son()
s.skills()


