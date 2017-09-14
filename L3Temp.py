#List methods:


#Index()

spam = ['hey','hello','howdy','hoi']
print(spam.index('hello'))

#Append()

spam = ['cats','dogs','rats']
spam.append("mouse")
print(spam)

#Insert()

print(spam)
spam.insert(1, 'mouse')
print(spam)

#Remove()

spam = ['cats','cats','dogs']
spam.remove('cats')
print(spam)

    #Del (Alternative)

spamm = ['cats','dogs','rats']
del spamm[2]
print(spamm)

#Sort()

spam = [4,22,4.5,88.1,-4,0.2]
spam.sort()
print(spam)

spam = ['cats','ants','badgers','elephants']
spam.sort()
print(spam)

spam = ['Alice','Bob','birds','ants','Carol']
spam.sort()
print(spam)

spam = ['A','a','Z','z']
spam.sort()
print(spam)

#Sort with keyword arguement

spam = ['A','a','z','Z']
spam.sort(key = str.lower)
print(spam)

