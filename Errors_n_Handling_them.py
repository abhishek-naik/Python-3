#Errors & Exceptions

def zerodiv(divideBy):
    return 42/divideBy
print(zerodiv(2))
print(zerodiv(0))
print(zerodiv(42))

#Handling the errors

def divError(divNum):
    try:
        return 45/divNum
    except ZeroDivisionError:
        print("Hey!? you tried to divide by zero")

print(divError(5))
print(divError(0))
print(divError(55))


#Input Validation

print("How many cats do you own")
numCats = input()
try:
    if int(numCats) >= 4:
        print("Woww!! so many of them.")
    else:
        print("Ohh, you have quite a few cats")

except ValueError:
    print("Please type a number.")
