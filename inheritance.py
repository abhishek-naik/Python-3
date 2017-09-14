class father:
    def gardening(self):
        print("I enjoy gardening")

class mother:
    def cooking(self):
        print("I love cooking")

class son(father,mother):
    def sports(self):
        print("I enjoy sports")

s=son()
s.gardening()
s.cooking()
s.sports()
    
