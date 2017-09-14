Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print("Hello World!")
Hello World!
>>> result=(8+5)*\
	 2+\
	 9/5
>>> result
27.8
>>> print("The value of PI is %5.3f % 3.1417")
The value of PI is %5.3f % 3.1417
>>> print('The value of PI is approximately %5.2f.' % 3.1417)
The value of PI is approximately  3.14.
>>> print("Latest Python Version is: %d" %3.5)
Latest Python Version is: 3
>>> print("%20s: %d"% ('Python',3000.34))
              Python: 3000
>>> name = input("Enter your name")
Enter your name Abu
>>> print("Welcome to session on programming in Python,",name)
Welcome to session on programming in Python,  Abu
>>> customer_id= 12454
>>> customer_name="John"
>>> bill_amount=675.45
>>> x=5.3+0.9j
>>> customer_id
12454
>>> customer_name
'John'
>>> bill_amount
675.45
>>> x
(5.3+0.9j)
>>> print(customer_id,customer_name,bill_amount)
12454 John 675.45
>>> print(x.real)
5.3
>>> print(x.imag+3)
3.9
>>> 10//3
3
>>> # truncate_div
>>> a=10
>>> b=a
>>> print("Value of a & b before increment")
Value of a & b before increment
>>> print("id of a:",id(a))
id of a: 1930639264
>>> print("id of b:",id(b))
id of b: 1930639264
>>> # id_is_memoryAddress
>>> b=a+1
>>> print("Value of a & b after increment")
Value of a & b after increment
>>> print("id of a:",id(a))
id of a: 1930639264
>>> print("id of b:",id(b))
id of b: 1930639280
>>> int_a=10
>>> print("Type of 'int_a':",type(int_a))
Type of 'int_a': <class 'int'>
>>> str_b="Hello"
>>> print("Type of 'str_b':",type(str_b))
Type of 'str_b': <class 'str'>
>>> list_c=[]
>>> print("Type of 'list_c':",type(list_c))
Type of 'list_c': <class 'list'>
>>> # type_of_variable
>>> """ Use naming conventions for a good code """
' Use naming conventions for a good code '
>>> x=3
>>> if x>5:
	print("true")
	print(x)

	
>>> # Indentation
>>> #For_else_tap_enter_X2
>>> else:
	
SyntaxError: invalid syntax
>>> if x>5:
	print("true")
	print(x)

	
>>> else
SyntaxError: invalid syntax
>>> if x>5:
	print("true)
	      
SyntaxError: EOL while scanning string literal
>>> if x>5:
	print("true")
else:
	print("false")

	
false
>>> if x>3:
	print("hello")
	print(x)
elif x<10:
	print("Hola")
	print(x)
else:
	print("hi")
	print(var)
print("End")
SyntaxError: invalid syntax
>>> if x>3:
	print("hello")
	print(x)
elif x<10:
	print("Hola")
	print(x)
else:
	print("hi")
	print(var)

	
Hola
3
>>> # if_else__elif
>>> for value in range(1,6):
	print(value)

	
1
2
3
4
5
>>> for value in range(0,6,2)
SyntaxError: invalid syntax
>>> for value in range(0,6,2):
	print(value)

	
0
2
4
>>> for value in range(6,1,-2):
	print(value)

	
6
4
2
>>> for ch in "Hello World":
	print(ch.upper())

	
H
E
L
L
O
 
W
O
R
L
D
>>> var=3
>>> len([5,4,5])
3
>>> [1,3,7]+[8,9,9]
[1, 3, 7, 8, 9, 9]
>>> ['Hello']*4
['Hello', 'Hello', 'Hello', 'Hello']
>>> 7 in [1,3,7]
True
>>> for n in [1,3,7]:
	print(n)

	
1
3
7
>>> ['Hello']*4
['Hello', 'Hello', 'Hello', 'Hello']
>>> 
