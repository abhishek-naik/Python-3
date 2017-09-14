#For loop eg
for i in range(0,3):
    print("Hello, I'm " +str(i))

#
print(range(4))

#For loop using lists
for i in [0,1,2,3]:
    print(i)
    
#list function
print(list(range(4)))

#lists for larger data
TwosTable = list(range(0,101,2))
print(TwosTable)

#For i in range(len(**Some list**)):

supplies = ['pens','pencils','staplers','notepads']
for i in range(len(supplies)):
    print("Index " + str(i) + " in supplies is " + supplies[i])

#Multiple assignment

cat = ['Fat','Loud','Orange']
size,nature,color = cat
print(size,color,nature)

size,color,nature = 'Skinny','Brown','Evil'
print(size,color,nature)

#Swapping variables

a = "AAA"
b = "BBB"

a,b = b,a
print(a,b)
print(" A = " + a + " & B = " + b)

#Augmented Assignment operators

spam = 45
spam =  spam + 1
print(spam)
spam += 1          #spam = spam + 1
print(spam)

spam *= 2          #spam = spam * 2
print(spam)
                                                           
