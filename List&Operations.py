#Lists

#boom = ['kaboom','bang']

#print(boom)

#index (Accessing the items inside the list)

#print(boom[1])

#List of lists

#spam = [['cats','dogs'],[10,20,30,40],['douglas','costa','diego','go','pro']]

#print(spam[0][1])

#Negative Indexes
#print(boom[-1])
#print(spam[-2][-3])


#print("Lol! " + spam[-1][-4] + " scored only " + str(spam[-2][-4]) + " goals this summer")

#Slice

#lst = [1,2,3,4,5]
#print(lst[1:3])

#Changing a list's items

spam = [10,20,30]
spam[1] = 'Hello'
spam[2] = 'World'
print(spam)
spam[1:2] = ['Yoko','Sizzler']
print(spam)
spam[0:2] = ['Mista','world','wide']
print(spam)

#Deleting items

spam = ['cats','dogs','rats']
del spam[2]
print(spam)

#String list similarities

#1 Concatenation

cons = [1,2,3] + [4,5,6]
print(cons)

#2 String/List replication

cons = [1,2] * 2
print(cons)

# list() function

print(list('abcd'))

# in and not in operators

#1 In

print('Howdy' in ['Hello','Howdy','Heyo','Yoo'])

print(42 in [4,5,6])

#2 not in

print(45 not in [44,33,22])



