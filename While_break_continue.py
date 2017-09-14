# while_loop example
spam = 0
while spam < 5:
    print("Hello, I'm spam!")
    spam = spam + 1

#input_validation
name = ''
while name != 'Abu':
    print("Please enter your name!")
    name = input()
print("Thank youu!")


#break_example
name = ''
while True:
    print("Please enter your name!")
    name = input()
    if name == 'Abu':
        break
print("Thank youu!")


#continue_example
spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print("Spam = " + str(spam))
