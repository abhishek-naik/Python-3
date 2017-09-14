#Variables in local scope cannot be accessed by the code in global scope 

def spam():
    eggs = 95
spam()
print(eggs)

#Local variables in two different functions are totally different from one another (if both have same name)

def spam():
    eggs = 95
    bacon()
    print(eggs)
def bacon():
    ham = 100
    eggs = 0

spam()

#Code in the local scope can access the global variable

def spam():
    print(eggs)

eggs = 456
spam()

#Global statements

def spam():
    global eggs
    eggs = 4568
    print(eggs)

eggs = 000
spam()
print(eggs)
