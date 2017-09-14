class Critter(object):
    total = 0

    def status():
        print("Total critters",Critter.total)

    status = staticmethod(status)

    def __init__(self,name):
        Critter.total += 1
        self.name = name
    def getname(self):
        print(self.name)
        
print(Critter.total)
crit1 = Critter("ABU")
crit1.status()
crit2 = Critter("gfdgdg")
crit2.status()
